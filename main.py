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
elif player == 2:
    hero == Pelican()
elif player == 3:
    hero = Starfish()

print(hero)