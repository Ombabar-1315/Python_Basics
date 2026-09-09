employees = [
    {"name": "Om", "salary": 25000, "bonus": 5000},
    {"name": "Rahul", "salary": 30000, "bonus": 3000},
    {"name": "Priya", "salary": 28000, "bonus": 7000}
]

# function 1
def total_salary(salary,bonus):
    total = salary + bonus
    return total


#function 2
def calculate_tax(total):
    tax = 0
    if total >= 30000:
        tax = total * 0.10
    else:
        tax = total * 0.05
    return tax

# function 3
def final_salary(total,tax):
    exact_salary = total - tax
    return exact_salary


# function 4
def employee_report(employee):
    name = employee["name"]
    salary = employee["salary"]
    bonus = employee["bonus"]

    total = total_salary(salary,bonus)
    tax = calculate_tax(total)
    final = final_salary(total,tax)

    print("Name: ",name)
    print("Total Salary: ",total)
    print("Tax: ",tax)
    print("Final Salary: ",final)
    print()


for employee in employees:
    employee_report(employee)







