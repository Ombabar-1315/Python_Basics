students = [
    {"name": "Om", "marks": 94},
    {"name": "Rahul", "marks": 72},
    {"name": "Priya", "marks": 88},
    {"name": "Amit", "marks": 31},
    {"name": "Sneha", "marks": 67}
]


def check_result(marks):
    if marks >= 35:
        return "Pass"

    else:
        return "Fail"

def find_highest(students):
    high = 0
    high_name = ""   

    for student in students:
        marks = student["marks"]
        name = student["name"]

        if marks > high:
            high = marks
            high_name = name 

    return high_name
    


def calculate_average(students):
    total = 0
   
    for student in students:
        total += student["marks"]

    avg = total/len(students)
    return avg 


def display_students(students):
    print("========= Student Report =============")
    for student in students:
        marks = student["marks"]
        name = student["name"]
        result = check_result(marks)

        print(name,"\t" ,marks ,"\t", result)

    high = find_highest(students)
    avg = calculate_average(students)
    print()
    print("Highest: ",high)
    print("Average: ",avg)
    print("===================================")

   






display_students(students)


     

    
