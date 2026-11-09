import pytest
from src.main import BankAccount

@pytest.fixture(scope="function")
def sample_account():
    account = BankAccount(owner="Roman", balance=1000.0)
    yield account
    account.balance = 0