import pytest
from src.bank_account import BankAccount

def test_default_balance_is_zero():
    account = BankAccount()
    assert account.get_balance() == 0

def test_initial_balance_set_correctly():
    account = BankAccount(250)
    assert account.get_balance() == 250

def test_negative_initial_balance_raises_error():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-50)

def test_deposit_adds_money():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

def test_deposit_zero_or_negative_raises_error():
    account = BankAccount()
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(0)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(-20)

def test_withdraw_decreases_balance():
    account = BankAccount(200)
    account.withdraw(50)
    assert account.get_balance() == 150

def test_withdraw_invalid_amount_raises_error():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(-10)

def test_withdraw_insufficient_funds_raises_error():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)