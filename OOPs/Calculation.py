class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = sum(self.marks)
        avg = total / len(self.marks)

        return avg



stud1 = Student("Om",[85,90,95])

stud= stud1.average()
print(stud)

        