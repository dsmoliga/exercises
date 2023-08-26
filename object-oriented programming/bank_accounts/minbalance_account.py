from result import Error
from bank_account import BankAccount


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=1000):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def try_withdraw(self, amount):
        if self.balance - amount > self.minimum_balance:
            return super().try_withdraw(amount)
        else:
            return Error(f"You have to maintain at least {self.minimum_balance}", amount)
