from entities import Player, Enemy
from weapons import sword, bow, knuckle

player = Player(name = 'Ross', health = 100, strength = 5)
goblin = Enemy(name = 'goblin', health = 100, strength = 2, weapon = sword)

print('Type "Quit", if ever you want to exit: \n')

player.equip(sword)
# debugging
while True:

    player.attack(goblin)
    goblin.attack(player)

    print(f"health of {player.name}: {player.health}")
    print(f"health of {goblin.name}: {goblin.health}")

    user_input = input('\nTerminal: ')
    if user_input.lower() == 'quit':
        break




