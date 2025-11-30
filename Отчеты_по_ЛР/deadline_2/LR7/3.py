text = input("введите произвольный текст: ")
step = int(input("введите шаг: "))

print(f"текст с шагом {step}: {text[::step]}")