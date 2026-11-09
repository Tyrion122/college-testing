import pytest
from src.main import BankAccount

def test_account_creation():
    acc = BankAccount("Олена", 500.0)
    assert acc.get_balance() == 500.0
    assert acc.owner == "Олена"

@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (100.0, 1100.0),
    (500.0, 1500.0),
    (50.5, 1050.5)
])
def test_deposit(sample_account, deposit_amount, expected_balance):
    sample_account.deposit(deposit_amount)
    assert sample_account.get_balance() == expected_balance

def test_withdraw(sample_account):
    sample_account.withdraw(200.0)
    assert sample_account.get_balance() == 800.0

def test_add_interest(sample_account):
    sample_account.add_interest(10) 
    assert sample_account.get_balance() == 1100.0

def test_withdraw_insufficient_funds(sample_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        sample_account.withdraw(2000.0)

def test_deposit_invalid_type(sample_account):
    with pytest.raises(TypeError, match="Deposit amount must be a number"):
        sample_account.deposit("сто")

@pytest.mark.skip(reason="Функція переказу на інший рахунок ще в розробці")
def test_transfer_funds():
    assert False