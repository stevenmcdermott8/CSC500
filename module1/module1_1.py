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

    ## add num 1 + num 2 to get sum
    sumOfNumbers = num1 + num2
    ## subtract num 1 + num 2 to get difference
    differenceOfNumbers = num1 - num2

    ## print the results for the user to see
    print(f"{num1} + {num2} = {sumOfNumbers}")
    print(f"{num1} - {num2} = {differenceOfNumbers}")

## main function to run program
if __name__ == "__main__":
    main()
