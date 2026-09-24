import csv
import json

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

def calculate_total_marks(marks):
    return sum(marks)

def calculate_average_marks(marks):
    average = sum(marks) / len(marks)
    return average

def check_result(average):
    if average >= 35:
        return "Pass"
    else:
        return "Fail"

def find_topper(students):

     topper = ""
     high_marks = 0
     for student in students:
          marks = student["marks"]
          total = calculate_total_marks(marks)

          if total > high_marks:
               high_marks = total
               topper = student["name"]
     return topper,high_marks

def get_all_subject(students):
  
     all_subject = set()

     for student in students:
          all_subject.update(student["subjects"])

     return all_subject

    
      

def student_display(students):
        topper , high = find_topper(students)
        for student in students:

            name = student["name"]
            age = student["age"]
            marks = student["marks"]
            subject = student["subjects"]

            total = calculate_total_marks(marks)
            average = calculate_average_marks(marks)
            result = check_result(average)
            print("Name: ",name)
            print("Age: ",age)
            print("Marks: ",marks)
            print("Subject: ",subject)
            print("Total: ",total)
            print("Average: ",average)
            print("Result: ",result)
            print("-------------------------")
        print()
        print("Topper :",topper)
        print("Highest Total: ",high)

        subjects = get_all_subject(students)
        print("Unique Subject :")
        for sub in subjects:
             print(sub)


student_display(students)

with open("students_result.csv","a",newline="") as file:
     writer = csv.writer(file)

     writer.writerow(["Name","Age","Total","Average","Result"])

     for student in students:
          total = calculate_total_marks(student["marks"])
          average = calculate_average_marks(student["marks"])
          result = check_result(average)

          writer.writerow([
               student["name"],
               student["age"],
               total,
               average,
               result
          ])

print("\nStudent results saved to student_results.csv")


with open("students_result.csv","r") as file:
     reader = csv.DictReader(file)

     for row in reader:
          print(
            row["Name"],
            "| Total:",
            row["Total"],
            "| Average:",
            row["Average"],
            "| Result:",
            row["Result"]
        )



      

        