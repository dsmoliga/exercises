from unittest import TestCase
from parameterized import parameterized, parameterized_class
from bank_account import BankAccount


class TestBankAccount(TestCase):
    # GIVEN
    def test_balance_with_letters(self):
        my_balance = BankAccount('Test')
        with self.assertRaises(TypeError):
            result = my_balance

    @parameterized.expand([
        ('Default', None, 0),
        ('Letters', 'test', 0),
        ('Negative', -10, 0),
        ('Fraction', 0.5, 0.5)
    ])
    def test_balance_of_bank_account(self, name, input, expected):
        my_balance = BankAccount(input)
        self.assertEqual(my_balance.balance, expected)

    # WHEN
    @parameterized.expand([
        ('Letters', 'test', 500),
        ('Negative', -10, 500),
        ('Fraction', 0.3, 500.3),
        ('Zero', 0, 500)
    ])
    def test_deposit(self, name, input, expected):
        my_balance = BankAccount(500)
        my_balance.deposit(input)
        self.assertEqual(my_balance.balance, expected)

    @parameterized.expand([
        ('Letters', 'test', 500),
        ('Negative', -10, 500),
        ('Fraction', 0.3, 499.7),
        ('Zero', 0, 500),
        ('Higher than balance', 600, 500)
    ])
    def test_withdraw(self, name, input, expected):
        my_balance = BankAccount(500)
        my_balance.try_withdraw(input)
        self.assertEqual(my_balance.balance, expected)
