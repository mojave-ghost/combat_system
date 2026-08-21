import random
from heroes import Wombat, Pelican, Starfish

def random_attack(opponent, hero):
    move = random.randint(1,4)
    if isinstance(opponent, Wombat):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            return print(f"Your hero has taken {opponent.hurricane} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 2:
            hero.hit_points -= opponent.scald
            return print(f"Your hero has taken {opponent.scald} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            return print(f"Your hero has taken {opponent.wide_guard} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 4:
            hero.hit_points -= opponent.protect
            return print(f"Your hero has taken {opponent.protect} damage. {hero}'s hit points are now {hero.hit_points}")
    elif isinstance(opponent, Pelican):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            return print(f"Your hero has taken {opponent.hurricane} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 2:
            hero.hit_points -= opponent.scald
            return print(f"Your hero has taken {opponent.scald} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            return print(f"Your hero has taken {opponent.wide_guard} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 4:
            hero.hit_points -= opponent.protect
            return print(f"Your hero has taken {opponent.protect} damage. {hero}'s hit points are now {hero.hit_points}")
    elif isinstance(opponent, Starfish):
        if move == 1:
            hero.hit_points -= opponent.hurricane
            return print(f"Your hero has taken {opponent.hurricane} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 2:
            hero.hit_points -= opponent.scald
            return print(f"Your hero has taken {opponent.scald} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 3:
            hero.hit_points -= opponent.wide_guard
            return print(f"Your hero has taken {opponent.wide_guard} damage. {hero}'s hit points are now {hero.hit_points}")
        elif move == 4:
            hero.hit_points -= opponent.protect
            return print(f"Your hero has taken {opponent.protect} damage. {hero}'s hit points are now {hero.hit_points}")
    