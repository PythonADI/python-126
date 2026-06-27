"""
A class that holds state and changes over time.

A BankAccount remembers its balance. Methods change that balance — and they
can refuse a bad request (you can't withdraw more than you have). This is
where classes shine: data + the rules that protect it, in one place.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance      # starts at 0 unless you say otherwise

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Cannot withdraw {amount} — only {self.balance} left.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")


account = BankAccount("nino", 100)
account.deposit(50)        # Balance: 150
account.withdraw(30)       # Balance: 120
account.withdraw(999)      # refused — only 120 left
print(account.balance)     # 120

# a second account is completely separate
giorgi = BankAccount("giorgi")   # balance defaults to 0
giorgi.deposit(10)               # Balance: 10
