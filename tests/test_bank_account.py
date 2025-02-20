import pytest
from bank_account.bank_account import BankAccount

def test_deposit():
    account = BankAccount("12345")
    account.deposit(100)
    assert account.balance == 100