import csv

students = [
    {"name": "Om", "marks": [85, 92, 88]},
    {"name": "Rahul", "marks": [65, 72, 70]},
    {"name": "Priya", "marks": [90, 95, 93]}
]


def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)

    return average


def check_result(average):
    if average >= 35:
        return "Pass"
    else:
        return "Fail"


with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Total", "Average", "Result"])

    # Process each student
    for student in students:

        name = student["name"]
        marks = student["marks"]

        total = calculate_total(marks)
        average = calculate_average(marks)
        result = check_result(average)

        writer.writerow([
            name,
            total,
            f"{average:.2f}",
            result
        ])

print("Student results saved successfully!")