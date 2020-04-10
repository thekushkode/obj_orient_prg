"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print(f'{self.name} attacks {enemy.name}.')
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print(f'{self.name} received {points} damage.')
        if not self.is_alive():
            print(f'h no! {self.name} is dead.')

    def print_status(self):
        print(f'{self.name} has {self.health} health and {self.power} power.')

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 5, 5, 15)

    def recoop(self):
        if self.health < 5:
            if random.random() <= 0.2:
                self.health += 2

class Zombie(Character):
    def __init__(self, name):
        super().__init__(name, 10, 10, 3)

    def dont_die(self):
        if self.health <= 0:
            self.health = 50

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name, 1, 20, 0)

    def resilient(self, enemy):
        if random.random() <= 0.10:
            self.health -= enemy.power

class Coward(Character):
    def __init__(self, name):
        super().__init__(name, 10, 0, 10000)

    def run_away(self):
        give_coins = random.random() <= 1
        if give_coins:
            self.coins, enemy.coins = enemy.coins, self.coins

class Normal(Character):
    def __init__(self, name):
        super().__init__(name, 15, 1, 50)

    def police(self, enemy):
        print(f'Somebody call the police! {enemy.name} is attacking me!')




class Hero(Character):
    def __init__(self, name, armor=5, evade=2):
        super().__init__(name,)
        self.armor = armor
        self.evade = evade
            

    def restore(self):
        self.health = 10
        print(f"Hero's heath is restored to {self.health}!")
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def hero_attack(self, enemy):
        if not self.is_alive():
            return
        print(f'{self.name} attacks {enemy.name}.')
        enemy.receive_damage(self.power)
        if random.random() <= 0.2:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

    def hero_receive_damage(self, points):
        while self.evade <= 2:
            if random.random() <= 0.10:
                self.health -= 0
                print(f'You juked your opponent and received 0 damage!')
        while self.evade > 2 and self.evade <= 4:
            if random.random() <= 0.15:
                self.health -= 0
                (f'You juked your opponent and received 0 damage!')
        points -= hero.armor
        self.health -= points
        print(f'{self.name} received {points} damage.')
        if not self.is_alive():
            print(f'Oh no! {self.name} is dead.')

class Goblin(Character):
    def __init__(self, name, bounty=25):
        super().__init__(name, 6, 2, 0)
        self.bounty = bounty

class Wizard(Character):
    def __init__(self, name, bounty=50):
        super().__init__(name, 8, 1, 0)
        self.bounty = bounty

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print(f'{self.name} swaps power with {enemy.name} during attack.')
            self.power, enemy.power = enemy.power, self.power
        super().attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print(f'{hero.name} faces the {enemy.name}.')
        print("=====================")
        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print(f'1. fight {enemy.name}!')
            print("2. do nothing..")
            print("3. flee. lol")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.hero_attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print(f'Invalid input {user_input}')
                continue
            enemy.attack(hero)
        if hero.is_alive():
            hero.coins += enemy.bounty
            print(f'You defeated the {enemy.name}')
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class SuperTonic:
    cost = 10
    name = 'super tonic'
    def apply(self, hero):
        hero.health += 10
        print(f"{hero.name}'s health increased to {hero.health}.")

class Sword:
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print(f"{hero.name}'s power increased to {hero.power}.")

class Armor:
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print(f'{hero.name} armor has increased to {hero.armor}!')

class Evade:
    cost = 10
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        print(f'{hero.name} evade points has increased to {hero.evade}!')


class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print(f'You have {hero.coins} coins.')
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print(f'{i + 1}. buy {item.name} {item.cost}')
            print("10. leave")
            if item.cost > hero.coins:
                print('You dont have enough coins! Go kill another bad guy.')
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

norm = Normal('Norm')
coward = Coward('Carl')
zombie = Zombie('Zombie')
medic = Medic('Medic')
hero = Hero('LeBron', 0, 2)
enemies = [Goblin('Goblin'), Wizard('Merlin'), Zombie('Zombie'), Medic('Medic'), Coward('Carl'), Normal('Norm')]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
