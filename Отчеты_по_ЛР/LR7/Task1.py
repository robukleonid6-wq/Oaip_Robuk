direction = input('введите направление хода(left, right , straight, back): ')

if direction == 'left':
    print('Иду влево')
elif direction == 'right':
    print('Иду вправо')
elif direction == 'straight':
    print('Иду прямо')
elif direction == 'back':
    print('Иду назад')
else:
    print('Неправильное направление')