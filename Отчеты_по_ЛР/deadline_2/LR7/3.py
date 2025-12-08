def calc_avg(a: list[float]) -> float:

    # считает среднее
    # Args: a list[float]: числа
    # Returns: float: среднее

    if not a:
        return 0.0
    s = sum(a)
    n = len(a)
    return s / n


def fmt_fio(a: list[str], b: bool = True) -> str:

    # делает фио строкой
    # Args: a list[str]: части
    #b bool: заглавные ли
    # Returns: str: строка

    x = " ".join(a)
    if b:
        return x.title()
    return x


def filter_scores(a: dict[str, int], b: int) -> dict[str, int]:

    # фильтрует значения
    # Args: a dict[str, int]: данные
    #b int: минимум
    # Returns: dict[str, int]: новое

    r = {}
    for k, v in a.items():
        if v >= b:
            r[k] = v
    return r


print(calc_avg([10, 20, 30, 40]))
print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], b=False))

x = {"math": 95, "history": 78, "english": 88, "art": 92}
print(filter_scores(x, 90))

