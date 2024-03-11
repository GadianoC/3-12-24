from weapons import none

# Stat system
class Status:
    def __init__(self, name: str, health: int, strength: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.strength = strength
        self.weapon = none

    def attack(self, target):
        self.total_damage = (self.strength + self.weapon.damage)
        target.health -= self.total_damage
        target.health = max(target.health, 0)
        print(f'{self.name} dealt {self.total_damage} to {target.name} with {self.weapon.name}')
        
# Player Class
class Player(Status):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
        self.default_weapon = self.weapon

    def equip(self, weapon):
        self.weapon = weapon
        print(f'{self.name} equipped {weapon.name}!')

    def drop(self):
        self.weapon = self.default_weapon
        print(f'{self.name} dropped {weapon.name}')

# Enemy Class
class Enemy(Status):
    def __init__(self, weapon, name, health, strength):
        super().__init__(name, health, strength)
        self.weapon = weapon