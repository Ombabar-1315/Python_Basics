class ElectricityMeter:
    def __init__(self,consumer_name,units):
        self.consumer_name = consumer_name
        self.__units = units

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self,value):
        if value >= 0:
            self.__units = value
        else:
            print("Enter Valid units.")

    def calculate_bill(self):
      if self.__units <= 100:
        bill = self.__units * 5
        return bill

      elif self.__units <= 200:
         first_slab = 100 * 5
         remaining_units = self.__units - 100
         second_slab = remaining_units * 7

         return first_slab + second_slab
 
     
      else:
        first_slab = 100 * 5
        second_slab = 100 * 7
        remaining_units = self.__units - 200
        third_slab = remaining_units * 10

        return first_slab + second_slab + third_slab


m = ElectricityMeter("Om",10)



m.units = 150
print(m.units)
print(m.calculate_bill())


    
        
        