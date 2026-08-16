# class student:
#     def  __init__(self,marks1,marks2,marks3):
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#         self.percentage=(marks1+marks2+marks3)/3
# s1 = student(20,30,40)
# print(s1.percentage)
# s1.marks2 = 50
# print(s1.marks2)
# print(s1.percentage)
# so here we can see that the value of marks2 is changing but the percentage is not changing , because once the values are given,IT IS FIXED, so in this cases we use the property method TO CHANGE THE VALUES WITHIN THE PERCENTAGE FUNCTION


class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @property
    def percentage(self):
        return str((self.m1+self.m2+self.m3)/3)

s1 = student(20,30,40)
print(s1.percentage)
s1.m2=40
print(s1.percentage)
