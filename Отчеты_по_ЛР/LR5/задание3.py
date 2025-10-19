fio = input("введите фио через пробел: ")
data = fio.split()

if len(data) == 3:
    print("Фамилия:", data[0].upper());
    print("Имя:", data[1].upper());
    print("Отчество:", data[2].upper());
else:
    print("нужно ввести полностью ФИО")