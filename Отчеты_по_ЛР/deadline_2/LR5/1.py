from math import sqrt

tochka_a = (3, 7)
tochka_b = (10, 2)

x1, y1 = tochka_a
x2, y2 = tochka_b

rasstoyanie = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"точка A: {tochka_a}")
print(f"рочка B: {tochka_b}")
print(f"расстояние между точками: {rasstoyanie}")