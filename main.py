import combat
from dummy import Dummy

print("1. Melee")
print("2. Ranged")
print("3. Spell")
attack = int(input("Select your attack [1-3]: "))

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