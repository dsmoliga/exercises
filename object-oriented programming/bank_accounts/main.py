from bank_account import BankAccount
from minbalance_account import MinimumBalanceAccount

account = BankAccount(500)
min_account = MinimumBalanceAccount(2000, 1500)
result = min_account.try_withdraw(200)

if result.is_ok():
    print(result.message)
else:
    print(result.message)
