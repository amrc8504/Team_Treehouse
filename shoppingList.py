shoppingCart = []

def showHelp():
    print("What should we pick up at the store?\nEnter 'DONE' to stop adding items\nEnter 'HELP' to get help.\nEnter 'SHOW' to see your list.")

def add_to_list(item):
    shoppingCart.append(item)
    print(f'Added {item}.')

def showList():
    print('So far you have:')
    for item in shoppingCart:
        if shoppingCart == []:
            print("Nothing to see here...")
        else:
            print(item.title())

def clearList():
    clear = input("Are you sure? ")
    if clear.lower() == 'y':
        shoppingCart.clear()
        print("You list has been cleared.")
        return shoppingCart
    else:
        cancel = print("Action cancelled.")
        return cancel


showHelp()
def shoppingList():
    while True:
        new_item = input("Add Item: ")
        if new_item == 'DONE':
            break
        elif new_item =='HELP':
            showHelp()
            continue
        elif new_item == 'SHOW':
            showList()
            continue
        elif new_item == 'CLEAR':
            clearList()
            continue
        add_to_list(new_item)
    showList()
shoppingList()