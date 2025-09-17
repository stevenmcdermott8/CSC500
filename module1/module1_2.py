def main():
    ## begin try block to handle potential exception
    try:
        ## request input number from user
        num1 = int(input('Enter a number: '))
        ## request second input number from user
        num2 = int(input('Enter another number: '))
    except ValueError:
        ## inform user if we specifically get invalid input for the expected input type
        print("Invalid input. Please enter valid integers.")
        ## return here if exception happens to not execute further code
        return

    ## multiply num 1 by num 2 to get resulting value
    multiplicationOfNumbers = num1 * num2
    ## divide num 1 by num 2 to get resulting value
    divisionOfNumbers = num1 / num2

    ## print the results for the user to see
    print(f"{num1} x {num2} = {multiplicationOfNumbers}")
    print(f"{num1} / {num2} = {divisionOfNumbers}")

## main function to run program
if __name__ == "__main__":
    main()