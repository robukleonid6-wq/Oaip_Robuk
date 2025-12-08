def da(a: list[int], b: list[int]) -> list[int]:

    # находит общие элементы двух списков без повторений
    # Args: a list[int]: первый список
    #b list[int]: второй список

    # Returns: list[int]: список общих элементов
    s1 = set(a)
    s2 = set(b)
    r = s1 & s2
    return list(r)


list1 = [1, 2, 4, 7, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]

itog = da(list1, list2)
print(itog)

