class scooter:
    @staticmethod
    def start():
        print("scooter started")
    @staticmethod
    def stop():
        print("scooter stopped")

class honda(scooter):
    def __init__(self,name,model):
        self.name=name
        self.model=model
    @staticmethod
    def design():
        print("Activa's design")

class hero(honda):
    def __init__(self, name, model):
        self.name=name
        self.model=model

s1 = hero("pleasure","26")
print(s1.design())
print(s1.start())