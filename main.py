import heroes
from random_attack import random_attack
from attack import attack

# Select your hero
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

def main():
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

main()