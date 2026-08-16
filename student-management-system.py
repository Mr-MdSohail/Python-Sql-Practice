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
        print(f"Percentage: {percentage}%")
        return percentage
    def pass_fail(self):
        percentage = self.marks/6
        if percentage>30:
            print(f"{self.name} has passed!")
        else:
            print(f"{self.name} has failed")
students = [
    student('rohan',23,300),
    student('mohan',24,400),
    student('rahul',24,500),
    student('joy',24,250),
    student('elsa',24,600)
]
for s in students:
    s.details()
    print("")
topper = students[0]
for s in students:
    if s.marks>topper.marks:
        topper=s
topper.details()