# import necessary classes
from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase

## wrap gathering input name in function with validation
def get_customer_name():
    while True:
        ## request customer name from user
        name = input("Enter customer's name: ").strip()
        ## validate that name is not empty
        if name:
            return name
        else:
            print("Invalid input. Customers name cannot be empty. Please enter a valid name.")

## wrap gathering input date in function with validation
def get_todays_date():
    while True:
        ## request date from user
        date = input("Enter today's date: ").strip()
        ## validate that date is not empty
        if date:
            return date
        else:
            print("Invalid input. Today's date cannot be empty. Please enter a valid date.")


## wrap gathering input name in function with validation
def get_input_name():
    while True:
        ## request item name from user
        name = input('Enter the item name: ').strip()
        ## validate that name is not empty
        if name:
            return name
        else:
            print("Invalid input. Item name cannot be empty. Please enter a valid name.")

## wrap gathering input price in function to add error handling to gather valid values
def get_input_price():
     while True:
        ## begin try block to handle potential exception
        try:
            ## request input number from user, converting to float
            price = float(input('Enter the item price: '))
            ## return price if valid float
            return price
        except ValueError:
            ## inform user if we specifically get invalid input for the expected input type
            print("Invalid input. Please enter valid float values only.")
            ## loop continues until valid input is received

## wrap gathering input price in function to add error handling to gather valid values
def get_input_quantity():
     while True:
        ## begin try block to handle potential exception
        try:
            ## request input number from user, converting to integer
            quantity = int(input('Enter the item quantity: '))
            ## return quantity if valid integer
            return quantity
        except ValueError:
            ## inform user if we specifically get invalid input for the expected input type
            print("Invalid input. Please enter valid integer values only.")
            ## loop continues until valid input is received

## wrap gathering input name in function with validation
def get_input_description():
    while True:
        ## request item name from user
        name = input('Enter the item description: ').strip()
        ## validate that name is not empty
        if name:
            return name
        else:
            print("Invalid input. Item description cannot be empty. Please enter a valid description.")

# Function to display and handle the shopping cart menu
def print_menu(cart: ShoppingCart):
    # Define the menu options as a string to display for the user
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "d - Change item description\n"
        "p - Change item price\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    # Loop to continuously show the menu until the user chooses to quit
    while True:
        # show the menu to the user
        print(menu)
        choice = input("Choose an option: ").lower().strip()

        # Exit the loop if user chooses to quit
        if choice == 'q':
            print("Exiting menu.")
            break

        # Add a new item to the cart
        elif choice == 'a':
            item_name = get_input_name()  # Get item name from user
            item_description = get_input_description()  # Get item description
            item_price = get_input_price()  # Get item price
            item_quantity = get_input_quantity()  # Get item quantity

            # Create a new item and set its attributes
            item = ItemToPurchase()
            item.item_name = item_name
            item.item_price = item_price
            item.item_quantity = item_quantity
            item.item_description = item_description

            # Add the item to the shopping cart
            cart.add_item(item)

        # Remove an item from the cart
        elif choice == 'r':
            item_name = get_input_name()
            cart.remove_item(item_name)

        # Modify the description of an existing item
        elif choice == 'd':
            # create new instance of object to apply modifications
            item_for_modify = ItemToPurchase()
            item_for_modify.item_name = get_input_name()
            item_for_modify.item_description = get_input_description()
            cart.modify_item(item_for_modify)
                
        # Modify the price of an existing item
        elif choice == 'p':
            # create new instance of object to apply modifications
            item_for_modify = ItemToPurchase()
            item_for_modify.item_name = get_input_name()
            item_for_modify.item_price = get_input_price()
            cart.modify_item(item_for_modify)

        # Modify the quantity of an existing item
        elif choice == 'c':
            # create new instance of object to apply modifications
            item_for_modify = ItemToPurchase()
            item_for_modify.item_name = get_input_name()
            item_for_modify.item_quantity = get_input_quantity()
            cart.modify_item(item_for_modify)

        # Print descriptions of all items in the cart
        elif choice == 'i':
            cart.print_descriptions()

        # Print the total cost and details of the cart
        elif choice == 'o':
            cart.print_total()
            
        else:
            print("Invalid option. Please try again.")

# Main function to initialize the shopping cart and start the menu
def main():
    # Get customer name and current date
    customer_name = get_customer_name()
    current_date = get_todays_date()

    # Create a ShoppingCart object with the provided name and date
    cart = ShoppingCart(customer_name, current_date)

    # Display customer info
    print(f"\nCustomer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")

    # Start the menu loop
    print_menu(cart)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()