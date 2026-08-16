# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
        print("Total balance:",self.balance)

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount ,"was debited from your account.")
        print("Total balance:",self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount ,"was credited to your account.")
        print("Total balance:",self.balance)

    def get_balance(self):
        return self.balance

acc1 = Account(1000,6767)
acc1.debit(100)
acc1.credit(500)
"hello origin"
