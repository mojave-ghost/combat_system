import battle 
import items.shop_menu as shop_menu

def adventure_menu(hero, name):
    print("1. Battle \n2. Item Shop \n3. ")
    choice = int(input("Choose your adventure [1-3]: "))

    if choice == 1:
        battle.battle(hero, name)
    elif choice == 2:
        shop_menu.shop_menu()