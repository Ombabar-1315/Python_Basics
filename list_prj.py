marks = [45, 78, 32, 90, 65, 28, 88]

print("=============================")
print("Total Students :",len(marks))
print("Original Marks :")
print(marks)

print()

passed = [ i for i in marks if i > 35]

failed = [ j for j in marks if j < 35 ]

above = [ k for k in marks if k > 80]

square = [ a * a for a in marks if a > 80]

print("Passing Marks :")
print(passed)

print("----------------------------------")

print("Failed Marks  :")
print(failed)

print("----------------------------------")

print("Marks Above 80 :")
print(above)

print("----------------------------------")

print("Square Of Above 80 :")
print(square)

print("===================================")