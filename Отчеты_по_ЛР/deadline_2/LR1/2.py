count = 0
while True:
    number = int(input("введите число: "))
    
    if number == 0:
        break
    count += 1

print(f"количество введенных чисел до первого нуля: {count}")