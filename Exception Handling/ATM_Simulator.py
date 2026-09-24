balance = 10000
correct_pin = 1234

class Insufficientbalance(Exception):
    pass

class InvalidPin(Exception):
    pass

try:
    pin = int(input("Enter a Pin: "))
    amount = int(input("Enter amount: "))

    if pin != correct_pin:
        raise InvalidPin("Incorrect Pin")
    
    if amount <= 0:
        raise Insufficientbalance("Insufficient Balance: ")
    



except ValueError:
    print("Invalid amount. Please enter numbers only. ")

except InvalidPin as i:
    print(i)

except Insufficientbalance as b:
    print(b)

else:
    balance = balance - amount
    print("Transaction Successful \nRemaining Balance: ",balance)

finally:
    print("Transcation Completed.")


