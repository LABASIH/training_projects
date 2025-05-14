

inventory = [{'product':'rice', 'price':5000,'quantity':12},
             {'product':'onions', 'price':1250,'quantity':45},
             {'product':'bead', 'price':2700,'quantity':23},
             {'product':'toilet paper', 'price':2000,'quantity':16},
             {'product':'tooth paste', 'price':3450,'quantity':7}
             ]

def add_product():

    print('\n--- Add new product ---')
    # Asks the user to enter a product
    product = input('\nEnter the product you want to add: ').strip().lower()
    # Loops through out the inventory and checks for any duplicated value
    for products in inventory:
        if products['product'] == product.lower().strip():
            print('The product is already in the list')
            return

    while True:
        try: 
            # Asks the user to enter a price for the product          
            price = float(input('Enter a price for the product: $'))
            if price > 0:         
                break
            else:
                print('The value must be positive for price')
        except ValueError:
            print('Please enter a valid value for price')

    while True:
        try:
             # Asks the user to enter a quantity for the product           
             quantity = int(input('Enter the quantity for the product: '))

             if quantity > 0:         
                 break
             else:
                 print('The value must be positive for quantity')
        except ValueError:
                print('Please enter a valid value for quantity')
    # Gives the structure for the dictionary       
    inv = {'product': product.lower().strip(),
            'price':price,
            'quantity':quantity
            }
    # Add the new dictionary to the list   
    inventory.append(inv)
    print(f'{product} was added succesfully to the inventory')

def find_product():

    print('\n--- Look for product ---')
    # Asks the user for the product that is looking for
    find_product = input('\nEnter the product you are looking for: ').strip().lower()
    # Loops through out the inventory and checks for any coincidence and prints the product description
    for products in inventory:
        if products['product'] == find_product:
             print('\n--- Product description ---')
             print(f'\nProduct: {products['product']}')
             print(f'Price: ${products['price']}')
             print(f'Quantity: {products['quantity']}')
             return
    
    print(f'The product {find_product} was not found')

def change_price():

    product = input('Enter the name of the product you want to change the price: ')
     # Loops through the inventory and checks for any coincidence
    for products in inventory:
        if products['product'] == product:

            try:
                # If matches, ask the user for the new price 
                new_price = float(input('Enter the new price for the product $'))
                # Checks if the value entered is positive for price, then prints the confirmation
                if new_price > 0:
                   products['price'] = new_price
                   print('The price was updated succesfully')
                   return
            except ValueError:
                print('The new price must be a positive value')

def delete_product():

    print('\n---Delete a product---')
    # Asks the user for the product that wants to delete
    product = input('\nEnter the name of the product you want to delete: ').strip().lower()
    # Loops through out the inventory and gets the index of the product
    for i,products in enumerate(inventory):
        if products['product'] == product:
            # Deletes the product that matches the iteration and the product gived by the user
            del inventory[i]
            print(f'The product {product} was deleted succesfully')
            return
          
    print('\nThe product was not found')

def total():

    print('\n--- Calculate the total value of the inventory ---')
    # Uses of lambda function to calculate the value of each product multiplying the price and the quantity
    calculate_value = lambda p: p['price'] * p['quantity']
    total = 0 
    # Loops through out the inventory and uses the variable with the anonymous function to apply it to each product
    for products in inventory:
        total_product = calculate_value(products)
        total += total_product
    # Gives the total value of the inventory if the condition is meeted
    if total > 0:
        print(f'\nThe total value of the inventory is ${total:.2f}')
    else:
        print('The inventory is empty')


def menu():
    # Shows the menu while the condition is meeted
    while True:
        print('\n-----| Menu |-----')
        print('1. Add products')
        print('2. Look for products')
        print('3. Change price of a product')
        print('4. Delete product')
        print('5. Total price of the inventory')
        print('6. Exit')
        # Asks the user to choose the function that wants to use
        option = input('\nEnter the option you want to use: ')
        # Calls each defined function when the user gives the right option 
        if option == '1':
            add_product()
           
        elif option == '2':
            find_product()
        
        elif option == '3':
            change_price()
        
        elif option == '4':
            delete_product()
        
        elif option == '5':
            total()
               
        elif option == '6':
            print('\n--- The program is closing ---')
            break
        
        else:
            print('The option selected is not valid. Choose another option')
        
menu()
