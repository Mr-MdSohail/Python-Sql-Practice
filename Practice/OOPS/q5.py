class order:
    def __init__(self,item,price):
        self.item = item
        self.price=price
    def __gt__(self,o2):
        return self.price>o2.price
o1= order("pencil",60)
o2 = order("pen",90)
print(o1>o2)