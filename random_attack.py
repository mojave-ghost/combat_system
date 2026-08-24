import random
from heroes import Wombat, Pelican, Starfish

def random_attack(opponent, hero, name):
    move = random.randint(1,4)
    if move == 1:
        hero.hit_points -= opponent.moves[0]['damage']
        print("---------------------------------------------------------------------------------------------------------")
        print(f"{name} has taken {opponent.moves[0]['damage']} {opponent.moves[0]['name']} damage. {name}'s hit points are now {hero.hit_points}.")
        print("---------------------------------------------------------------------------------------------------------")
    elif move == 2:
        hero.hit_points -= opponent.moves[1]['damage']
        print("---------------------------------------------------------------------------------------------------------")
        print(f"{name} has taken {opponent.moves[1]['damage']} {opponent.moves[1]['name']} damage. {name}'s hit points are now {hero.hit_points}.")
        print("---------------------------------------------------------------------------------------------------------")
    elif move == 3:
        hero.hit_points -= opponent.moves[2]['damage']
        print("---------------------------------------------------------------------------------------------------------")
        print(f"{name} has taken {opponent.moves[2]['damage']} {opponent.moves[2]['name']} damage. {name}'s hit points are now {hero.hit_points}.")
        print("---------------------------------------------------------------------------------------------------------")
    elif move == 4:
        hero.hit_points -= opponent.moves[3]['damage']
        print("---------------------------------------------------------------------------------------------------------")
        print(f"{name} has taken {opponent.moves[3]['damage']} {opponent.moves[3]['name']} damage. {name}'s hit points are now {hero.hit_points}.")
        print("---------------------------------------------------------------------------------------------------------")
    