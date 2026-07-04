class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount < 0 or self.balance < amount:
            print("check amount!")
        else:
            self.balance -= amount
        

    def __str__(self):
        return self.owner

    def __repr__(self):
        return f"{self.owner} has {self.balance}$"
    
    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance
        


acc = Account("nino")
accs = [Account("Nika"), Account("Mary")]

acc.withdraw(-1000)

print(acc.balance)

print(acc)
print(accs)
accs[0].deposit(100)

print(accs[0] > accs[1])