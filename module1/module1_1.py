def main():
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    sumOfNumbers = num1 + num2
    differenceOfNumbers = num1 - num2
    print(f"{num1} + {num2} = {sumOfNumbers}")
    print(f"{num1} - {num2} = {differenceOfNumbers}")

if __name__ == "__main__":
    main()
