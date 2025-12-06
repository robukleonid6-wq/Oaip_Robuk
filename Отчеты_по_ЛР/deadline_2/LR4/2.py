lis = [1, 5, 51, 3, 10, 6, 66, 9, 1, 99]

lis_num = [
    num for num in lis if num % 2 == 0
]

lis_50 = [
    num for num in lis if num > 50
]

print(f'изначальный список чисел: {lis}')
print(f'четные числа: {lis_num}')
print(f'числа больше 50: {lis_50}')