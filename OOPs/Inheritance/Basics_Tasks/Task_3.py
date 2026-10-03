class Hospital_Staff:

    def __init__(self,name,staff_id):
        self.name = name
        self.staff_id = staff_id

    def show_details(self):
        print("Name: ",self.name)
        print("Staff Id: ",self.staff_id)


class Doctor(Hospital_Staff):

    def __init__(self, name, staff_id,special):
        super().__init__(name, staff_id)
        self.special = special

    def show_details(self):
        super().show_details()
        print("Speallization: ",self.special)

    def treat_patient(self):
        print(f"{self.name} is treating patients.")

class Nurse(Hospital_Staff):

    def __init__(self, name, staff_id,shift):
        super().__init__(name, staff_id)
        self.shift = shift

    def show_details(self):
        super().show_details()
        print("Shift: ",self.shift)

    def assist_patient(self):
        print(f"{self.name} is assisting patients during {self.shift} shift.")

D = Doctor("Dr.om","H101","Orthopedic")

D.show_details()
D.treat_patient()

print()

S = Nurse("Priya","H102","Night")

S.show_details()
S.assist_patient()
    
        