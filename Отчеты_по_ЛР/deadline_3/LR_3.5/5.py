import sys

def sozdat_spisok(n):
    return [x ** 2 for x in range(n)]

def sozdat_generator(n):
    return (x ** 2 for x in range(n))

n = 1000000
spisok = sozdat_spisok(n)
generator = sozdat_generator(n)
print(f"razmer spiska: {sys.getsizeof(spisok)} bayt")
print(f"razmer generatora: {sys.getsizeof(generator)} bayt")

# сложность по памяти, список — O(n), потому что хранит все элементы, генератор — O(1), потому что не хранит ничего большого