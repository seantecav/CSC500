def main():
    food_charge = float(input("Enter the charge for the food: $"))
    tip = food_charge * 0.18
    tax = food_charge * 0.07
    total = food_charge + tip + tax
    print("\n--- Bill Breakdown ---")
    print(f"Food charge: ${food_charge:.2f}")
    print(f"Tip (18%):  ${tip:.2f}")
    print(f"Sales tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
