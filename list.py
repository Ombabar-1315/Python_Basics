students = [
    ["Om",92],
    ["Rahul",85],
    ["Priya",97],
    ["Rudra",35]
]
for student in students:
    print("Name  :",student[0])
    print("Marks :",student[1])
    if student[1] >= 35:
        print("Result : pass")
    else:
        print("Result : fail")
    print("-----------------------")
    