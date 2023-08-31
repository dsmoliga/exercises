from unittest import TestCase
from parameterized import parameterized, parameterized_class
from minbalance_account import MinimumBalanceAccount


class TestMinimumBalanceAccount(TestCase):
    # TODO - ADD TEST FOR TYPEERROR
    @parameterized.expand([
        ('Min balance zero', 0, 0),
        ('Min balance negative', -1000, 1000),
        ('Min balance fraction', 4004.4, 4004.4)
    ])
    def test_minimum_balance_account(self, name, input, expected):
        my_balance = MinimumBalanceAccount(minimum_balance=input)
        self.assertEqual(my_balance.minimum_balance, expected)

    @parameterized.expand([
        ('Balance equal min_balance', 1000, 1000),
        ('Balance lower min_balance', 900, 900)
    ])
    def test_minimum_balance_account_with_balance(self, name, input, expected):
        my_balance = MinimumBalanceAccount(input)
        self.assertEqual(my_balance.balance, expected)
