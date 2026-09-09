
secrete = 5

while True:
    num = int(input("Enter a number: "))
    if num == secrete:
        print("Congratulations! You've guessed the secret number.")
        break
    elif num < secrete:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")   

    print ("Guess Again")

