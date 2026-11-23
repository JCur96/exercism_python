"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    
    keys = set(items)
    inv_dict = {}
    for key in keys: 
        inv_dict[key] = items.count(key)

    return inv_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    incoming_inv = create_inventory(items)
    for key, value in incoming_inv.items():
        inventory[key] = inventory.get(key, 0) + value
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    incoming_inv = create_inventory(items)
    for key, value in incoming_inv.items():
        if inventory.get(key) == None:
            continue
        if inventory[key] == 0:
            continue
        else:
            current_value = inventory[key] 
            update_value = max(0, current_value - value)
            inventory[key] = update_value
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, 'not found')
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    #out_list = []
    #for key, value in inventory.items():
    #    if inventory[key] > 0:
    #        positive_inv = (key, value)
    #        out_list.append(positive_inv)


    #return out_list

    return [(k,v) for k,v in inventory.items() if inventory[k] > 0]
