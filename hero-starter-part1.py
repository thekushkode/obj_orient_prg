"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from character_class import Charachter

class Hero(Charachter):
    pass

class Goblin(Charachter):
    pass

class Zombie(Charachter):
    pass

    
zombie = Zombie('Zombie')
hulk = Hero('Hulk')
goblin = Goblin('Goblin')


def main():
    hulk.health = 50
    hulk.power = 15
    zombie.health = 50
    zombie.power = 10

    while zombie.is_alive() and hulk.is_alive():
        hulk.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hulk.attack(zombie)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print(f'Invalid input: {user_input}.')

        if zombie.health > 0:
            zombie.attack(hulk)

main()
