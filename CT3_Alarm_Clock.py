def main():
    # Ask the user for the current time in hours (0-23)
    current_time = int(input("Enter the current time (0-23): "))

    # Ask the user how many hours to wait for the alarm
    wait_time = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the alarm time using modulo arithmetic
    alarm_time = (current_time + wait_time) % 24

    # Display the result
    print(f"\nThe alarm will go off at {alarm_time}:00 on a 24-hour clock.")

if __name__ == "__main__":
    main()
