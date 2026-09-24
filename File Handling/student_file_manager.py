name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
marks = float(input("Enter your marks: "))

result = ""
if marks >= 35:
    result = "Pass"
    

else:
    result = "Fail"

with open("student.txt","a") as file:
    file.write(f"\nname: {name} | Age: {age} | City: {city} | Marks: {marks} | Result: {result}")


with open("student.txt","r") as file:
    data = file.read()

print(data)

