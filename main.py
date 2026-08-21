from heroes import Wombat, Pelican, Starfish
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
        attack(hero, enemy)
        random_attack(enemy, hero)    

        if hero.hit_points <= 0 or enemy.hit_points <= 0:
            if hero.hit_points <= 0:
                print("You have been defeated!")
            elif enemy.hit_points <= 0:
                print("You have defeated your opponent!")
            break
        else:
            continue

main()