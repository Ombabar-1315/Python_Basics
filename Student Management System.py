students = [
    {
        "name": "Om",
        "age": 20,
        "marks": [85, 92, 88],
        "subjects": {"Python", "C++"}
    },
    {
        "name": "Rahul",
        "age": 21,
        "marks": [65, 72, 70],
        "subjects": {"Python", "Java"}
    },
    {
        "name": "Priya",
        "age": 20,
        "marks": [90, 95, 93],
        "subjects": {"Python", "C++", "Java"}
    }
]


# Calculate total marks
def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


# Calculate average marks
def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    return average


# Check Pass or Fail
def check_result(average):
    if average >= 35:
        return "Pass"
    else:
        return "Fail"


# Find topper
def find_topper(students):

    topper = 0
    topper_name = ""

    for student in students:

        total = calculate_total(student["marks"])

        if total > topper:
            topper = total
            topper_name = student["name"]

    return topper_name, topper


# Get all unique subjects
def get_all_subjects(students):

    subjects = set()

    for student in students:
        subjects.update(student["subjects"])

    return subjects


# Display one student
def display_student(student):

    name = student["name"]
    age = student["age"]
    marks = student["marks"]
    subjects = student["subjects"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    result = check_result(average)

    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Result:", result)
    print("Subjects:", subjects)


# Display all students and summary
def display_all_students(students):

    topper_name, highest_marks = find_topper(students)
    all_subjects = get_all_subjects(students)

    print("Topper:", topper_name)
    print("Highest Marks:", highest_marks)

    print()
    print("All Unique Subjects:", all_subjects)


# Display students
for student in students:

    display_student(student)
    print()


# Summary
print("==================================")
print("\tSUMMARY")
print("==================================")

display_all_students(students)

print("===================================")