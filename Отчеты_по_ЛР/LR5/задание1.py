num1 = float(input("введите первое число: "))
num2 = float(input("введите второе число: "))
print(f"сложение: {num1 + num2}")
print(f"вычитание: {num1 - num2}")
print(f"умножение: {num1 * num2}")

if num2 != 0:
    print(f"деление: {num1 / num2}")
else:
    print("делить на 0 нельзя")