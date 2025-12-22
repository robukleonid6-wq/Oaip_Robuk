def find_places(zal, n):
    for i, r in enumerate(zal):
        c = 0
        s = 0
        for j, m in enumerate(r):
            if m == 0:
                if c == 0:
                    s = j
                c += 1
                if c == n:
                    return f"ряд {i+1}, места с {s+1} пo {s+n}"
            else:
                c = 0
    return "вместе не сядете"

z = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1]
]

k = int(input("сколько нужно мест? "))
result = find_places(z, k)
print(result)