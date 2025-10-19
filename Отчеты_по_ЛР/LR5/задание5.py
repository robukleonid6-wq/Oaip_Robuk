import random
import string

def generate_random_string(length: int) -> str:
    """Генерирует случайную строку из букв ASCII и цифр."""
    # Определяем набор символов, из которых будет состоять строка
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    # Генерируем строку
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

message = input("Введите сообщение: ")
n = int(input("Введите число n: "))

finalMessage = "";
for sortThrough in message:
    finalMessage += sortThrough + generate_random_string(n)

print("конечное сообщение:", finalMessage)