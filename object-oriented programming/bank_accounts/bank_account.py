from result import Ok, Error


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return Ok("Withdraw was success", amount)
        return Error("Failed to withdraw", amount)

    def __str__(self):
        return str(self.balance)
