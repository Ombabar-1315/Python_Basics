python = {"Om", "Rahul", "Priya", "Aman"}
java = {"Rahul", "Priya", "Sneha"}

all_students = python | java
print(all_students)
print()
all_students = python & java
print(all_students)
print()

all_students = python - java
print(all_students)
