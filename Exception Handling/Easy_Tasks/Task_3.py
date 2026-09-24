person = {
    "name": "Om",
    "age": 20,
    "city": "Solapur",
    "course": "Computer Engineering"
}


try:
    info = input("Enter Information to display: ")
    if info in person:
        print(person[info])
    else:
        raise KeyError("❌ This information is not available.")
        

except KeyError as e:
    print(e)