# Create an Account class with 2 attributes- balance and account no.
# Create methods for debit, credit and printing the balance

class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Euro", amount, "Amount debited")
        print("Bank Balance = ", self.calc_balance())    

    def credit(self, amount):
        self.balance += amount
        print("Euro", amount, "Amount credited")  
        print("Bank Balance = ", self.calc_balance())      

    def calc_balance(self):
        return self.balance
       
account1 = Account(10000, 12345789)
account1.debit(1000)
account1.credit(500)