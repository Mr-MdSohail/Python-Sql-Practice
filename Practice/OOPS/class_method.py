# class person:
#     name = "anonymous"
#     def change_name(self,name):
#         self.name = name
# p1 = person()
# p1.change_name("rahul")
# print(p1.name)
# print(person().name)
# here we can see even after cusing the change naem function the name is not changing , the change_name function is creating a new name , not changing the actual 'anonymous' name
# in this type of cases , we use the classmehtod

class person:
    name = "anonymous"
    @classmethod
    def change_name(cls,name):
        cls.name=name
p1 = person()
p1.change_name("rahul")
print(p1.name)
print(person().name)