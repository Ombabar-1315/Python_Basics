class DigitalWallet:

    def __init__(self,owner,balance,currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency


    def add_money(self,amount):
        if amount <= 0:
            print("Enter Valid Amount.")
        else:
            self.balance += amount
        print("Balance Increases")
        print("Balance :",self.balance)

    def spend_money(self,amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Balance .")
            return
        print("Balance Decreases.")
        print("Balnce :",self.balance)


    def show_balance(self):
        print("Current Balance: ",self.balance)




customer = DigitalWallet("om",20000,"INR")
customer.show_balance()
print("-------------------------------")
customer.add_money(500)
print("-------------------------------")
customer.spend_money(20600)
print("--------------------------------")
customer.add_money(-5)





        

