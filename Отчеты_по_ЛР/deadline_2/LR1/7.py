symbol = input("введите символ: ")
height = int(input("введите высоту: "))
width = int(input("введите ширину: "))

i = 0
while i < height:
    if i == 0 or i == height - 1:
        j = 0
        while j < width:
            print(symbol, end="")
            j = j + 1
        print()
    else:
        j = 0
        while j < width:
            if j == 0 or j == width - 1:
                print(symbol, end="")
            else:
                print(" ", end="")
            j = j + 1
        print()
    i = i + 1