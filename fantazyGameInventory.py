#Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total+=int(v)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

#List to Dictionary Function for Fantasy Game Inventory

def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k not in inventory.keys():
            inventory.setdefault(k,1)
        else:
            inventory[k]+=1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)




