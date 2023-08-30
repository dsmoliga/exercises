from unittest import TestCase
from bank_account import BankAccount

class TestBankAccount(TestCase):
    def test_balance_with_letters(self):
        my_balance = BankAccount('abcdefg')
        with self.assertRaises(TypeError):
            result = my_balance
