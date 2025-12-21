def zadacha_1(spisok):
    for i in spisok:
        if i == 100:
            return True
    return False

def zadacha_2(spisok):
    return spisok[0] + spisok[-1]
# сложность: o(1) - доступ по индексу всегда константное время, не зависит от размера списка

def zadacha_3(spisok):
    schetchik = 0
    for i in spisok:
        for j in spisok:
            if i == j:
                schetchik += 1
    return schetchik
# сложность: o(n^2) - внутри двойной цикл, каждый проходит по n элементам, итого n*n операций