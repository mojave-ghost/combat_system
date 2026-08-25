import battle 

def adventure_menu(hero, name):
    print("1. Battle \n2. \n3. ")
    choice = int(input("Choose your adventure [1-3]: "))

    if choice == 1:
        battle.battle(hero, name)