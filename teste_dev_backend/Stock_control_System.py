
#global list to simulate a Data base.
global_stock=[]
#id item
item_id_counter = 0

#menu do estoque.
def menu():
    while True:
        print('--------------------')
        print('>>>Control Stock<<<')
        print('--------------------')
        print('[1] Register New Item')
        print('[2] List Items of Stock')
        print('[3] Remove Item from stock')
        print('[4] Exit')

        try:
            option = int(input('Select One Option: '))
        except ValueError:
            print('Ops, select one option between 1 and 4')
            continue
        if 1 <= option <=4:
            if option == 1:
                registeritem()
            elif option == 2:
                listitems()
            elif option == 3:
                removeitem()
            elif option == 4:
                break
        else:
            print('Invalid Option! Please type a number between 1 and 4 of menu.')
#registro de item. 
def registeritem():
    global item_id_counter
    print('-----------------------')
    print('>>>Register new item<<<')
    print('-----------------------')
    name_of_item = str(input('Enter Item Name: '))
    while True:
        try:
            quantity_of_item = int(input('Type the quantity of item: '))
            if quantity_of_item <0:
                print('Quantity must be positive')
            else:
                break
        except ValueError:
            print('Please, Enter a Int Number!')

    item={
        "ID": item_id_counter,
        "Name": name_of_item,
        "Quantity": quantity_of_item
    }
    global_stock.append(item)
    item_id_counter += 1
    print('--------------------')
    print('>>>Add successfully<<<')
    print('--------------------')
#listagem dos itens.
def listitems(pause_on_exit=True):
    print('--------------------------------------------')
    print('>>>>>>>>>>>>>>>>List of Stock<<<<<<<<<<<<<<<')
    print('--------------------------------------------')

    if not global_stock:
        print('Stock is currently empty')
    else:
        print(f"{'ID':<4} | {'Name':<20} | {'Quantity':>8}")
        print('-------------------------------------------')
        for item in global_stock:
            output_line = f"{item['ID']:<4} | {item['Name']:<20} | {item['Quantity']:>8}"
            print(output_line)
    if pause_on_exit:
        input("Press Enter to return to the Main Menu...")

#remoção dos itens do estoque
def removeitem():
    print('-----------------')
    print('>>>Remove item<<<')
    print('-----------------')

    if not global_stock:
        print('Stock is currently empty')
        return
    else:
        listitems(pause_on_exit=False)

        while True:
            try:
                id_to_remove = int(input('Type the ID that you want remove: '))
                if id_to_remove <0:
                    print('ID must be 0 or greater.')
                else:
                    break
            except ValueError:
                print('Please type a Number ID')
            
        item_found = False
        for index, item in enumerate(global_stock, start=0):
            if item['ID'] == id_to_remove:
                global_stock.pop(index)
                print(f"Success! Removed item ID {id_to_remove}")
                item_found = True
                break

        if not item_found:
            print(f"Error: Item with ID {id_to_remove} was not found in stock.")
        
        input('\n Press ENTER to return to the main menu...')
menu()