user_password = input('введите пароль: ')
pass_confirm = input('подтвердите пароль: ')

if user_password != pass_confirm:
    print('пароли не совпали')
    exit()

Authorization = input('Авторизация: введите пароль: ')

if Authorization == user_password:
    print('Access')
else:
    print('Denied')