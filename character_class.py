# Charachter Class to go along with SuperHero Exercises

class Charachter():
    def __init__(self, name, strength=15, power=10, health=50):
        self.name = name
        self.strength = strength
        self.health = health
        self.power = power

    def is_alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print(f'{self.name}, you have {self.health} health and {self.power} power.')

    def attack(self, char_name):
        char_name.health -= self.power
        print(f'{self.name} inflicts {self.power} damage on you!')
        if char_name.health <= 0:
            char_name.dont_die()
            # print(f'{char_name.name}, you are dead!')

    def dont_die(self):
        if self.health <= 0:
            self.health = 50