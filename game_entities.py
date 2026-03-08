import random
import character

# This module defines the Player and Enemy classes.
# These classes inherit from the Character class.

class Player(character.Character):

    # Creates the player character with default stats
    def __init__(self, name):

        super().__init__(
            name,
            health=120,
            magic=50,
            attack_power=30,
            defense_power=10,
            speed=20,
            accuracy=80,
            skills=["Heal", "Double Slash"]
        )

        # Stores the player's maximum health so healing cannot exceed it
        self.max_health = 120

    # The heal skill restores between 25% and 35% of the player's health
    def heal(self):

        magic_cost = 10

        if self.magic < magic_cost:

            print("Not enough magic to use Heal.")
            return

        self.magic -= magic_cost

        heal_percent = random.uniform(0.25, 0.35)

        # Uses max_health instead of hardcoded value
        heal_amount = int(self.max_health * heal_percent)

        # Adds the healing but prevents exceeding max health
        self.health = min(self.max_health, self.health + heal_amount)

        print(f"{self.name} uses Heal and restores {heal_amount} HP.")


    # Double Slash skill has character attack twice but it only requires one check for the hit chance
    def double_slash(self, target):

        magic_cost = 15

        if self.magic < magic_cost:

            print("Not enough magic to use Double Slash.")
            return

        self.magic -= magic_cost

        if self.attack_hits(target):

            damage = max(1, self.attack_power - target.defense_power)

            total_damage = damage * 2

            target.take_damage(total_damage)

            print(f"{self.name} uses Double Slash and deals {total_damage} damage.")

        else:

            print(f"{self.name}'s Double Slash missed.")


class Enemy(character.Character):

    # Creates different enemy types with different stats
    def __init__(self, monster_type):

        if monster_type == "wolf":

            super().__init__("Wolf", 90, 20, 22, 6, 30, 75, ["Charge"])

        elif monster_type == "goblin":

            super().__init__("Goblin", 100, 25, 25, 8, 22, 70, ["Charge"])

        elif monster_type == "orc":

            super().__init__("Orc", 130, 30, 32, 12, 15, 65, ["Charge"])

    # Charge skill does 1.5x damage but it has a slightly lower accuracy
    def charge(self, target):

        magic_cost = 10

        if self.magic < magic_cost:

            self.basic_attack(target)
            return

        self.magic -= magic_cost

        lowered_accuracy = self.accuracy * 0.8

        hit_rate = (lowered_accuracy / (lowered_accuracy + target.speed)) * 100

        roll = random.uniform(0, 100)

        if roll <= hit_rate:

            damage = max(1, self.attack_power - target.defense_power)

            charge_damage = int(damage * 1.5)

            target.take_damage(charge_damage)

            print(f"{self.name} uses Charge and deals {charge_damage} damage.")

        else:

            print(f"{self.name}'s Charge missed.")