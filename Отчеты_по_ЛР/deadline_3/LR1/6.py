def repeat(n):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return actual_decorator

@repeat(3)
def greet(name):
    print(f"привет, {name}!")

greet("заур")