def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "F"


def main():
    print("=== Student Marks & Grade Calculator ===")
    name = input("Enter student name: ").strip() or "Student"
    subjects = ["English", "Maths", "Science", "Social"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Please enter a mark between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(subjects)
    grade = get_grade(percentage)
    result = "PASS" if all(mark >= 35 for mark in marks) else "FAIL"

    print("\\n----- RESULT -----")
    print(f"Student: {name}")
    print(f"Total: {total:.1f}/{len(subjects) * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
