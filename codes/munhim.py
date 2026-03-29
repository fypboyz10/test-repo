import random

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
            return True
        return False

    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            self.transactions.append(("transfer", amount, other.name))
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        if name not in self.accounts:
            self.accounts[name] = BankAccount(name, balance)

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)

    def withdraw(self, name, amount):
        if name in self.accounts:
            return self.accounts[name].withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            return self.accounts[from_acc].transfer(self.accounts[to_acc], amount)
        return False

    def total_balance(self):
        total = 0
        for acc in self.accounts.values():
            total += acc.get_balance()
        return total

    def apply_interest(self, rate):
        for acc in self.accounts.values():
            interest = acc.get_balance() * rate
            acc.deposit(interest)

    def random_transactions(self, n):
        names = list(self.accounts.keys())
        for _ in range(n):
            a = random.choice(names)
            b = random.choice(names)
            amount = random.randint(1, 100)
            if a != b:
                self.transfer(a, b, amount)
            else:
                if random.choice([True, False]):
                    self.deposit(a, amount)
                else:
                    self.withdraw(a, amount)


bank = BankSystem()
bank.create_account("Ali", 1000)
bank.create_account("Sara", 1500)
bank.create_account("Ahmed", 2000)

bank.random_transactions(20)
bank.apply_interest(0.05)

print("Total Balance:", bank.total_balance())

for name, acc in bank.accounts.items():
    print(name, acc.get_balance(), acc.get_transactions())
