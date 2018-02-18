#! python3
def addToInventory(inventory, addedItems):
    inve = inventory
    for i in addedItems:
        if i in inve.keys():
            inve[i] = inve[i] + 1
    return inve


def displayInventory(inventory):
    print('Inventory:')
    for i in inventory.keys():
        print(inventory[i], i)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
