class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no=roll_no
        self.marks=marks
    def details(self):
        print("Name:",self.name)
        print("Roll number:",self.roll_no)
        print("Marks (out of 600):",self.marks)
    def cal_percentage(self):
        percentage = self.marks/6
        return percentage
    def pass_fail(self):
        if self.cal_percentage()>30:
            print(f"{self.name} has passed!")
        else:
            print(f"{self.name} has failed")
    def grade(self):
        percentage = self.marks/6
        if percentage>=90:
            print("Grade A")
        elif percentage>=75:
            print("Grade B")
        elif percentage>=60:
            print("Grade C")
        elif percentage>=40:
            print("Grade D")
        else:
            print("Grade F")
students = [
    student('rohan',23,300),
    student('mohan',24,400),
    student('rahul',24,500),
    student('joy',24,250),
    student('elsa',24,600)
]
for s in students:
    s.details()
    percentage = s.cal_percentage()
    print(s.name, percentage)
    s.pass_fail()
    s.grade()
    print("")
topper = students[0]
for s in students:
    if s.marks>topper.marks:
        topper=s
print("Topper Details: ")
topper.details()    