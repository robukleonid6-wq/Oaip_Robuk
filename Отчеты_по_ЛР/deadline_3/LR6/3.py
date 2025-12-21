class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, number):
        return number * self.factor

by_5 = Multiplier(50)
print(by_5(10)) 
print(by_5(2))  