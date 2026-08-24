# Select your move
from heroes import Wombat, Pelican, Starfish

def attack(hero, opponent, name):
    if isinstance(hero, Wombat):
        print("MOVE LIST")
        print("1. Tackle")
        print("2. Headbutt")
        print("3. Double-Edge")
        print("4. Quick Attack")
        move = int(input("Select your battle move [1-4]: "))
        print("\n")

        if move == 1:
            opponent.hit_points -= hero.tackle
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.tackle} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 2:
            opponent.hit_points -= hero.headbutt
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.headbutt} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 3:
            opponent.hit_points -= hero.double_edge
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.double_edge} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 4:
            opponent.hit_points -= hero.quick_attack
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.quick_attack} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
    elif isinstance(hero, Pelican):
        print("1. Hurricane")
        print("2. Scald")
        print("3. Wide Guard")
        print("4. Protect")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.hurricane
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.hurricane} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 2:
            opponent.hit_points -= hero.scald
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.scald} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 3:
            opponent.hit_points -= hero.wide_guard
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.wide_guard} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 4:
            opponent.hit_points -= hero.protect
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.protect} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
    elif isinstance(hero, Starfish):
        print("1. Surf")
        print("2. Psychic")
        print("3. Thunderbolt")
        print("4. Ice Beam")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.surf
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.surf} damage. Your target's hit points are now {opponent.hit_points}." )
            print("********************************************************************************************************* \n")
        elif move == 2:
            opponent.hit_points -= hero.psychic
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.psychic} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 3:
            opponent.hit_points -= hero.thunderbolt
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.thunderbolt} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 4:
            opponent.hit_points -= hero.ice_beam
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.ice_beam} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")