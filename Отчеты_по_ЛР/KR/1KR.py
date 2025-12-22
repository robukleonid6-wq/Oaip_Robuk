cvet = input("введи цвет на английском: ")

cvet = cvet.lower()

match cvet:
    case "red":
        print("красный")
    case "blue":
        print("синий")
    case "green":
        print("зеленый")
    case "yellow":
        print("желтый")
    case "black":
        print("черный")
    case "white":
        print("белый")
    case "gray-brown-crimson":
        print('серо-буро-малиновый')
    case _:
        print("неизвестный цвет")