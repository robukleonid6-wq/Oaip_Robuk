def squares_gen(chislo):
    for i in range(1, chislo + 1):
        yield i ** 2

gen = squares_gen(7)
for val in gen:
    print(val)