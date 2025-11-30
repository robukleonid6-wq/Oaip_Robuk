text = input('введите текст: ')

bounds = input('введите начальный и конечный индекс через пробел: ')

start, end = map(int, bounds.split())

start_index = start - 1
end_index = end

print('результат', text[start_index:end_index])