class car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("car stopped")

class byd(car):
    def __init__(self,name):
        self.name = name

car1 = byd("supra")
print(car1.name)
car1.start()