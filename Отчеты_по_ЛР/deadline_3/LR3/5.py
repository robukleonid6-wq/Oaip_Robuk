import time

def fibonachchi(n):
    if n <= 1:
        return n
    return fibonachchi(n - 1) + fibonachchi(n - 2)

def tail_fibonacci(n, accumulator1=0, accumulator2=1):
    if n == 0:
        return accumulator1
    if n == 1:
        return accumulator2
    return tail_fibonacci(n - 1, accumulator2, accumulator1 + accumulator2)

n = 30

start_time = time.time()
print(f"Fibonacci({n}) = {fibonachchi(n)}")
print(f"Time taken (Naive): {time.time() - start_time:.6f} seconds")

start_time = time.time()
print(f"Tail Fibonacci({n}) = {tail_fibonacci(n)}")
print(f"Time taken (Tail): {time.time() - start_time:.6f} seconds")