symbol = input("введите символ: ")
height = int(input("введите высоту: "))
width = int(input("введите ширину: "))

i = 0
while i < height:
    j = 0
    row = ""
    while j < width:
        row = row + symbol
        j = j + 1
    print(row)
    i = i + 1