import battle 
import items.shop_menu as shop_menu

def adventure_menu(hero, name):
    while True: 
        try:
            print("1. Battle \n2. Item Shop \n3. \n 0. Exit")
            choice = int(input("Choose your adventure [1-3]: "))
        except ValueError:
            print("Invalid input! Please enter a number.")

        if choice == 1:
            battle.battle(hero, name)
        elif choice == 2:
            shop_menu.shop_menu()
        elif choice == 0:
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valide option")