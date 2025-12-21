def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return None
    sredina = len(arr) // 2
    levaya_chast = arr[:sredina]
    pravaya_chast = arr[sredina:]
    maks_levyy = find_max(levaya_chast)
    maks_pravyy = find_max(pravaya_chast)
    return maks_levyy if maks_levyy > maks_pravyy else maks_pravyy

chisla = [3, 7, 1, 9, 4, 2, 55]
print(find_max(chisla))