# Task 2: Student Grades
# A dictionary stores student names (keys) and their grades (values).

grades = {
    "Amit": "A",
    "Riya": "B",
    "John": "C",
}

while True:
    print()
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in grades:
            print(name, "already exists. Use option 2 to update the grade.")
        else:
            grade = input("Enter grade: ").upper()
            grades[name] = grade
            print(name, "added with grade", grade)

    elif choice == "2":
        name = input("Enter student name: ")
        if name in grades:
            grade = input("Enter new grade: ").upper()
            grades[name] = grade
            print(name, "updated to grade", grade)
        else:
            print(name, "not found. Use option 1 to add the student.")

    elif choice == "3":
        print("--- Student Grades ---")
        for name in grades:
            print(name, ":", grades[name])

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
