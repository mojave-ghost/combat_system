from attack import attack
from random_attack import random_attack
from heroes import Wombat, Pelican, Starfish
from .leveling import level_up


def battle(hero, name):
    # Select your opponent
    print("1. Wombat")
    print("2. Pelican")
    print("3. Starfish")
    opponent = int(input("Select your opponent [1-3]: "))
    if opponent == 1:
        enemy = Wombat()
    elif opponent == 2:
        enemy = Pelican()
    elif opponent == 3: 
        enemy = Starfish()

    while True:
        attack(hero, enemy, name)
        random_attack(enemy, hero, name)    

        if hero.hit_points <= 0 or enemy.hit_points <= 0:
            if hero.hit_points <= 0:
                print("\n You have been defeated!")
            elif enemy.hit_points <= 0:
                print("\n You have defeated your opponent!")
                print("You have gained _ exp.")
                level_up.level_up(True, 5, 5)
            break
        else:
            continue
