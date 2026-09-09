students = [
      ["om", 92],
      ["Rahul", 35],
      ["Priya", 95],
      ["Aman", 28],
      ["Sneha", 78]
]

grade = ""
count = 0
pas = 0
fail = 0
high = students[0][1]
low = students[0][1]
total = 0
for student in students:
    count += 1
    if student[1] >= 35:
        grade = "pass"
    else:
        grade = "Fail"
    print()
    print(f"{student[0]} \t {student[1]} \t {grade}")


   

    if student[1] >= 35:
        pas += 1


    else:
        fail += 1

    if student[1] > high:
        high = student[1]

    if student[1] < low :
        low = student[1]

    if student [1] > 0:
        total += student[1]


print()
print("================= Student Report Card =================")
print()

print("Total Studnts     :",count)
print("\nPassed Students :",pas)

print("\nFailed Students :",fail)
print("\nHighest Marks   :",high)
print("\nLowest Marks    :",low)
print("\nAverage marks   :",total/count)

print()
print("=======================================================")
    
    
   


  

    



