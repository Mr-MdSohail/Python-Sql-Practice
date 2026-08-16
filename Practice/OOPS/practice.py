# class car:
#     name="Mercedes"
#     model="K21"
#     field="SUV"
#     def info(self):
#         if self.field == "SUV":
#             print(f"{self.name} {self.model} is an {self.field} car")
#         else:
#             print(f"{self.name} {self.model} is a {self.field} car")

# a = car()
# a.name="Mahindra"
# a.model= "BE6"
# a.info()

# b = car()
# b.name = "Toyota"
# b.model = "Fortuner"
# b.info()

# c = car()
# c.name = "BYD"
# c.model= "J8"
# c.field= "Hatchback"
# c.info()

class student:
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
s1=student("Rahul",55)
s1.display()

class animal:
    def eat(self):
        print("Animal is eating")
    def bark(self):
        print("Animal is barking")
class dog(animal):
    def __init__(self,breed):
        self.breed=breed
a1 = dog("bulldog")
a1.eat()                
a1.bark()

print(type(6))