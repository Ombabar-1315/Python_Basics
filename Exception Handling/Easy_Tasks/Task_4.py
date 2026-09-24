class invalidAge(Exception):
    pass

try:
    age = int(input("Enter Age: "))
    if age <= 0:
        raise invalidAge("Age Cannot be Zero Or Negative.")
    
    if age > 120:
        raise ValueError("❌ Invalid age.")



except invalidAge as e:
    print(e)

except ValueError as e:
    print(e)
else:
    print(age)