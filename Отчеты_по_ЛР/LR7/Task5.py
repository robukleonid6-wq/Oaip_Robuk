import math

parts = input("введите выражение (число знак число): ").split()
a, op, b = float(parts[0]), parts[1], float(parts[2])

if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
elif op == '%': print(a % b)
elif op == '//': print(a // b)
elif op == '**': print(a ** b)
elif op == '%%': print(a * b / 100)
elif op == '/**': print(a ** (1/b))
else: print("неизвестный знак")