class Employee:

    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_employee(self):
        print("Employee Name: ",self.name)
        print("Employee Id: ",self.emp_id)



class Developer(Employee):

    def __init__(self, name, emp_id,Lang):
        super().__init__(name, emp_id)
        self.Lang = Lang

    def write_code(self):
        print(f"{self.name} is Writing {self.Lang} code.")



class Senior_Developer(Developer):

    def __init__(self, name, emp_id, Lang,experience):
        super().__init__(name, emp_id, Lang)
        self.experience = experience

    def show_employee(self):
        super().show_employee()
        print("Language: ",self.Lang)
        print("Experience: ",self.experience)

    def mentor(self):
        super().write_code()
        print("Om is mentoring junior developers.")


c = Senior_Developer("Om",101,"Python","5 Years")
c.show_employee()
c.mentor()
       

        