class Bicycle:

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)

print("================================")
c1 = Bicycle("HP","h-201",450000)
c1.show_details()
print("-------------------------------")
c2 = Bicycle("PHP","p-301",500000)
c2.show_details()
print("================================")        


