# Course data
ROOMS = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

INSTRUCTORS = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

TIMES = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def lookup_course(course_code: str):
    """Return (room, instructor, time) for a course_code or None if not found."""
    course_code = course_code.strip().upper()
    if course_code in ROOMS and course_code in INSTRUCTORS and course_code in TIMES:
        return ROOMS[course_code], INSTRUCTORS[course_code], TIMES[course_code]
    return None


def main():
    print("Course Lookup")
    print("Enter a course number (e.g., CSC101). Type 'q' to quit.\n")
    while True:
        user_input = input("Course number: ").strip()
        if user_input.lower() in {"q", "quit", "exit"}:
            print("Goodbye.")
            break

        result = lookup_course(user_input)
        if result:
            room, instructor, time = result
            code = user_input.strip().upper()
            print(f"\nCourse:      {code}")
            print(f"Room:        {room}")
            print(f"Instructor:  {instructor}")
            print(f"Time:        {time}\n")
        else:
            print("Sorry, that course was not found. Try again.\n")


if __name__ == "__main__":
    main()
