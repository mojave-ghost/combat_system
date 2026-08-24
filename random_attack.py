import random
from heroes import Wombat, Pelican, Starfish

def random_attack(opponent, hero, name):
    move = random.randint(1,4)
    if isinstance(opponent, Wombat):
        if move == 1:
            hero.hit_points -= opponent.tackle
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.tackle} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 2:
            hero.hit_points -= opponent.headbutt
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.headbutt} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 3:
            hero.hit_points -= opponent.double_edge
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.double_edge} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 4:
            hero.hit_points -= opponent.quick_attack
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.quick_attack} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
    elif isinstance(opponent, Pelican):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.hurricane} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 2:
            hero.hit_points -= opponent.scald
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.scald} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.wide_guard} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 4:
            hero.hit_points -= opponent.protect
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.protect} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
    elif isinstance(opponent, Starfish):
        if move == 1:
            hero.hit_points -= opponent.surf
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.surf} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 2:
            hero.hit_points -= opponent.psychic
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.psychic} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 3:
            hero.hit_points -= opponent.thunderbolt
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.thunderbolt} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
        elif move == 4:
            hero.hit_points -= opponent.ice_beam
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{name} has taken {opponent.ice_beam} damage. {name}'s hit points are now {hero.hit_points}.")
            print("---------------------------------------------------------------------------------------------------------")
    