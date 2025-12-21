def flat_gen(nested_list):
    for podspisok in nested_list:
        yield from podspisok

matritsa = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 1],
    [6, 7, 8, 1]
]
for num in flat_gen(matritsa):
    print(num, end=" ")