class animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("животное издает звук")

class dog(animal):
    def make_sound(self):
        print("гав!")

class cat(animal):
    def make_sound(self):
        print("мяу!")

def animal_chorus(animals):
    for animal in animals:
        animal.make_sound()

animals = [dog("печкин"), cat("матроскин")]
animal_chorus(animals)