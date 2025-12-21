import time

spisok = list(range(100000))

nachalo = time.time()
for _ in range(1000):
    spisok.pop(0)
konec = time.time()
print(f"время для pop(0): {konec - nachalo} секунд")

spisok = list(range(100000))

nachalo = time.time()
for _ in range(1000):
    spisok.pop()
konec = time.time()
print(f"время для pop(): {konec - nachalo} сек")

# вывод: pop() намного быстрее, потому что сложность o(1), а pop(0) o(n) из-за сдвига всех элементов