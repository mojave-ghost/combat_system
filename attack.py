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
            opponent.hit_points -= hero.moves[0]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[0]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 2:
            opponent.hit_points -= hero.moves[1]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[1]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 3:
            opponent.hit_points -= hero.moves[2]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[2]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 4:
            opponent.hit_points -= hero.moves[2]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[2]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
    elif isinstance(hero, Pelican):
        print("1. Hurricane")
        print("2. Scald")
        print("3. Wide Guard")
        print("4. Protect")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.moves[0]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[0]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 2:
            opponent.hit_points -= hero.moves[1]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[1]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 3:
            opponent.hit_points -= hero.moves[2]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[2]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 4:
            opponent.hit_points -= hero.moves[3]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[3]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
    elif isinstance(hero, Starfish):
        print("1. Surf")
        print("2. Psychic")
        print("3. Thunderbolt")
        print("4. Ice Beam")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.moves[0]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[0]['damage']} damage. Your target's hit points are now {opponent.hit_points}." )
            print("********************************************************************************************************* \n")
        elif move == 2:
            opponent.hit_points -= hero.moves[1]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[1]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 3:
            opponent.hit_points -= hero.moves[2]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[2]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")
        elif move == 4:
            opponent.hit_points -= hero.moves[3]['damage']
            print("*********************************************************************************************************")
            print(f"{name} hit the enemy target for {hero.moves[3]['damage']} damage. Your target's hit points are now {opponent.hit_points}.")
            print("********************************************************************************************************* \n")