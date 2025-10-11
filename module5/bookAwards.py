# CSU Global Bookstore Book Club Points Program
def get_books_purchases():
    """
    Prompts the user to enter the number of books purchased this month.
    Validates the input to ensure it's a non-negative integer.
    Returns the number of books purchased.
    """
    while True:
        user_input = input("Enter the number of books purchased this month: ")
        try:
            books = int(user_input)  # Try converting input to an integer
            if books < 0:
                # Reject negative numbers
                print("Number of books cannot be negative. Please enter a valid number.")
            else:
                # Valid input; return the number
                return books
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a whole number.")

def calculate_points(books_purchased):
    """
    Calculates and returns the number of points awarded based on the number of books purchased.
    
    Points system:
    - 8 or more books: 60 points
    - 6–7 books: 30 points
    - 4–5 books: 15 points
    - 2–3 books: 5 points
    - 0–1 books: 0 points
    """
    points_awarded = 0
    if books_purchased >= 8:
        points_awarded = 60
    elif books_purchased >= 6:
        points_awarded = 30
    elif books_purchased >= 4:
        points_awarded = 15
    elif books_purchased >= 2:
        points_awarded = 5
    else:
        points_awarded = 0
    
    return points_awarded

def main():
    """
    Main function to run the Book Club Points Program.
    - Gets the number of books purchased from the user.
    - Calculates the points earned.
    - Displays the result to the user.
    """
    books = get_books_purchases()  # Get user input
    points = calculate_points(books)  # Calculate points based on input
    print(f"You have earned {points} point(s) this month.")  # Display result

# Entry point of the program
if __name__ == "__main__":
    main()
