class TravelPass:
    agency = "CityRide"

    def __init__(self,name,type,balance):
        self.name = name
        self.type = type
        self.__balance = balance


    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value):
        if value >= 0:
            self.__balance = value
        else:
            print("Amount Cannot Be Negative.")

    def recharge(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Enter Valid Amount.")

    def travel(self,fare):
            if fare <= 0:
                print("Invalid Fare.")
            elif self.__balance >= fare:
              self.__balance -= fare
            else :
              print("insufficient balance.")
        
          

    def show_pass(self):
        print("Passanger Name =",self.name)
        print("Passanger Type =",self.type)
        print("Balance = ",self.balance)
        print("Agency = ",self.agency)

    @classmethod
    def change_agency(cls,agency):
        cls.agency = agency

    @staticmethod
    def is_valid_pass(type):
        if type == "Daily" or type == "Monthly"  or type == "Student":
            return True
        return False


t1 = TravelPass("Om","Daily",200)
t2 = TravelPass("Abhi","Monthly",1200)

t1.recharge(200)
t1.travel(-500)
t1.show_pass()

print(TravelPass.is_valid_pass("Daily"))
print()

TravelPass.change_agency("Rapido")
t2.show_pass()




        

