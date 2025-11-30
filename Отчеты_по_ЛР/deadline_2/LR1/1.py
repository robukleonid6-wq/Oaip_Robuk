number = int(input("введите положительное целое число: "))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10

print(f"итог: {total}")