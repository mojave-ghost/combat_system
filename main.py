import combat
import dummy

print("1. Melee")
print("2. Ranged")
print("3. Spell")
attack = input("Select your attack [1-3]: ")

if (attack == 1)
    target_hit_points = melee(Dummy)
    print(f"You hit your target for 10 melee damage. Your target's hit points is now {target_hit_points}")
elif (attack == 2)
    target_hit_points = ranged(Dummy)
    print(f"You hit your target for 7.5 spell damage. Your target's hit points is now {target_hit_points}")
elif (attack == 3)
    target_hit_points = spell(Dummy)
    print(f"You hit your target for 5 spell damage. Your target's hit points is now {target_hit_points}")