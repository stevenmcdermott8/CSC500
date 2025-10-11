# Average Rainfaill Program

# Function to get rainfall input for a single month
def get_months_rainfall(month):
    while True:
        try:
            # Prompt user to enter rainfall for the given month
            rainfall = float(input(f"Enter the rainfall (in inches) for month {month}: "))
            
            # Check for negative input
            if rainfall < 0:
                print("Rainfall cannot be negative. Please enter a valid amount.")
            else:
                # Valid input; exit loop and return value
                return rainfall
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a numeric value.")

# Main function to drive the program
def main():
    total_rainfall = 0  # Initialize total rainfall accumulator

    # Ask user for the number of years to collect data
    years = int(input("Enter the number of years: "))

    # Loop through each year
    for year in range(1, years + 1):
        print(f"\nYear {year}")
        
        # Loop through each month in the year
        for month in range(1, 13):
            # Add rainfall for the current month to the total
            total_rainfall += get_months_rainfall(month)

    # Calculate total number of months
    total_months = 12 * years

    # Calculate average rainfall per month
    average_rainfall = total_rainfall / total_months

    # Display the results
    print("\nRainfall Information")
    print(f"Total months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
