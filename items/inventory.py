import json

def inventory(item):
    save_data = {
        "item": item
    }
    with open("save_data.json", "w") as file:
        json.dump(save_data, file)
    print(f"{item.__class__.name} has been added to your bag. \n")