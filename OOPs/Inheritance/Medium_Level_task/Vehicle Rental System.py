class Vehicle:

    def __init__(self, brand, model, rent_per_day):
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rent Per Day:", self.rent_per_day)

    def calculate_rent(self, days):
        if days > 0:
            rent = self.rent_per_day * days
            return rent
        else:
            print("Enter Valid Days.")
            return 0


class Car(Vehicle):

    def __init__(self, brand, model, rent_per_day, number_of_seats):
        super().__init__(brand, model, rent_per_day)
        self.number_of_seats = number_of_seats

    def show_details(self):
        super().show_details()
        print("Seats:", self.number_of_seats)


class Bike(Vehicle):

    def __init__(self, brand, model, rent_per_day, engine_cc):
        super().__init__(brand, model, rent_per_day)
        self.engine_cc = engine_cc

    def show_details(self):
        super().show_details()
        print("Engine CC:", self.engine_cc)


class Truck(Vehicle):

    def __init__(self, brand, model, rent_per_day, load_capacity):
        super().__init__(brand, model, rent_per_day)
        self.load_capacity = load_capacity

    def show_details(self):
        super().show_details()
        print("Load Capacity:", self.load_capacity)


# Car
C = Car("Tata", "Safari", 3000, 7)

print("========== CAR ==========")
C.show_details()

days = 4
total = C.calculate_rent(days)

print("Rental Days:", days)
print("Total Rent:", total)


print()

# Bike
B = Bike("Kawasaki", "H2R", 2000, "600CC")

print("========== BIKE ==========")
B.show_details()

days = 2
total = B.calculate_rent(days)

print("Rental Days:", days)
print("Total Rent:", total)


print()

# Truck
T = Truck("Volvo", "V-HR", 7000, "4 Ton")

print("========== TRUCK ==========")
T.show_details()

days = 5
total = T.calculate_rent(days)

print("Rental Days:", days)
print("Total Rent:", total)