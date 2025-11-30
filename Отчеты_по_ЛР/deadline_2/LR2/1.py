n = int(input("введите число n: "))
summa = 0

for i in range(1, n + 1):
    summa += i

print(f"сумма чисел от 1 до {n} = {summa}")