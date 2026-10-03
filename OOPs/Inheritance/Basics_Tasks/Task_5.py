class User:

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def show_profile(self):
        print("Name: ",self.name)
        print("Email: ",self.email)


class Student(User):

    def __init__(self, name, email,course):
        super().__init__(name, email)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")

    def show_profile(self):
         super().show_profile()
         print("Couse: ",self.course)


class Instructor(User):

    def __init__(self, name, email,subject):
        super().__init__(name, email)
        self.subject = subject


    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

    def show_profile(self):
         
         super().show_profile()
         print("Subject: ",self.subject)


class PremiumStudent(Student):

    def __init__(self, name, email, course,subscription):
        super().__init__(name, email, course)
        self.subscription = subscription

    def show_profile(self):
         super().show_profile()
         print("Subscription: ",self.subscription)

    def access_premium(self):
        super().study()
        print(f"{self.name} has acceess to {self.subscription} content.")


p = PremiumStudent("Om","Om@gamil","Python","Premium")
p.show_profile()
p.access_premium()

print()

I = Instructor("Patil","sir@gmail","Java")
I.show_profile()
I.teach()

        