## define class to contain details for items to purchase
class ItemToPurchase:  
    def __init__(self):
        ## initialize item attributes with default values
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        ## calculate the total cost for the item
        total_cost = self.item_price * self.item_quantity
        print('{name} {quantity} @ ${price:.2f} = ${cost:.2f}'.format(
            name = self.item_name, 
            quantity = self.item_quantity, 
            price = self.item_price, 
            cost = total_cost
        ))

## wrap gathering input name in function with validation
def get_input_name():
    while True:
        ## request item name from user
        name = input('Enter the item name:\n').strip()
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
            price = float(input('Enter the item price:\n'))
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
            quantity = int(input('Enter the item quantity:\n'))
            ## return quantity if valid integer
            return quantity
        except ValueError:
            ## inform user if we specifically get invalid input for the expected input type
            print("Invalid input. Please enter valid integer values only.")
            ## loop continues until valid input is received
    
## main function to run program
def main():
    ## Gather details for first item
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = get_input_name()
    item1.item_price = get_input_price()
    item1.item_quantity = get_input_quantity()

    ## gather details for second item
    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = get_input_name()
    item2.item_price = get_input_price()
    item2.item_quantity = get_input_quantity()

    ## multiply each items price by quantity to get total cost of each item then add these values together 
    ## to get total cost
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity

    ## print the final output including each item and the total cost
    ## simulating an itemized receipt
    print('\n\nTOTAL COST\n')
    item1.print_item_cost()
    item2.print_item_cost()
    print("\nTotal: ${:.2f}".format(total_cost))

## run main function if script is executed directly
if __name__ == "__main__":
    main()
