import random
from game_entities import Player, Enemy

# Main program for the battle game.
# Imports the Player and Enemy classes and runs the battle encounter.

# Creates a random enemy for the encounter
def create_random_enemy():

    monster = random.choice(["wolf", "goblin", "orc"])

    return Enemy(monster)


def main():

    print("=== Simple Battle Game ===")

    player_name = input("Enter your character name: ")

    player = Player(player_name)

    enemy = create_random_enemy()

    print("\nA wild enemy appears!")
    print(enemy)

    # the battle continues until one character is defeated
    while player.is_alive() and enemy.is_alive():

        print("\nChoose an action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Double Slash")

        choice = input("Enter your choice: ")

        if choice == "1":

            player.basic_attack(enemy)

        elif choice == "2":

            player.heal()

        elif choice == "3":

            player.double_slash(enemy)

        else:

            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if enemy.is_alive():

            print("\nEnemy turn:")

            if random.choice([True, False]):

                enemy.charge(player)

            else:

                enemy.basic_attack(player)

    # Final result
    if player.is_alive():

        print("\nYou defeated the enemy!")

    else:

        print("\nYou were defeated.")


if __name__ == "__main__":
    main()