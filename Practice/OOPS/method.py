class student:
    college_name = "AB College"
    def __init__(self,name):
        self.name = name

    def hello(self):
        print("Hello",self.name,"from",self.college_name)
    
    @staticmethod
    def hello():
        print("Hello")

s1 = student("Sohail")
s1.hello()

s2 = student("Rahul")
