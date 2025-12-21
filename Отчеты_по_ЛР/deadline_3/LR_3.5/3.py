import time
import random

def find_duplicates(arr):
    dublikaty = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                dublikaty.append(arr[i])
    return dublikaty

arr_5000 = [random.randint(1, 1000) for _ in range(5000)]

nachalo = time.time()
find_duplicates(arr_5000)
vremya_5000 = time.time() - nachalo
print(f"vremya dlya 5000: {vremya_5000}")

arr_10000 = [random.randint(1, 1000) for _ in range(10000)]

nachalo = time.time()
find_duplicates(arr_10000)
vremya_10000 = time.time() - nachalo
print(f"время для 10000: {vremya_10000}")

print(f"если данные выросли в 2 раза, время выросло приблизительно в {vremya_10000 / vremya_5000} раз")