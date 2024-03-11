class Weapons:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

sword = Weapons(name = 'Sword', weapon_type = 'meele', damage = 10, value = 15)

bow = Weapons(name = 'Bow', weapon_type = 'range', damage = 7, value = 12)

knuckle = Weapons(name = 'club', weapon_type = 'blunt', damage = 6, value = 11)

none = Weapons(name = 'None', weapon_type = 'blunt', damage = 1, value = 0)