class SavingAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def check_balance(self):
        return self.balance

account = SavingAccount(100)
print(f"Initial Balance: {account.check_balance()}")
print(f"Balance after deposit of 50: {account.deposit(50)}")
try:
    account.withdraw(200)
except ValueError as e:
    print(e)
print(f"Balance after withdrawal of 30: {account.withdraw(30)}")