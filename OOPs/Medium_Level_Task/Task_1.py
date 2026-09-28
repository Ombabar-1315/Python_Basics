class ParkingMeter:
    def __init__(self,vechicle_number,hours,rate_per_hour):
        self.vechicle_number = vechicle_number
        self.hours = hours
        self.rate_per_hour = rate_per_hour


    def calculate_cost(self):
        total = self.hours*self.rate_per_hour
        return total

    def extend_parking(self,Extra):
        self.hours += Extra
       

        
      

    def show_receipt(self):
        print("Vechicle Number: ",self.vechicle_number)
        print("Total Hours: ",self.hours )
        print("Rate Per Hour: ",self.rate_per_hour)
        print("Final Cost: ",self.calculate_cost())


p1 = ParkingMeter(101,2,100)

p1.extend_parking(3)
p1.show_receipt()

    
        