numbers = input("введите три целых числа через пробел: ")
a, b, c = numbers.split()

a = int(a)
b = int(b)
c = int(c)

# № 2
result1 = a * b
result2 = b * c
result3 = c * a

# № 4
if c == 0:
    print('деление на 0 невозможно')
    exit()

if a == 0:
    print('деление на 0 невозможно')
    exit()
step4_1 = a ** 4
step4_2 = b % c
step4_3 = c // a

# № 6
print("результаты № 2:");
print(f"{a} * {b} = {result1}");
print(f"{b} * {c} = {result2}");
print(f"{c} * {a} = {result3}");

print("результаты № 4:")
print(f"{a} ^4 = {step4_1}")
print(f"остаток от деления {b} на {c} = {step4_2}")
print(f"целочисленное деление {c} на {a} = {step4_3}")

print(f"сумма переменных: {step4_1 + step4_2 + step4_3}")