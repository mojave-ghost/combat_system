from attack import attack
from random_attack import random_attack
from heroes import Wombat, Pelican, Starfish

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
