import random

def random_numbers():
    while True:
        yield random.randint(1, 100)



class Processor:
    def process(self, generator):
        s = 0
        c = 0
        num_list = []

        for num in generator:
            s += num
            c += 1
            num_list.append(num)

            if s > 1000:
                break

        self.numbers_used = num_list
        return c

p = Processor()
gen = random_numbers()
result = p.process(gen)
print(f"понадобилось чисел: {result}")
print(f"числа были: {p.numbers_used}") ## это я чисто сам захотел 😁

