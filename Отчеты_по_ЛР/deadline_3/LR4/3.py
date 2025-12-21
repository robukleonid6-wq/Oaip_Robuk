class character:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} идет"

class archer(character):
    def shoot(self):
        return f"{self.name} стреляет из лука"

class knight(character):
    def attack_sword(self):
        return f"{self.name} бьет мечом"

luchnik = archer("леголас")
rycar = knight("артур")
print(luchnik.move())
print(luchnik.shoot())
print(rycar.move())
print(rycar.attack_sword())