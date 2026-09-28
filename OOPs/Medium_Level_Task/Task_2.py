class Course:
    platform = "LearnHub"

    def __init__(self,couse_name,instructor,fee,enrolled_students = 0):
        self.course_name = couse_name
        self.instructor = instructor
        self.fee = fee
        self.enrolled_students = enrolled_students

    def enroll(self):
        self.enrolled_students += 1

    def cancel_enroll(self):
        if self.enrolled_students > 0:
                self.enrolled_students -= 1
        else:
            print("No enrolled students to cancel.")
        
       

    def show_course(self):
        print("Course Name: ",self.course_name)
        print("Instructor: ",self.instructor)
        print("Fee Structure: ",self.fee)
        print("Enrolled Student: ",self.enrolled_students)
        print("Platform Name: ",self.platform)

    @classmethod
    def change_platform(cls,platform):
        cls.platform = platform

s1 = Course("CPP", "KK Sir", 4000, 2)

s2 = Course("Java", "RK Sir", 3500)
s2.enroll()


print("=========================")
s1.show_course()

print("-------------------------")
s2.show_course()


Course.change_platform("ApnaCollege")

s2.cancel_enroll()
s2.cancel_enroll()

print("=========================")
s1.show_course()

print("-------------------------")
s2.show_course()
