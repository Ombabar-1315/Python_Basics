class Delivery:

    company = "FastDrop"

    def __init__(self,customer,address,package):
        self.customer = customer
        self.address = address
        self.package = package

    def show_delivery(self):
        print("Customer Name: ",self.customer)
        print("Address : ",self.address)
        print("Package: ",self.package)
        print("Company Name:",self.company)


    @classmethod
    def change_Company(cls,company):
        cls.company = company

print("=========================================")
c1 = Delivery("Om","Solapur","Cycle")
c1.show_delivery()    
print("----------------------------")
c2 = Delivery("Rudra","Pune","Laptop")
c2.show_delivery()   


Delivery.change_Company("Amazon")
print()
c3 = Delivery("Om","Solapur","Cycle")
c3.show_delivery()    
print("----------------------------")
c4 = Delivery("Rudra","Pune","Laptop")
c4.show_delivery()   


