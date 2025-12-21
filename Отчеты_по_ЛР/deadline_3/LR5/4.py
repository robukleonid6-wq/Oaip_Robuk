class hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def strike(self, target):
        target.health -= self.attack_power
        print(f"{self.name} ударил {target.name} на {self.attack_power} урона")

knight = hero("артур", 100, 20)
rogue = hero("робин", 80, 15)

knight.strike(rogue)
knight.strike(rogue)
knight.strike(rogue)
rogue.strike(knight)
rogue.strike(knight)

print(f"{knight.name}: {knight.health}")
print(f"{rogue.name}: {rogue.health}")