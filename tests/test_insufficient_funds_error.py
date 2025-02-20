import pytest
from bank_account.bank_account import BankAccount

def test_insufficient_funds_error():
    account = BankAccount("12345")
    with pytest.raises(ValueError):
        account.withdraw(100)