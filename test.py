# '''Documentation (Copied Profesors Code:) (Do Not Mind This)'''

# class Status:
#     def __init__(self, name: str, health: int, damage: int, speed: int):
#         self.name = name
#         self.health = health
#         self.damage = damage
#         self.speed = speed

# class Enemy(Status):
#     def __init__(self, player, name, health, damage, speed):
#         super().__init__(name, health, damage, speed)
#         self.player = player
    
#     def attack(self):
#         self.player.get_damage(self.damage)

# class Player(Status):
#     def __init__(self, name, health, damage, speed):
#         super().__init__(name, health, damage, speed)

#     def get_damage(self, amount):
#         self.health -= amount

# player1 = Player(name = 'Adin', damage = 5, health = 100, speed = 10)
# goblin = Enemy(player = player1,name ='goblin', damage = 2, health = 50, speed = 10)

# while True:

#     goblin.attack()
#     print(player1.health)

#     user_input = input()
#     if user_input.lower() == 'quit':
#         break
