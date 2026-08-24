from heroes import Wombat, Pelican, Starfish
from random_attack import random_attack
from attack import attack
import save


# Select your hero
def select_hero():
    print("1. Wombat")
    print("2. Pelican")
    print("3. Starfish")
    player = int(input("Select your hero [1-3]: "))
    if player == 1:
        hero = Wombat()
    elif player == 2:
        hero = Pelican()
    elif player == 3: 
        hero = Starfish()
    print()

    # Name your hero option 
    is_named = input("Do you want to name your hero? [y/n]")
    if is_named == "y" or is_named == "Y":
        name = input("Name your hero: ")
    elif is_named.lower() == "n":
        name = "Your hero"

    # Open a file in write mode ('w') and save the data
    with open("save.py", "w") as file:
        file.write(f'name="{name}"\n')

    return hero, name

def select_opponent():
    # Select your opponent
    print("1. Wombat")
    print("2. Pelican")
    print("3. Starfish")
    opponent = int(input("Select your opponent [1-3]: "))
    if opponent == 1:
        return Wombat()
    elif opponent == 2:
        return Pelican()
    elif opponent == 3: 
        return Starfish()

def battle(hero, enemy, name):
    while True:
        attack(hero, enemy, name)
        random_attack(enemy, hero, name)    

        if hero.hit_points <= 0 or enemy.hit_points <= 0:
            if hero.hit_points <= 0:
                print("\n You have been defeated!")
            elif enemy.hit_points <= 0:
                print("\n You have defeated your opponent!")
            break
        else:
            continue

def main():
    # Start the game
    print("****************************************")
    print("POKEMAN: A HEART SO TRUUUUE")
    print("****************************************")
    print()
    print("Main Menu")
    print("[1] New Game")
    print("[2] Load Game")
    game_state = int(input("Start a new game or load saved file? [1-2]: "))

    if game_state == 1:
        hero, name = select_hero()
        enemy = select_opponent()
        battle(hero, enemy, name) 
    elif game_state == 2:
        name = hero.name
        class_type = hero.class_type
        print(name)
        print(class_type)

main()
