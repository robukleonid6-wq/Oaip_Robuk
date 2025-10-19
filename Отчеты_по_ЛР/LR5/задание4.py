numbers = input('введите пять чисел')
aloneNumbers = numbers.split()

num1 = int(aloneNumbers[0])
num2 = int(aloneNumbers[1])
num3 = int(aloneNumbers[2])
num4 = int(aloneNumbers[3])
num5 = int(aloneNumbers[4])

numberMin = min(num1, num2, num3, num4, num5)
numberMax = max(num1, num2, num3, num4, num5)

print("Min", numberMin)
print("Max", numberMax)