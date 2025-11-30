fruits = {
    'яблоки': 5,
    'бананы': 3,
    'апельсины': 10,
    'арбузы': 33
}

print("начальное количество фруктов: ")
for fruit, count in fruits.items():
    print(f"За прилавком есть {count} {fruit}")

fruits['яблоки'] -= 2

fruits['арбузы'] = 0

print("итоговое количество фруктов: ")
for fruit, count in fruits.items():
    print(f"за прилавком осталось {count} {fruit}")