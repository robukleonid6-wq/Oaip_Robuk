print("введите текст: ")

stroki_teksta = []
while True:
    vvod_stroki = input()
    if vvod_stroki == "":
        break
    stroki_teksta.append(vvod_stroki)

celiy_tekst = " ".join(stroki_teksta)

znaki_prepinaniya = [",", ".", "!", "?", ";", ":", "-", "—", "(", ")", "[", "]", "{", "}", "\"", "`"]
chistiy_tekst = celiy_tekst
for znak in znaki_prepinaniya:
    chistiy_tekst = chistiy_tekst.replace(znak, " ")

slova = chistiy_tekst.split()

slova_v_nizhnem_registre = []
for slovo in slova:
    slova_v_nizhnem_registre.append(slovo.lower())

if len(slova_v_nizhnem_registre) == 0:
    print("Нет слов для анализа!")
else:
    samoie_dlinoe_slovo = slova_v_nizhnem_registre[0]
    samoie_korotkoe_slovo = slova_v_nizhnem_registre[0]
    
    for slovo in slova_v_nizhnem_registre:
        if len(slovo) > len(samoie_dlinoe_slovo):
            samoie_dlinoe_slovo = slovo
        if len(slovo) < len(samoie_korotkoe_slovo):
            samoie_korotkoe_slovo = slovo
    
    summa_dlin = 0
    for slovo in slova_v_nizhnem_registre:
        summa_dlin = summa_dlin + len(slovo)
    sredniaia_dlina = summa_dlin / len(slova_v_nizhnem_registre)
    
    slovar_chastoti = {}
    for slovo in slova_v_nizhnem_registre:
        if slovo in slovar_chastoti:
            slovar_chastoti[slovo] = slovar_chastoti[slovo] + 1
        else:
            slovar_chastoti[slovo] = 1
    
    spisok_chastoti = []
    for slovo, kolichestvo in slovar_chastoti.items():
        spisok_chastoti.append((slovo, kolichestvo))
    
    for i in range(len(spisok_chastoti)):
        for j in range(len(spisok_chastoti) - 1 - i):
            if spisok_chastoti[j][1] < spisok_chastoti[j + 1][1]:
                temp = spisok_chastoti[j]
                spisok_chastoti[j] = spisok_chastoti[j + 1]
                spisok_chastoti[j + 1] = temp
    
    top_5_slov = []
    kolvo_slov_dlya_pokaza = 5
    if len(spisok_chastoti) < kolvo_slov_dlya_pokaza:
        kolvo_slov_dlya_pokaza = len(spisok_chastoti)
    
    for i in range(kolvo_slov_dlya_pokaza):
        top_5_slov.append(spisok_chastoti[i])
    
    print("cамое длинное слово:", samoie_dlinoe_slovo)
    print("cамое короткое слово:", samoie_korotkoe_slovo)
    print("cредняя длина слова:", sredniaia_dlina)
    print("топ-5 слов:", top_5_slov)