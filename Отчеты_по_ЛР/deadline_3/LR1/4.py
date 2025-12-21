import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"время выполнения функции {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@timer
def slow_func():
    for _ in range(1000000): 
        pass 

slow_func()