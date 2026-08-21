import random

def random_attack(opponent, hero):
    move = random.randinit(1,4)
    if isinstance(opponent, Wombat):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            print(f"You hit your target for {opponent.hurricane} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 2:
            hero.hit_points -= opponent.scald
            print(f"You hit your target for {opponent.scald} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            print(f"You hit your target for {opponent.wide_guard} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 4:
            hero.hitpoints -= opponent.protect
            print(f"You hit your target for {opponent.protect} damage. Your target's hit points are now {hero.hit_points}")
    elif isintance(opponent, Pelican):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            print(f"You hit your target for {opponent.hurricane} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 2:
            hero.hit_points -= opponent.scald
            print(f"You hit your target for {opponent.scald} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            print(f"You hit your target for {opponent.wide_guard} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 4:
            hero.hitpoints -= opponent.protect
            print(f"You hit your target for {opponent.protect} damage. Your target's hit points are now {hero.hit_points}")
    elif isinstance(opponent, Starfish):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            print(f"You hit your target for {opponent.hurricane} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 2:
            hero.hit_points -= opponent.scald
            print(f"You hit your target for {opponent.scald} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            print(f"You hit your target for {opponent.wide_guard} damage. Your target's hit points are now {hero.hit_points}")
        elif move == 4:
            hero.hitpoints -= opponent.protect
            print(f"You hit your target for {opponent.protect} damage. Your target's hit points are now {hero.hit_points}")
    