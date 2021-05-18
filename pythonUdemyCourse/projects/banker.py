class BankOfPython:

    def __init__(self, owner: str, opening_balance: float = 0):
        self.owner = owner
        self.balance = opening_balance

    def deposit(self, amount):
        if amount < 0:
            print('Deposit Failed. Enter positive value.')
            return self.balance
        self.balance += amount
        print('Deposit Successful.')
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('Withdrawal Failed. Insufficient Funds.')
        else:
            self.balance -= amount
            print('Withdrawal Successful.')
        return self.balance

    def __str__(self):
        return f'Account Owner : \t {self.owner} \nAccount Balance : \t {self.balance}'


acc1 = BankOfPython('Aditya', 200)
print(acc1)

print(acc1.balance)
print(acc1.deposit(5000))
print(acc1.withdraw(4000))
print(acc1.withdraw(4000))
