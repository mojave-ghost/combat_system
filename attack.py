# Select your move
from heroes import Wombat, Pelican, Starfish

def attack(hero, opponent):
    if isinstance(hero, Wombat):
        print("1. Tackle")
        print("2. Headbutt")
        print("3. Double-Edge")
        print("4. Quick Attack")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.tackle
            print(f"You hit your target for {hero.tackle} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 2:
            opponent.hit_points -= hero.headbutt
            print(f"You hit your target for {hero.headbutt} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 3:
            opponent.hit_points -= hero.double_edge
            print(f"You hit your target for {hero.double_edge} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 4:
            opponent.hit_points -= hero.quick_attack
            print(f"You hit your target for {hero.quick_attack} damage. Your target's hit points are now {opponent.hit_points}")
    elif isinstance(hero, Pelican):
        print("1. Hurricane")
        print("2. Scald")
        print("3. Wide Guard")
        print("4. Protect")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.hurricane
            print(f"You hit your target for {hero.hurricane} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 2:
            opponent.hit_points -= hero.scald
            print(f"You hit your target for {hero.scald} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 3:
            opponent.hit_points -= hero.wide_guard
            print(f"You hit your target for {hero.wide_guard} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 4:
            opponent.hit_points -= hero.protect
            print(f"You hit your target for {hero.protect} damage. Your target's hit points are now {opponent.hit_points}")
    elif isinstance(hero, Starfish):
        print("1. Surf")
        print("2. Psychic")
        print("3. Thunderbolt")
        print("4. Ice Beam")
        move = int(input("Select your battle move [1-4]: "))
        if move == 1:
            opponent.hit_points -= hero.surf
            print(f"You hit your target for {hero.surf} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 2:
            opponent.hit_points -= hero.psychic
            print(f"You hit your target for {hero.psychic} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 3:
            opponent.hit_points -= hero.thunderbolt
            print(f"You hit your target for {hero.thunderbolt} damage. Your target's hit points are now {opponent.hit_points}")
        elif move == 4:
            opponent.hit_points -= hero.ice_beam
            print(f"You hit your target for {hero.ice_beam} damage. Your target's hit points are now {opponent.hit_points}")