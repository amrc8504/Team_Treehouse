shoppingCart = []


def showHelp():
    print("What should we pick up at the store?\nEnter 'DONE' to stop adding items\nEnter 'HELP' to get help.\nEnter 'SHOW' to see your list.\nEnter 'CLEAR' to clear your list.\nEnter 'REMOVE' to remove an item.")


def add_to_list(item):
    item = item.title()
    shoppingCart.append(item)
    print(f'Added {item}.')


def showList():
    print('Your list:')
    for item in shoppingCart:
        if item == False:
            print("Nothing to see here...")
        else:
            print(item.title())


def clearList():
    clear = input("Are you sure? [Y/N] ")
    if clear.lower() == 'y':
        shoppingCart.clear()
        print("You list has been cleared.")
        return shoppingCart
    else:
        cancel = print("Action cancelled.")
        return cancel


def removeItem():
    removedItem = input(
        "What item do you want to remove from your list? ").title()
    try:
        if removedItem not in shoppingCart:
            raise ValueError(f'{removedItem.title()} is not on the list.')
    except ValueError as err:
        print(f'No need, {err}')
    else:
        shoppingCart.remove(removedItem)
        print(f'{removedItem} was removed.')


showHelp()


def shoppingList():
    while True:
        new_item = input("Add Item: ")
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            showHelp()
            continue
        elif new_item == 'SHOW':
            showList()
            continue
        elif new_item == 'CLEAR':
            clearList()
            continue
        elif new_item == 'REMOVE':
            removeItem()
            continue
        add_to_list(new_item)
    showList()


shoppingList()
