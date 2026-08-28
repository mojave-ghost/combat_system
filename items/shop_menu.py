from . import item_data
from .add_to_inventory import add_to_inventory

def shop_menu():
    print("\nITEMS")
    print(f"1. {item_data.shop_catalog_level1[0]['name']}: ", end="")
    print(f"{item_data.shop_catalog_level1[0]['description']}")
    print(f"2. {item_data.shop_catalog_level1[1]['name']}: ", end="")
    print(f"{item_data.shop_catalog_level1[1]['description']}")
    print(f"3. {item_data.shop_catalog_level1[2]['name']}: ", end="")
    print(f"{item_data.shop_catalog_level1[2]['description']}")
    print(f"4. {item_data.shop_catalog_level1[3]['name']}: ", end="")
    print(f"{item_data.shop_catalog_level1[3]['description']}")
    print(f"5. {item_data.shop_catalog_level1[4]['name']}: ", end="")
    print(f"{item_data.shop_catalog_level1[4]['description']}")

    try:
        # Hard code catalog length = 5
        choice = int(input("\nBUY AN ITEM [1-5] OR exit [0]: "))
        if choice == 1:
            print(f"You bought a {item_data.shop_catalog_level1[0]['name']}.")
        elif choice == 2:
            print(f"You bought a {item_data.shop_catalog_level1[1]['name']}.")
        elif choice == 3:
            print(f"You bought a {item_data.shop_catalog_level1[2]['name']}.")
        elif choice == 4:
            print(f"You bought a {item_data.shop_catalog_level1[3]['name']}.")
        elif choice == 5:
            print(f"You bought an {item_data.shop_catalog_level1[4]['name']}.")
        else:
            print("You have exited the item shop.")
    except ValueError:
        choice = 0

    # buy shop item and add to save_data.json
    if 1 <= choice <= 5:
        selected_item = item_data.shop_catalog_level1[choice - 1]
        print(f"\n You have bought a {selected_item['name']}.")
        add_to_inventory(selected_item)
    else:
        print("You have exited the item shop.")

    

