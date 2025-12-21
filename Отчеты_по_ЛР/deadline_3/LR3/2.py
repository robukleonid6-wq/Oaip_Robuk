def summa_tsifr(number):
    if number == 0:
        return 0
    return number % 10 + summa_tsifr(number // 10)

print(summa_tsifr(1234523243432432))