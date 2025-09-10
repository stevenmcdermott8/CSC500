def main():
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    multiplicationOfNumbers = num1 * num2
    divisionOfNumbers = num1 / num2
    print(f"{num1} x {num2} = {multiplicationOfNumbers}")
    print(f"{num1} / {num2} = {divisionOfNumbers}")

if __name__ == "__main__":
    main()