# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        average = (self.m1 + self.m2 + self.m3) / 3
        print("Average is", average)    

s1 = student("rahul", 3, 3, 3)
s1.avg()
