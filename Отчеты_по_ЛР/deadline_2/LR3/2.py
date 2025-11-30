text = input("введите произвольную строку: ")

char_count = {}
for char in text.lower():
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("результат подсчета символов:")
print(char_count)