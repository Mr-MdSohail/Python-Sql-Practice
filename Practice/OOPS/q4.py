class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print(self.role, self.dept, self.salary)

e1=employee("web developer","IT",445000)
e1.showDetails()

class engineer(employee):
    def __init__(self, name,age,role,dept,salary):
        super().__init__(role,dept,salary)
        self.role=role
        self.dept=dept
        self.salary=salary
        self.name=name
        self.age=age

person = engineer("rahul",33,"designer","IT",9999)
print(person.name,person.age)
person.showDetails()