class adult:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def AgeChecker(self):
        if self.age >= 18:
            print("You are eligible.")
        


class minor(adult):

    def AgeChecker(self):
        super().AgeChecker()
        if self.age < 18:
            print("Your Not Eligible")


m = minor("om",19)
m.AgeChecker()
        