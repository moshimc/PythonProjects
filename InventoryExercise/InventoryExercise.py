#inventory.py


# ----------------------------------------
# Imports
# ----------------------------------------


# ----------------------------------------
# Properties
# ----------------------------------------
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# ----------------------------------------
# Name: addToInventory
# Abstract: add items to dictionary
# ----------------------------------------
def addToInventory(inventory, addedItems):
    for gear, stock in inventory.items():
        for loot in addedItems:
            if loot == gear:
                inventory[gear] += 1
    return inventory


# ----------------------------------------
# Name: displayInventory
# Abstract: display inventory contents
# ----------------------------------------
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for gear, stock in inventory.items():
        print(str(stock) + ' ' + gear)
        item_total += stock
    print("Total number of items: " + str(item_total))


# ----------------------------------------
# START
# ----------------------------------------
displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
