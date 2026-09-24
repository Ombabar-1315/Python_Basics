try:
    f = input("Enter File Name: ")

    with open(f,"r")as file:
        data = file.read()

except FileNotFoundError:
    print("File Not Found ")
else:
    print("File opened successfully.")
    print(data)
finally:
    print("Code Is Executed.")