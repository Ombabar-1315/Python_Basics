class Vehicle:
    registration_authority = "Maharashtra RTO"
    total_registered = 0

    def __init__(self, owner, vehicle_number, vehicle_type):
        self.owner = owner
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

        if Vehicle.validate_vehicle_number(vehicle_number):
            Vehicle.total_registered += 1

    @staticmethod
    def validate_vehicle_number(number):
        if len(number) == 4 and number[0:2].isalpha() and number[2:4].isdigit():
            return True
        else:
            return False

    @classmethod
    def change_authority(cls, registration_authority):
        cls.registration_authority = registration_authority

    @classmethod
    def show_total_registered(cls):
        return cls.total_registered

    def show_vehicle(self):
        print("Owner:", self.owner)
        print("Vehicle Number:", self.vehicle_number)
        print("Vehicle Type:", self.vehicle_type)
        print("Registration Authority:", self.registration_authority)

    def change_owner(self, name):
        self.owner = name


v1 = Vehicle("Om", "MH3", "Two Wheeler")
v2 = Vehicle("Rudra", "KA20", "Four Wheeler")

v1.show_vehicle()

print()

Vehicle.change_authority("Karnataka RTO")
v2.show_vehicle()

print()
print("Total Registered:", Vehicle.show_total_registered())