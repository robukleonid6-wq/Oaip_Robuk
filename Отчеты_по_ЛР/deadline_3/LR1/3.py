def logger(func):
    def wrapper(*args, **kwargs):
        print(f"вызов функции {func.__name__} с аргументами: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"результат: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a / b

add(5, 10)
add(1, 10)
add(4, 10)
add(77, 10)
