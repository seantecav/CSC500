def CSC500part2():
    # Ask for number of books purchased
    try:
        books = int(input("Enter the number of books purchased this month: "))
        
        if books < 0:
            print("Number of books cannot be negative.")
            return

        # Decision structure for points
        if books == 0:
            points = 0
        elif books == 2:
            points = 5
        elif books == 4:
            points = 15
        elif books == 6:
            points = 30
        elif books >= 8:
            points = 60
        else:
            # If they bought 1, 3, 5, 7 books → 0 points
            points = 0

        print(f"Books purchased: {books}")
        print(f"Points awarded: {points}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


# Run the program
CSC500part2()


