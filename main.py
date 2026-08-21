import combat
from dummy import Dummy
from heroes import Wombat, Pelican, Starfish

# Select your hero
print("1. Wombat")
print("2. Pelican")
print("3. Starfish")
player = int(input("Select your hero [1-3]: "))
target = Dummy()
# Select your opponent
print("1. Wombat")
print("2. Pelican")
print("3. Starfish")
opponent = int(input("Select your opponent [1-3]: "))
if opponent = 1:
    enemy = Wombat()
elif opponent = 2:
    enemy = Pelican()
elif opponent = 3: 
    enemy = Starfish()

# Choose your move
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
    elif move == 2:
        target.hit_points -= hero.headbutt
        print(f"You hit your target for {hero.headbutt} damage. Your target's hit points are now {target.hit_points}")
    elif move == 3:
        target.hit_points -= hero.double_edge
        print(f"You hit your target for {hero.double_edge} damage. Your target's hit points are now {target.hit_points}")
    elif move == 4:
        target.hitpoints -= hero.quick_attack
        print(f"You hit your target for {hero.quick_attack} damage. Your target's hit points are now {target.hit_points}")
elif player == 2:
    hero = Pelican()
    print("1. Hurricane")
    print("2. Scald")
    print("3. Wide Guard")
    print("4. Protect")
    move = int(input("Select your battle move [1-4]: "))
    if move == 1:
        target.hit_points -= hero.hurricane
        print(f"You hit your target for {hero.hurricane} damage. Your target's hit points are now {target.hit_points}")
    elif move == 2:
        target.hit_points -= hero.scald
        print(f"You hit your target for {hero.scald} damage. Your target's hit points are now {target.hit_points}")
    elif move == 3:
        target.hit_points -= hero.wide_guard
        print(f"You hit your target for {hero.wide_guard} damage. Your target's hit points are now {target.hit_points}")
    elif move == 4:
        target.hitpoints -= hero.protect
        print(f"You hit your target for {hero.protect} damage. Your target's hit points are now {target.hit_points}")
elif player == 3:
    hero = Starfish()
    print("1. Surf")
    print("2. Psychic")
    print("3. Thunderbolt")
    print("4. Ice Beam")
    move = int(input("Select your battle move [1-4]: "))
    if move == 1:
        target.hit_points -= hero.surf
        print(f"You hit your target for {hero.surf} damage. Your target's hit points are now {target.hit_points}")
    elif move == 2:
        target.hit_points -= hero.psychic
        print(f"You hit your target for {hero.psychic} damage. Your target's hit points are now {target.hit_points}")
    elif move == 3:
        target.hit_points -= hero.thunderbolt
        print(f"You hit your target for {hero.thunderbolt} damage. Your target's hit points are now {target.hit_points}")
    elif move == 4:
        target.hitpoints -= hero.ice_beam
        print(f"You hit your target for {hero.ice_beam} damage. Your target's hit points are now {target.hit_points}")
