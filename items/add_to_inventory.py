import json

def add_to_inventory(item):
    # Retrieve display name from dictionary or object
    """
    ISINSTANCE() DOCUMENATION
        isinstance(object, classinfo)
        object: The variable or object you want to check.
        classinfo: A class, data type (like int, str), or a tuple containing multiple classes/types
    """
    if isinstance(item, dict):
        """
        GET() DOCUMENTATION
            dictionary.get(key, default_value)
            key: The name of the key you want to look up.
            default_value (optional): The value returned if the key is missing. It defaults to None if left blank.
        """
        item_name = item.get("name", "Unknown Item")
    else:
        item_name = item.__class__.__name__

    # Read existing save data to avoid wiping out hero name and class
    try:
        with open("save_data.json", "r") as file:
            save_data = json.load(file)
    except FileNotFoundError:
        save_data = {}

    # Initialize or update the inventory list
    if "inventory" not in save_data:
        save_data["inventory"] = []
    
    save_data["inventory"].append(item_name)

    # Write updated data back to file
    with open("save_data.json", "w") as file:
        json.dump(save_data, file, indent=4)

    print(f"{item_name} has been added to your bag.\n")