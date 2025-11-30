text = input('введите произвольный текст: ')
poisk = input('введите слово для поиска: ')

count = text.count(poisk)
index = text.find(poisk)

if count <= 0:
    print('таких слов нет')
else:
    print('такое слово есть')
    print(f'колличество таких слов: {count}')
