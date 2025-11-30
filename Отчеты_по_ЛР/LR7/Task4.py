year = int(input('введи год: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('этот год високосный')
else:
    print('этот год не високосный')