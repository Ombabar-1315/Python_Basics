def calculator():
    a = int(input("Enter Num A: "))
    b = int(input("Enter Num B: "))
    print("Addition: ",a+b)
    print("Substraction: ",a-b)
    print("Multiplication: ",a*b)
    print("Division: ",a/b)


try:
    calculator()
except ValueError:
    print("Enter A Valid Number: ")
except ZeroDivisionError:
    print("Number Cannot Divide By Zero: ")
else:
    print("No Exception")
finally:
    print("Program Excecuted: ")