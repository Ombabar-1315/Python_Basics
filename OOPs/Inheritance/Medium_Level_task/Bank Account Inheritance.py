class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Deposit Amount.")

            
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount.! Enter Valid Amount")
        elif amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance.")

    def show_Balance(self):
        print("Account Holder: ",self.account_holder)
        print("Account Number: ",self.account_number)
        print("Balance: ",self.balance)


class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance,interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate


    def calculate_interest(self):
        interest = 0
        if self.interest_rate > 0:
           interest = self.balance * self.interest_rate / 100
           return interest
        else:
            print("Enter Valid Interst Rate")
            return 0 

    def show_Balance(self):
        super().show_Balance()
        print("Interest Rate: ",self.interest_rate)
        print("Interest: ",self.calculate_interest())



class CurrentAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance,minimum_balance):
        super().__init__(account_number, account_holder, balance)
        self.minimum_balance = minimum_balance


    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a Valid Withdrawel Amount.")
        elif self.balance - amount < self.minimum_balance:
            print("Withdrawal denied.")
            print("Minimum balance must be maintained.")
        else:
            super().withdraw(amount)

    def show_Balance(self):
         super().show_Balance()
         print("Minimum Balance: ",self.minimum_balance)

print("======= Saving Account ===========")
S = SavingsAccount("SBI101","OM",10000,7)
S.show_Balance()
print()
C = CurrentAccount("SBI102","RUDRA",5000,2000)
C.withdraw(2000)
C.show_Balance()


        



