import student_utils as stud

students = [
    {"name": "Om", "marks": [85, 92, 88]},
    {"name": "Rahul", "marks": [65, 72, 70]},
    {"name": "Priya", "marks": [90, 95, 93]}
]
def student_display(students):
 
   
 for student in students:
   marks = student["marks"]
   name = student["name"]

   total = stud.calculate_total(marks)
   avg = stud.calculate_average(marks)
   result = stud.check_result(avg)
   highest = stud.find_highest(marks)
   print("Name :",name)
   print("Total Marks :",total)
   print("Average :",avg)
   print("Result :",result)
   print("Highest :",highest)
   print()



student_display(students)
   
   