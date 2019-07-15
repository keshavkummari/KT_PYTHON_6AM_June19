class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

    def deposit(self,amount):
        self.balance += amount 
        return self.balance

a = BankAccount()
print(a.deposit(100))

b = BankAccount()
print(b.withdraw(50))
print(b.withdraw(30))
print(b.withdraw(20))
