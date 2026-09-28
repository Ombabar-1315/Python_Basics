class SmartLight:
    def __init__(self,brand,brightness,is_on):
        self.brand = brand
        self.brightness = brightness
        self.is_on = is_on

    def turn_of(self):
       if self.is_on == True:
           return "ON"
       
    def turn_off(self):
        if self.is_on == False:
            return "OFF"
      

    def incrases_brightness(self,amount):
        if amount >= 100:
            print("Brightness Cannot Be Exceed 100 .")
            return
        else:
            self.brightness += amount

    def decreses_brightness(self,amount):
        if amount <= 0:
            print("Brightness Cannot Be Low .")
            return
        else:
            self.brightness -= amount

    def Show_Status(self):
        print("Brance: ",self.brand)
        print("Power: ",self.is_on)
        print("BrightnessL ",self.brightness)


light = SmartLight("Phillips",50,True)


light.Show_Status()
light.turn_of()
light.Show_Status()
print()

light.incrases_brightness(30)

light.Show_Status




        
    