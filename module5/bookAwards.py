# CSU Global Bookstore Book Club Points Program

def get_books_purchases():
    while True:
        user_input = input("Enter the number of books purchased this month: ")
        try:
            books = int(user_input)
            if books < 0:
                print("Number of books cannot be negative. Please enter a valid number.")
            else:
                return books
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_points(books_purchased):
    """Returns the number of points awarded based on books purchased."""
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
    # Prompt user for input
    books = get_books_purchases()
    points = calculate_points(books)
    print(f"You have earned {points} point(s) this month.")

# Run the program
if __name__ == "__main__":
    main()