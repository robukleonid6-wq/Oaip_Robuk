def my_range(start, end, shag):
    tekushchee = start
    while tekushchee < end:
        yield tekushchee
        tekushchee += shag

for i in my_range(1, 50, 0.5):
    print(i)