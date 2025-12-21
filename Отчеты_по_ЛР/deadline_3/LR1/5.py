def safe_exec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("ошибка: деление на ноль")
            return 0
    return wrapper

@safe_exec
def divide(a, b):
    return a / b

print(f"Результат 1: {divide(10, 0)}")
print(f"Результат 2: {divide(5, 0)}")