# Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print (f' {v} {k}')
        item_total += inventory.get(k,0)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    # your code goes here
    for name in addedItems:
        num_item = inventory.setdefault(name,0)
        inventory[name] += 1
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)