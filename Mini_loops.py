students = [
    {
        "name": "Om",
        "age": 20,
        "city": "Solapur",
        "marks": 92,
        "subjects": ["Python", "C++"],
        "purchases": [500, 1200, 300]
    },
    {
        "name": "Rahul",
        "age": 21,
        "city": "Pune",
        "marks": 35,
        "subjects": ["Python", "Java"],
        "purchases": [700, 200]
    },
    {
        "name": "Priya",
        "age": 20,
        "city": "Solapur",
        "marks": 95,
        "subjects": ["Python", "C++"],
        "purchases": [1500, 800]
    },
    {
        "name": "Aman",
        "age": 19,
        "city": "Pune",
        "marks": 28,
        "subjects": ["Java", "C++"],
        "purchases": [300, 400]
    },
    {
        "name": "Sneha",
        "age": 21,
        "city": "Mumbai",
        "marks": 78,
        "subjects": ["Python", "Java"],
        "purchases": [900, 600]
    }
]

total = 0
count = 0 
passed_students = 0
failed_students = 0
highest = students[0]["marks"]
highest_name = students[0]["name"]
lowest_name = students[0]["name"]
lowest = students[0]["marks"]   

solapur = 0
pune = 0
mumbai = 0

unique_subject = set ()
amount = 0



for student in students:
     total += 1
     count += student["marks"]

     unique_subject.update(student["subjects"])
    
     if student["marks"] >= 35:
            passed_students += 1
     else:
            failed_students +=1
    
     if student["marks"] > highest:
            
            highest = student["marks"]
            highest_name = student["name"]
    
        
     if student["marks"] < lowest:
            lowest= student["marks"]
            lowest_name = student["name"]


     if "Solapur" in student["city"]:
                solapur += 1 

     if "Pune" in student["city"]:
                    pune += 1 

     if "Mumbai" in student["city"]:
                    mumbai += 1 

    
  

print("===================== Analyzer ======================")
print()
print("Total Students  :",total)

print()

print("Passed Students :",passed_students)
print("Failed Students :",failed_students)

print()

print("Highest Students :",highest_name)
print("Highest Marks  :",highest)
print()

print("Lowest Students :",lowest_name)
print("Lowest Marks  :",lowest)

print()

avg = count/total
print("Average Marks :",avg)

print()

print("Students above average :")

for student in students:
       if student["marks"] > avg:
              print(student["name"])

print()

print("Solapur Students :",solapur)
print("Pune Students    :",pune)
print("Mumbai Students  :",mumbai)
print()

print("Unique Subjects :")
for unique in unique_subject:
        print(unique)
       
print()
print("Students studying Python :")
for student in students:
        if "Python" in student["subjects"]:
                print(student["name"])


print()
print("Students studying Java :")
for student in students:
        if "Java" in student["subjects"]:
                print(student["name"])


print()
print("Students studying c++ :")
for student in students:
        if "C++" in student["subjects"]:
                print(student["name"])



print()
for student in students:
        total_amount = 0
        for price in student["purchases"]:
               
                total_amount += price 
                

        print(student["name"], "->", "₹",total_amount)
                


        
print()
highest_spend = 0
highest_spending_student = ""
total_Spending = 0
for student in students:

    student_total = 0

    for price in student["purchases"]:
        student_total += price
       

    if student_total > highest_spend:
        highest_spend = student_total
        highest_spending_student = student["name"]

            
print("Highest Spending Student :",highest_spending_student)
print("Highest Spending :",highest_spend) 


print()

lowest_spend = None
lowest_spending_student = ""

for student in students:

    student_total = 0

    for price in student["purchases"]:
        student_total += price

    total_Spending += student_total

    if lowest_spend is None or student_total < lowest_spend:
        lowest_spend = student_total
        lowest_spending_student = student["name"]
            
print("Lowest Spending Student :",lowest_spending_student)
print("Lowest Spending :",lowest_spend) 

print()

print("Average Spending :",total_Spending/total)
print()
for student in students:

    student_total = 0

    for price in student["purchases"]:
        student_total += price

    if student["marks"] >= 80 and student_total > 1000:
        print(student["name"])
        




print("==========================================================")