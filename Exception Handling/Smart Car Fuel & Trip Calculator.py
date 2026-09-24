car = {
    "model": "Swift",
    "fuel": 20,
    "mileage": 18
}

def calculate_trip(distance,mileage,fuel):
    if distance <= 0:
     raise ValueError("Distance must be greater than 0")
    fuel_required = distance / mileage

    if fuel >= fuel_required:
       Remaining_fuel =  fuel - fuel_required
       
       


try:
    distance = int(input("Enter Distance: "))



except:
   print("Invalid distance. Please enter a number.")

except ValueError as e:
   print(e)


