import dice
import player

name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))

player = player.create_player(
    name = name,
    age = age
)



print("=================================")
print("\t 🎲 DICE BATTLE ")
print("=================================")

print("Player Name:",player["name"])
print("Age :",player["age"])

print()

print("Rolling Dice...........")

print()

player_dice = dice.roll_dice()
computer_dice = dice.roll_dice()

print(f"{name}'s Dice :",player_dice)
print("Computer's Dice :",computer_dice)
print()

result = ""
player_score = player_dice
computer_score = computer_dice

if player_score > computer_score:
    result = f"{name} wins!"

elif player_score == computer_score:
    result = "It's a Draw!" 

else:
    result = "Computer Wins!"



print("---------------------------")
print(result)
print("---------------------------")    