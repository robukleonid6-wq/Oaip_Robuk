count = int(input("сколько чисел нужно? "))

numbers = []

for i in range(count):
    num = float(input(f"введите число {i + 1}: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / count

above_average = 0
for num in numbers:
    if num > average:
        above_average += 1

print("Результаты:")
print(f"Максимальное: {maximum}")
print(f"Минимальное: {minimum}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {above_average}")