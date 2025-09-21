def CSC500part1():
    # Ask for number of years
    years = int(input("Enter the number of years: "))

    total_rainfall = 0.0
    total_months = years * 12

    # Outer loop for years
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        
        # Inner loop for 12 months
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Enter inches of rainfall for month {month}: "))
                    if rainfall < 0:
                        print("  Rainfall cannot be negative. Try again.")
                        continue
                    total_rainfall += rainfall
                    break
                except ValueError:
                    print("  Invalid input. Please enter a numeric value.")
    
    # Calculate average
    average = total_rainfall / total_months

    # Display results
    print("\n----- Rainfall Summary -----")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average:.2f} inches")


# Run the program
CSC500part1()
