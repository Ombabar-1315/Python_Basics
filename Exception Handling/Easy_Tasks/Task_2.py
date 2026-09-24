
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

try:
    index = int(input("Enter Index Number: "))
    print("Fruit: ",fruits[index])

except IndexError:
    print("❌ Invalid index. Fruit does not exist.")
