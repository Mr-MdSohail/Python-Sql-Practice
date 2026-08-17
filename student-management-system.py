class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no=roll_no
        self.marks=marks
        while self.marks<0 or self.marks>600:
            print(f"For student {self.name}, Student total marks cannot be greater than 600")
            user_marks=int(input(f"Enter valid marks for {self.name}: "))
            self.marks=user_marks
            if 0<=self.marks<=600:
                break
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
    student('rahul',28,500),
    student('joy',26,250),
    student('elsa',20,6000)
]
while True:
    num=int(input("Which action you wanna perform?\n1. Add Student\n2. Remove Student\n3. Search Student\n4. Display All Students\n5. Exit\n"))
    if 1<=num<=5:
        if num == 1:
            print("Enter details of student you wanna add:")
            new_name=input("Enter student name: ")
            new_roll=int(input("Enter student roll number: "))
            new_marks=int(input("Enter student marks: "))
            new_student = student(new_name,new_roll,new_marks)
            students.append(new_student)
            print("Student added successfully!")
            for s in students:
                s.details()

        elif num ==2:
            remove_roll = int(input("Enter the roll number of student you wanna remove:"))
            found2 = False
            for s in students:
                if remove_roll==s.roll_no:
                    students.remove(s)
                    found2=True
                    print("student removed successfully")
                    for s in students:
                        s.details()
                    break
            if not found2:
                print("Student not found!")

        elif num==3:
            search_num=int(input(("Enter the roll number of student you wanna search for:\n")))
            found3=False
            for s in students:
                if search_num==s.roll_no:
                    print("Heres the details of student you searched for:")
                    s.details()
                    found3=True
                    break
            if not found3:
                print("Student not found!")

        elif num==4:
            for s in students:
                s.details()

        elif num==5:
            print("Program Ended.")
            break

    else:
        print("Please enter a valid action number")