python_students = {"Om", "Rahul", "Priya", "Aman"}
java_students = {"Rahul", "Priya", "Sneha"}


unique_students = python_students | java_students

both_students = python_students & java_students

python_only_students = python_students - java_students

java_only_students = java_students - python_students

print("============== Unique Students =======")
print(unique_students)
print()
print("============== Students in Both Courses =======")
print(both_students)
print()
print("============== Python Only Students =======")
print(python_only_students)
print()
print("============== Java Only Students =======")
print(java_only_students)