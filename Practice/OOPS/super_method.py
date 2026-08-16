class student:
    def __init__(self,name):
        self.name = name
    @staticmethod
    def student_pass():
        print("studnt has passed")
    @staticmethod
    def student_fail():
        print("studnt has failed")

class college_student(student):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.name=name
        self.rollno=rollno

s1 = college_student("45")
print(s1.rollno)
print(s1.student_pass())
print(s1.name)