def deep_flatten(lst):
    rezultat = []
    def vnut_rekursiya(element):
        if isinstance(element, list):
            for pod_element in element:
                vnut_rekursiya(pod_element)
        else:
            rezultat.append(element)
    vnut_rekursiya(lst)
    return rezultat

slozhnyy_lst = [1, [2, [3, 4], 5], 6, [[7], 8], [6]]
print(deep_flatten(slozhnyy_lst))