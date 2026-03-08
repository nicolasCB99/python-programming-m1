import random

# This module defines the base Character class.
# Both Player and Enemy will inherit from this class.

class Character:

    # Constructor that sets up the basic attributes for any of the characters
    def __init__(self, name, health, magic, attack_power, defense_power, speed, accuracy, skills):

        self.name = name
        self.health = health
        self.magic = magic
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.speed = speed
        self.accuracy = accuracy
        self.skills = skills

    # Checks if the character is still alive
    def is_alive(self):
        return self.health > 0

    # Calculates the hit chance using a simple formula
    def calculate_hit_rate(self, target):

        return (self.accuracy / (self.accuracy + target.speed)) * 100

    # Determines whether an attack lands successfully
    def attack_hits(self, target):

        hit_rate = self.calculate_hit_rate(target)
        roll = random.uniform(0, 100)

        return roll <= hit_rate

    # Performs a basic attack against another character in battle
    def basic_attack(self, target):

        if self.attack_hits(target):

            damage = max(1, self.attack_power - target.defense_power)

            target.take_damage(damage)

            print(f"{self.name} attacks {target.name} and deals {damage} damage.")

        else:
            print(f"{self.name} attacks {target.name}, but misses.")

    # Reduces health when damage is taken
    def take_damage(self, damage):

        self.health = max(0, self.health - damage)

    # Special method used when printing character information
    def __str__(self):

        return f"{self.name} | HP: {self.health} | MP: {self.magic}"