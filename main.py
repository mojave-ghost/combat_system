import combat
from dummy import Dummy
from heroes import Wombat, Pelican, Starfish

print("1. Melee")
print("2. Ranged")
print("3. Spell")
attack = int(input("Select your attack [1-3]: "))
print("1. Wombat")
print("2. Pelican")
print("3. Starfish")
player = int(input("Select your hero [1-3]: "))

target = Dummy()
if (attack == 1):
    target_hit_points = combat.melee(target)
    print(f"You hit your target for 10 melee damage. Your target's hit points is now {target_hit_points}.")
elif (attack == 2):
    target_hit_points = combat.ranged(target)
    print(f"You hit your target for 7.5 spell damage. Your target's hit points is now {target_hit_points}.")
elif (attack == 3):
    target_hit_points = combat.spell(target)
    print(f"You hit your target for 5 spell damage. Your target's hit points is now {target_hit_points}.")

if player == 1:
    hero = Wombat()
    print("1. Tackle")
    print("2. Headbutt")
    print("3. Double-Edge")
    print("4. Quick Attack")
    move = int(input("Select your battle move [1-4]: "))
    if move == 1:
        target.hit_points -= hero.tackle
        print(f"You hit your target for {hero.tackle} damage. Your target's hit points are now {target.hit_points}")
elif player == 2:
    hero == Pelican()
    print("1. Hurricane")
    print("2. Scald")
    print("3. Wide Guard")
    print("4. Protect")
    move = int(input("Select your battle move [1-4]: "))
elif player == 3:
    hero = Starfish()
    print("1. Surf")
    print("2. Psychic")
    print("3. Thunderbolt")
    print("4. Ice Beam")
    move = int(input("Select your battle move [1-4]: "))

print(hero)