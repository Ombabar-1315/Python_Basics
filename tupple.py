students = [
    {
        "name": "Om",
        "marks": 92,
        "courses": {"Python", "C++"}
    },
    {
        "name": "Rahul",
        "marks": 35,
        "courses": {"Python", "Java"}
    },
    {
        "name": "Priya",
        "marks": 95,
        "courses": {"Python", "C++"}
    },
    {
        "name": "Aman",
        "marks": 28,
        "courses": {"Java", "C++"}
    },
    {
        "name": "Sneha",
        "marks": 78,
        "courses": {"Python", "Java"}
    }
]

total = 0
count = 0 
passed_students = 0
failed_students = 0
highest = students[0]["marks"]
highest_name = ""
lowest_name = ""
lowest = students[0]["marks"]   


unique_sets = set()


for student in students:
    total += 1
    count += student["marks"]
    unique_sets.update(student["courses"])
    
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

  

print("================ STUDENT ANALYSIS =================")

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

print("Average Marks :",count/total)

print()


print("Students Above 80: ")
for student in students:
    if student["marks"] >= 80:
        print(student["name"])

print()
print("Python Students:")
for student in students:
    if "Python" in student["courses"]:
        print(student["name"])

print()

print("Students Learning Both Python and Java:")
for student in students:
    if "Python" in student["courses"] and "Java" in student["courses"]:
        print(student["name"])

print()

print("Unique Coureses :\n",unique_sets)
print()
print("=====================================================")