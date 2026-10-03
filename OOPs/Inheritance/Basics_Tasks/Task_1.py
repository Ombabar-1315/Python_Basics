class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def show_vehicle(self):
        print("Vehicle Brand: ",self.brand)
        print("Vehicle Model: ",self.model)

    def start(self):
        print("Vehicle is starting.....")


class Car(Vehicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def show_car(self):
        print("Vehicle Brand: ",self.brand)
        print("Vehicle Model: ",self.model)
        print("Vehicle Fuel Type: ",self.fuel_type)

    def drive(self):
        super().start()
        print("Car is ready to drive....")
        print("Car Is Driving.")


c = Car("Tata","Safari","Diesel")
c.show_car()
c.drive()
        
        