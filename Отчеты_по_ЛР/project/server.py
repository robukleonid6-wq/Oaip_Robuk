#!/usr/bin/env python3
"""
Простой HTTP сервер на чистом Python с использованием сокетов
Поддерживает GET/POST запросы и обслуживание статических файлов
"""

import socket
import os
import sys
import mimetypes
import urllib.parse
import json
from datetime import datetime
import argparse
import threading
import signal

class HTTPServer:
    
    def __init__(self, host='localhost', port=8080, static_dir='static'):
        self.host = host
        self.port = port
        self.static_dir = static_dir
        self.running = False
        self.server_socket = None
        self.routes = {}
        
        # Регистрация маршрутов по умолчанию
        self.register_default_routes()
    
    def register_default_routes(self):
        self.routes['GET'] = {}
        self.routes['POST'] = {}
        
        # Маршрут по умолчанию
        self.routes['GET']['/'] = self.handle_root
        self.routes['GET']['/index.html'] = self.handle_root
        
        # Маршрут для API
        self.routes['GET']['/api/status'] = self.handle_api_status
        self.routes['POST']['/api/echo'] = self.handle_api_echo
        
        # Маршрут для формы
        self.routes['GET']['/form'] = self.handle_form_get
        self.routes['POST']['/form'] = self.handle_form_post
    
    def start(self):
        """Запуск сервера"""
        try:
            # Создание сокета
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Привязка к хосту и порту
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            self.running = True
            print(f"[+] Сервер запущен на http://{self.host}:{self.port}")
            print(f"[+] Статические файлы из директории: {self.static_dir}")
            print("[+] Для остановки нажмите Ctrl+C\n")
            
            # Обработка сигналов для корректного завершения
            signal.signal(signal.SIGINT, self.shutdown)
            signal.signal(signal.SIGTERM, self.shutdown)
            
            # Основной цикл сервера
            while self.running:
                try:
                    # Принятие соединения
                    client_socket, client_address = self.server_socket.accept()
                    print(f"[*] Подключение от {client_address[0]}:{client_address[1]}")
                    
                    # Обработка соединения в отдельном потоке
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, client_address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
                except OSError:
                    break
                    
        except Exception as e:
            print(f"[-] Ошибка при запуске сервера: {e}")
            sys.exit(1)
    
    def shutdown(self, signum=None, frame=None):
        print("\n[!] завершение работы сервера...")
        self.running = False
        
        if self.server_socket:
            self.server_socket.close()
        
        sys.exit(0)
    
    def handle_client(self, client_socket, client_address):
        try:
            # Получение данных от клиента
            request_data = client_socket.recv(4096).decode('utf-8')
            
            if not request_data:
                return
            
            # Разбор запроса
            method, path, headers, body = self.parse_request(request_data)
            
            # Обработка запроса
            response = self.handle_request(method, path, headers, body)
            
            # Отправка ответа
            client_socket.sendall(response.encode('utf-8'))
            
        except Exception as e:
            print(f"[-] Ошибка обработки запроса: {e}")
            error_response = self.create_response(
                500, 
                "Internal Server Error",
                "text/plain",
                f"Server Error: {str(e)}"
            )
            client_socket.sendall(error_response.encode('utf-8'))
        
        finally:
            client_socket.close()
            print(f"[*] Соединение с {client_address[0]}:{client_address[1]} закрыто")
    
    def parse_request(self, request_data):
        lines = request_data.strip().split('\r\n')
        
        if not lines:
            raise ValueError("Пустой запрос")
        
        # Первая строка: метод, путь, версия протокола
        method, path, version = lines[0].split(' ', 2)
        
        # Заголовки
        headers = {}
        body = ""
        i = 1
        
        # Чтение заголовков
        while i < len(lines) and lines[i]:
            if ': ' in lines[i]:
                key, value = lines[i].split(': ', 1)
                headers[key.lower()] = value
            i += 1
        
        # Тело запроса (если есть)
        if i < len(lines) - 1:
            body = '\r\n'.join(lines[i+1:])
        
        return method, path, headers, body
    
    def handle_request(self, method, path, headers, body):
        try:
            # Разбор пути и параметров запроса
            parsed_path = urllib.parse.urlparse(path)
            clean_path = parsed_path.path
            
            # Проверка на статический файл
            if clean_path.startswith('/static/'):
                return self.serve_static_file(clean_path[8:])
            
            # Проверка маршрутов
            if method in self.routes and clean_path in self.routes[method]:
                handler = self.routes[method][clean_path]
                return handler(path, headers, body)
            
            # Пробуем обслужить как статический файл
            if os.path.exists(os.path.join(self.static_dir, clean_path.lstrip('/'))):
                return self.serve_static_file(clean_path.lstrip('/'))
            
            # Если файл не найден
            return self.create_response(
                404,
                "Not Found",
                "text/html",
                self.error_page(404, "Страница не найдена")
            )
            
        except Exception as e:
            print(f"[-] Ошибка обработки запроса: {e}")
            return self.create_response(
                500,
                "Internal Server Error",
                "text/html",
                self.error_page(500, str(e))
            )
    
    def serve_static_file(self, file_path):
        """Обслуживание статических файлов"""
        try:
            # Защита от path traversal атак
            safe_path = os.path.normpath(file_path).lstrip('/')
            full_path = os.path.join(self.static_dir, safe_path)
            
            if not os.path.exists(full_path):
                return self.create_response(
                    404,
                    "Not Found",
                    "text/html",
                    self.error_page(404, f"Файл {file_path} не найден")
                )
            
            # Определение MIME-типа
            mime_type, _ = mimetypes.guess_type(full_path)
            if not mime_type:
                mime_type = 'application/octet-stream'
            
            # Чтение файла
            with open(full_path, 'rb') as f:
                content = f.read()
            
            return self.create_response(
                200,
                "OK",
                mime_type,
                content,
                is_binary=True
            )
            
        except PermissionError:
            return self.create_response(
                403,
                "Forbidden",
                "text/html",
                self.error_page(403, "Доступ запрещен")
            )
        except Exception as e:
            return self.create_response(
                500,
                "Internal Server Error",
                "text/html",
                self.error_page(500, str(e))
            )
    
    def handle_root(self, path, headers, body):
        # Обработка корневого пути
        index_path = os.path.join(self.static_dir, 'index.html')
        
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return self.create_response(
                200,
                "OK",
                "text/html",
                content
            )
        else:
            welcome_page = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Простой веб-сервер</title>
            <meta charset="utf-8">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 10px;
                    background: #f9f9f9;
                }
                h1 { color: #333; }
                .success { color: green; font-weight: bold; }
                .links { margin: 20px 0; }
                .links a {
                    display: block;
                    margin: 10px 0;
                    padding: 10px;
                    background: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                }
                .links a:hover { background: #45a049; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Простой веб-сервер</h1>
                <div class="links">
                    <h3>Доступные страницы:</h3>
                    <a href="/static/index.html">Главная страница</a>
                    <a href="/form">Тестовая форма</a>
                    <a href="/api/status">Статус API</a>
                </div>
              
            </div>
        </body>
        </html>
            """.format(port=self.port, static_dir=self.static_dir)
            
            return self.create_response(
                200,
                "OK",
                "text/html",
                welcome_page
            )
    
    def handle_form_get(self, path, headers, body):
        # Обработка GET запроса формы
        form_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Тестовая форма</title>
            <meta charset="utf-8">
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                form { max-width: 400px; margin: 0 auto; }
                input, textarea { width: 100%; padding: 10px; margin: 10px 0; }
                button { background: #4CAF50; color: white; padding: 10px 20px; border: none; }
            </style>
        </head>
        <body>
            <h1>Тестовая форма</h1>
            <form method="POST" action="/form">
                <input type="text" name="name" placeholder="Ваше имя" required>
                <input type="email" name="email" placeholder="Email" required>
                <textarea name="message" placeholder="Сообщение" rows="5"></textarea>
                <button type="submit">Отправить</button>
            </form>
            <p><a href="/">На главную</a></p>
        </body>
        </html>
        """
        
        return self.create_response(
            200,
            "OK",
            "text/html",
            form_html
        )
    
    def handle_form_post(self, path, headers, body):
        # Обработка POST запроса формы
        try:
            # Парсинг данных формы
            params = urllib.parse.parse_qs(body)
            
            # Подготовка данных
            name = params.get('name', [''])[0]
            email = params.get('email', [''])[0]
            message = params.get('message', [''])[0]
            
            result_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Результат формы</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .success {{ color: green; }}
                </style>
            </head>
            <body>
                <h1 class="success">Форма успешно отправлена!</h1>
                <p><strong>Имя:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Сообщение:</strong> {message}</p>
                <p><a href="/form">Вернуться к форме</a> | <a href="/">На главную</a></p>
            </body>
            </html>
            """
            
            return self.create_response(
                200,
                "OK",
                "text/html",
                result_html
            )
            
        except Exception as e:
            return self.create_response(
                400,
                "Bad Request",
                "text/html",
                self.error_page(400, f"Ошибка обработки формы: {str(e)}")
            )
    
    def handle_api_status(self, path, headers, body):
        """Обработка API статуса"""
        status_data = {
            "status": "running",
            "server": "Simple Python HTTP Server",
            "timestamp": datetime.now().isoformat(),
            "host": self.host,
            "port": self.port,
            "static_dir": self.static_dir
        }
        
        return self.create_response(
            200,
            "OK",
            "application/json",
            json.dumps(status_data, indent=2)
        )
    
    def handle_api_echo(self, path, headers, body):
        """Эхо-API, возвращает полученные данные"""
        echo_data = {
            "method": "POST",
            "timestamp": datetime.now().isoformat(),
            "headers": dict(headers),
            "body": body
        }
        
        return self.create_response(
            200,
            "OK",
            "application/json",
            json.dumps(echo_data, indent=2)
        )
    
    def create_response(self, status_code, status_text, content_type, content, is_binary=False):
        # Создание HTTP ответа
        if is_binary:
            content_length = len(content)
            response = f"HTTP/1.1 {status_code} {status_text}\r\n"
            response += f"Content-Type: {content_type}\r\n"
            response += f"Content-Length: {content_length}\r\n"
            response += "Connection: close\r\n"
            response += "\r\n"
            response = response.encode('utf-8') + content
            return response.decode('latin-1')  # Для совместимости
        else:
            response = f"HTTP/1.1 {status_code} {status_text}\r\n"
            response += f"Content-Type: {content_type}; charset=utf-8\r\n"
            response += f"Content-Length: {len(content.encode('utf-8'))}\r\n"
            response += "Connection: close\r\n"
            response += "\r\n"
            response += content
            return response
    
    def error_page(self, code, message):
        # страницы ошибки
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ошибка {code}</title>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; text-align: center; }}
                .error {{ color: #d32f2f; font-size: 72px; margin: 20px; }}
                .message {{ font-size: 24px; margin: 20px; }}
            </style>
        </head>
        <body>
            <div class="error">{code}</div>
            <div class="message">{message}</div>
            <p><a href="/">Вернуться на главную</a></p>
        </body>
        </html>
        """

def main():
    # Главная функция для запуска сервера из командной строки
    parser = argparse.ArgumentParser(description='Простой HTTP сервер на Python')
    parser.add_argument('--host', default='localhost', help='Хост для привязки (по умолчанию: localhost)')
    parser.add_argument('--port', type=int, default=8080, help='Порт для прослушивания (по умолчанию: 8080)')
    parser.add_argument('--static', default='static', help='Директория со статическими файлами (по умолчанию: static)')
    
    args = parser.parse_args()
    
    # Проверка существования директории static
    if not os.path.exists(args.static):
        print(f"[!] Директория '{args.static}' не найдена. Создаю...")
        os.makedirs(args.static, exist_ok=True)
        
        # Создание примера index.html
        with open(os.path.join(args.static, 'index.html'), 'w', encoding='utf-8') as f:
            f.write("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Главная страница</title>
                <meta charset="utf-8">
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    .container { max-width: 800px; margin: 0 auto; }
                    .header { background: #2196F3; color: white; padding: 20px; }
                    .content { padding: 20px; border: 1px solid #ddd; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Добро пожаловать!</h1>
                    </div>
                    <div class="content">
                        <h2>Это главная страница</h2>
                        <p>Простой веб-сервер успешно работает!</p>
                        <p>Доступные страницы:</p>
                        <ul>
                            <li><a href="/">Корневая страница</a></li>
                            <li><a href="/form">Тестовая форма</a></li>
                            <li><a href="/api/status">Статус API</a></li>
                        </ul>
                    </div>
                </div>
            </body>
            </html>
            """)
        
        # Создание примера CSS
        with open(os.path.join(args.static, 'style.css'), 'w', encoding='utf-8') as f:
            f.write("""
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                border-radius: 10px;
                margin-bottom: 30px;
            }
            
            .button {
                background: #4CAF50;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            """)
    
    # Запуск сервера
    server = HTTPServer(args.host, args.port, args.static)
    server.start()
main()