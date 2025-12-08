def sum_numbers(*nums: float) -> float:

#     складывает произвольное количество чисел
#     nums (float): значения для сложения
#     float: сумма всех значений

    s = 0
    for n in nums:
        s += n
    return s

print(sum_numbers(1, 2, 3, 4, 5))
