def binarnyy_poisk(arr, target):
    def poisk_vnutri(niz, verh):
        if niz > verh:
            return -1
        sredina = (niz + verh) // 2
        if arr[sredina] == target:
            return sredina
        elif arr[sredina] > target:
            return poisk_vnutri(niz, sredina - 1)
        else:
            return poisk_vnutri(sredina + 1, verh)
    return poisk_vnutri(0, len(arr) - 1)

moy_arr = [10, 20, 30, 40, 50, 60, 70]
print(binarnyy_poisk(moy_arr, 70))
print(binarnyy_poisk(moy_arr, 99))