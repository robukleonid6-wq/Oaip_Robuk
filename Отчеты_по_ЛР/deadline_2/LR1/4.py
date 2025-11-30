from random import randint

number = randint(1, 100)
count = 0

print("угадай число от 1 до 100")

while True:
    answer = int(input("введи число: "))
    count = count + 1
    
    if answer < number:
        print("больше")
    elif answer > number:
        print("меньше")
    else:
        print(f"да это {number}")
        print(f"угадал с {count} попытки")
        break