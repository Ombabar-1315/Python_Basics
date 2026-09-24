name = input("Enter student name: ")
age = input("Enter student age: ")
marks = input("Enter student marks: ")

with open("students.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Marks: {marks}\n")
    file.write("--------------------\n")

print("\nStudent saved successfully!")

with open("students.txt", "r") as file:
    data = file.read()

print("\n----- ALL STUDENTS -----")
print(data)