class Locker:
        def __init__(self,owner,locker_number,pin,balance):
            self.owner = owner
            self.locker_number = locker_number
            self.__pin = pin
            self.__balance = balance


        @property
        def balance(self):
            return self.__balance

        @balance.setter
        def balance(self,value):
            if value >= 0:
                self.__balance = value
            else:
                print("Balance cannot be negative.")

        def deposit(self,amount):
            if amount > 0:
                self.__balance += amount
            else:
                print("Invalid Amount.")
        
        def withdraw(self,amount):
            if amount <= 0:
                print("Amount Cannot be negative.")
            elif self.__balance >= amount:
                self.__balance -= amount
            else:
                print("Insufficient Balance.")

        def verify_pin(self,pin):
            if pin == self.__pin:
                return True
            else:
                return False
            
        def change_pin(self,old_pin,new_pin):
            if old_pin == self.__pin:
                if new_pin >= 0:
                    self.__pin = new_pin
                else:
                    print("Enter Valid Pin.")
            else:
                print("Old Pin Cannot Match! Please Try Again.")

        def show_locker(self):
            print("Owner: ",self.owner)
            print("Locker Number: ",self.locker_number)
            print("Balance: ",self.__balance)


locker = Locker("Om", 101, 1234, 5000)
locker.deposit(1000)
locker.show_locker()


print()
locker.withdraw(1000)
locker.show_locker()



    

        



