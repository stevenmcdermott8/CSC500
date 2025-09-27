'''
Write a program that calculates the total amount of a meal 
purchased at a restaurant. The program should ask the user to enter 
the charge for the food and then calculate the amounts with an 18 percent 
tip and 7 percent sales tax. Display each of these amounts and the total price
'''

## defining constants for tip and tax percentage
# set tip and tax amounts to variables, allows to change values easier later
# represent percentages as a value between 0-1 with 0 being 0% and 1 being 100%
TIP_PERCENTAGE = 0.18
TAX_PERCENTAGE = 0.07

# define function to gather cost and handle errors
def get_cost():
    ''' surround with try/except to catch invalid input and prevent application
    from crashing, put inside a loop to allow running function until valid input is given'''
    while True:
        ## begin try block to handle potential exception
        try:
            # gather data from user for total cost for food
            food_cost = float(input('Enter the cost of the food: '))
            if food_cost < 0:
                print("Food cost cannot be negative. Please enter a valid amount.")
                continue
            # return the food cost value entered
            return food_cost
        except ValueError:
            # inform user if we specifically get invalid input for the expected input type
            print("Invalid input. Please enter valid float values representing dollars and cents. eg: 12.34.")


def main():
    # store the gather value of the food cost
    food_cost = get_cost()
    
    # calculate the tip total
    tip_total = food_cost * TIP_PERCENTAGE

    # calculate the tax total
    tax_total = food_cost * TAX_PERCENTAGE

    # caclulcate the final out of pocket amount
    total_cost = food_cost + tip_total + tax_total

    '''print out values, format all values as dollar amounts using '$' 
    and {:.2f} to ensure printing 2 decimal places for the float values'''
    print('Total food cost: ${:.2f}'.format(food_cost))
    print('Total tip (18%): ${:.2f}'.format(tip_total))
    print('Total tax (7%): ${:.2f}'.format(tax_total))
    print('Total cost: ${:.2f}'.format(total_cost))


# main function to run program
if __name__ == "__main__":
    main()