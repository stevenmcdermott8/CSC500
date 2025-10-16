## define class to contain details for items to purchase
class ItemToPurchase:  
    def __init__(self):
        ## initialize item attributes with default values
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = ''

    def print_item_cost(self):
        ## calculate the total cost for the item
        total_cost = self.item_price * self.item_quantity
 
        ## format price and cost: show without decimals if whole number
        formatted_price = (
            f"${int(self.item_price)}" if self.item_price.is_integer() else f"${self.item_price:.2f}"
        )
        formatted_cost = (
            f"${int(total_cost)}" if total_cost.is_integer() else f"${total_cost:.2f}"
        )

        # print the output values
        print('{name} {quantity} @ {price} = {cost}'.format(
            name = self.item_name, 
            quantity = self.item_quantity, 
            price = formatted_price, 
            cost = formatted_cost
        ))