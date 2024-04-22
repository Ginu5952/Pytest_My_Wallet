import pytest
from wallet import Wallet,InsufficientAmount



def test_default_initial_amount(empty_wallet):
   
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):

    assert wallet.balance == 500

def test_wallet_add_cash(wallet):
   
    wallet.add_cash(200)  
    assert wallet.balance == 700

def test_wallet_spend_cash(wallet):
   
    wallet.spend_cash(100)  
    assert wallet.balance == 400


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
  
    
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(600)


@pytest.mark.parametrize(
    "add,spent,expected_balance",[
    (200,100,100),
    (1500,1000,500),
])
def test_transaction_history(my_wallet,add,spent,expected_balance):
    my_wallet.add_cash(add)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected_balance