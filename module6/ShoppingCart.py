# Import the ItemToPurchase class
from ItemToPurchase import ItemToPurchase

# Define the ShoppingCart class
class ShoppingCart:

    # Constructor initializes customer name, current date, and an empty list for cart items
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an ItemToPurchase object to the cart
    def add_item(self, item_to_add : ItemToPurchase):
        self.cart_items.append(item_to_add)

    # Removes an item from the cart by name
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        # If item is not found, print a message
        if not found:
            print("Item not found in cart. Nothing removed.")

    # Modifies an existing item in the cart if the new item has non-default values
    def modify_item(self, item_to_modify : ItemToPurchase):
        found = False
        for item in self.cart_items:
            # Check if the item name matches
            if item.item_name == item_to_modify.item_name:
                ## update boolean that item is found for later check
                found = True
                
                # Only update if the new values are not default
                if item_to_modify.item_description != '':
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity

                break
        # If item is not found, print a message
        if not found:
            print("Item not found in cart. Nothing modified.")

    # Returns the total number of items in the cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Returns the total cost of all items in the cart
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    # Prints the total cost and details of each item in the cart
    def print_total(self):
        if not self.cart_items:
            print("\nSHOPPING CART IS EMPTY")
        else:
            print('\nOUTPUT SHOPPING CART')
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            num_items = self.get_num_items_in_cart()
            print(f"Number of Items: {num_items}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Prints the description of each item in the cart
    def print_descriptions(self):
        if not self.cart_items:
            print("\nSHOPPING CART IS EMPTY")
        else:
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            print("Item Descriptions")
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")

