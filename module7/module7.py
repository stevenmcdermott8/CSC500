def main():
    # Dictionaries mapping of rooms per class
    rooms = {
        "CSC101": "3004",   # Room number for CSC101
        "CSC102": "4501",   # Room number for CSC102
        "CSC103": "6755",   # Room number for CSC103
        "NET110": "1244",   # Room number for NET110
        "COM241": "1411",   # Room number for COM241
    }

    # Dictionaries mapping of instructor per class
    instructors = {
        "CSC101": "Haynes",     # Instructor for CSC101
        "CSC102": "Alvarado",   # Instructor for CSC102
        "CSC103": "Rich",       # Instructor for CSC103
        "NET110": "Burke",      # Instructor for NET110
        "COM241": "Lee",        # Instructor for COM241
    }

    # Dictionaries mapping of times per class
    times = {
        "CSC101": "8:00 a.m.",   # Meeting time for CSC101
        "CSC102": "9:00 a.m.",   # Meeting time for CSC102
        "CSC103": "10:00 a.m.",  # Meeting time for CSC103
        "NET110": "11:00 a.m.",  # Meeting time for NET110
        "COM241": "1:00 p.m.",   # Meeting time for COM241
    }

    # Create a set of valid course codes (keys assumed to be shared by all dictionaries)
    valid_courses = set(rooms.keys())

    # Display initial instructions to the user
    print("Course Lookup. Type a course code (e.g., CSC101), or 'quit' to exit.\n")

    try:
        # Infinite loop to keep asking for user input until they exit
        while True:
            # Prompt user for input, strip whitespace, and convert to uppercase
            user_input = input("Enter a course number: ").strip().upper()

            # Check if user wants to quit
            if user_input in {"QUIT", "EXIT"}:
                print("Goodbye!")
                break

            # If input matches a valid course, display its details
            if user_input in valid_courses:
                print(f"\nCourse:       {user_input}")
                print(f"Room:         {rooms[user_input]}")
                print(f"Instructor:   {instructors[user_input]}")
                print(f"Meeting Time: {times[user_input]}\n")
            else:
                # Handle invalid course input
                print("\nSorry, that course number was not found.")
                print("Available courses:", ", ".join(sorted(valid_courses)))
                print("Please try again or type 'quit' to exit.\n")

    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C interruption
        print("\n\nGoodbye!")


# Entry point of the program
if __name__ == "__main__":
    main()