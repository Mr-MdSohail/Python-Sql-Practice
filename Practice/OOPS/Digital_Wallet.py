class Digital_Wallet:
    def __init__(self,user):
         self.user=user
         self.balance=0
         self.transactions = []
    def make_payment(self,amount):
            if self.balance>=amount:
                self.balance -= amount
                print("\nRs."+str(amount)+" was debited from your wallet.")
                print("Total balance:",self.balance)
                self.transactions.append("-"+str(amount)+" : "+"Rs."+str(amount)+" was debited")
            else:
                 print("\nInsufficient balance!")
    def add_money(self,amount):
        self.balance += amount
        print("\nRs."+str(amount)+" was added to your wallet.")
        print("Total balance:",self.balance)
        self.transactions.append("+"+str(amount)+" : "+"Rs."+str(amount)+" was added")
    def Transaction_history(self):
         print("\nTransaction history:")
         for i in self.transactions:
              print(i)
wall=Digital_Wallet('sohail')
wall.add_money(100)
wall.make_payment(10)
wall.make_payment(90)
wall.Transaction_history()