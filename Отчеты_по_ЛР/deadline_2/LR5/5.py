text = input('введите произвольный текст: ')
poisk = input('введите слово для поиска: ')

count = text.count(poisk)
index = text.find(poisk)

print(f'колличество встречный слов: {count}')
print(f'индекс первого вхождения: {index + 1}')

text_new = text.replace(poisk, "")
print(f'строка без введенного слова: {text_new}')