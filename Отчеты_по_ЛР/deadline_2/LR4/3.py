spisok_zadach = []

flag_programmy = True
while flag_programmy == True:
    
    print("1 - посмотреть задачи")
    print("2 - добавить задачу")
    print("3 - удалить задачу")
    print("4 - выход")
    
    vybor_polzovatelya = input("введите цифру: ")
    
    if vybor_polzovatelya == "1":
        print("вот все задачи:")
        if len(spisok_zadach) == 0:
            print("пока ничего нет")
        else:
            schotchik = 0
            while schotchik < len(spisok_zadach):
                nomer_dlya_pokaza = schotchik + 1
                print(str(nomer_dlya_pokaza) + ". " + spisok_zadach[schotchik])
                schotchik = schotchik + 1
    
    elif vybor_polzovatelya == "2":
        novaya_zadacha = input("напишите задачу: ")
        spisok_zadach.append(novaya_zadacha)
        print("добавили задачу!")

    elif vybor_polzovatelya == "3":
        if len(spisok_zadach) == 0:
            print("нечего удалять")
        else:
            print("вот все задачи:")
            i = 0
            while i < len(spisok_zadach):
                nomer = i + 1
                print(str(nomer) + ". " + spisok_zadach[i])
                i = i + 1

            nomer_dlya_udaleniya = input("какую задачу удалить? введите номер: ")
            try:
                nomer_kak_chislo = int(nomer_dlya_udaleniya)

                if nomer_kak_chislo >= 1 and nomer_kak_chislo <= len(spisok_zadach):

                    zadacha_kotoraya_udalitsya = spisok_zadach[nomer_kak_chislo - 1]

                    spisok_zadach.pop(nomer_kak_chislo - 1)
                    print("удалили задачу: " + zadacha_kotoraya_udalitsya)
                else:
                    print("неправильный номер")
            except:
                print("надо вводить цифру!")
    
    elif vybor_polzovatelya == "4":
        print("выходим из программы...")
        flag_programmy = False
    
    else:
        print("не понял, выберите 1, 2, 3 или 4")
    print("")