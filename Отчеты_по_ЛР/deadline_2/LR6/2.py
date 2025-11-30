text = input("введите произвольный текст: ")
stroki = input("введите две строки через пробел: ")

strings = stroki.split()

if len(strings) == 2:
    string1, string2 = strings
    new_text = text.replace(string1, string2)
    print(f"новый текст: {new_text}")
else:
    print("нужно ввести ровно две строки через пробел")