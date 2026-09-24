
import csv

students = [
    {"name": "Om", "marks": [85, 92, 78]},
    {"name": "Rahul", "marks": [35, 42, 28]},
    {"name": "Priya", "marks": [95, 88, 91]}
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

def calculate_result(average):
    if average >= 35:
        return "Pass"
    else:
        return "Fail"


with open("student.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name","Total","Average","Result"])

    for student in students:
        name = student["name"]
        marks = student["marks"]

        total = calculate_total(marks)
        average = calculate_average(marks)
        result = calculate_result(average)

        writer.writerow([
           name,
           total,
           average,
           result
        ])

with open("student.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

   