import pytest
from wallet import Wallet,InsufficientAmount

@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(500)

@pytest.fixture
def my_wallet():
    return Wallet()