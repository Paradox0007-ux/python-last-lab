
def calculate_performance(*args, **kwargs):

    if len(args) == 0:
        print("No marks available!")
        return None

    total = sum(args)
    minimum = min(args)
    maximum = max(args)
    average = total / len(args)

    grade_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for mark in args:
        if mark >= 90:
            grade_count["A"] += 1
        elif mark >= 80:
            grade_count["B"] += 1
        elif mark >= 70:
            grade_count["C"] += 1
        elif mark >= 60:
            grade_count["D"] += 1
        else:
            grade_count["F"] += 1

    print("\nStudent Name:", kwargs.get("name", "Unknown"))
    print("Subject:", kwargs.get("subject", "General"))

    return minimum, maximum, average, grade_count


while True:
    print("\n===== CLASS PERFORMANCE ANALYZER =====")
    print("1. Analyze Student Performance")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        subject = input("Enter subject: ")

        marks_input = input("Enter marks separated by spaces: ")
        marks = tuple(map(float, marks_input.split()))

        result = calculate_performance(
            *marks,
            name=name,
            subject=subject
        )

        if result is not None:
            minimum, maximum, average, grades = result

            print("\n===== PERFORMANCE REPORT =====")
            print("Minimum Marks:", minimum)
            print("Maximum Marks:", maximum)
            print("Average Marks:", round(average, 2))
            print("Grade Distribution:", grades)

    elif choice == "2":
        print("Exiting Performance Analyzer...")
        break

    else:
        print("Invalid choice!")
