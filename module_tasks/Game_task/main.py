import game 



print("========================")
print(" 🎮 LUCKY NUMBER GAME ")
print("=========================")

name = input("Enter your name: ")

print(f"Hello {name}!")
num = game.generate_lucky_number()
print("Your Lucky Number is: ",num)

if num % 2 == 0:
    print(num,"is Even ")
else:
    print(num,"is Odd")

print()

print("🍀 Today looks lucky!")
