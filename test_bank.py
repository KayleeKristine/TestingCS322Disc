# **Objective:** Write basic unit tests for the `Account` class's functionalities.  
# **Create a new file** named `test_bank.py` and implement basic tests. Include docstrings in your test cases.

import pytest
from bank import Account

def test_initial_balance():
    myAccount = Account('Makena', 100)
    assert myAccount.get_balance() == 100 

def test_deposit():
    myAccount = Account('Makena', 100)
    init_balance = Account.get_balance()
    myAccount.deposit(10)
    assert myAccount.get_balance() == init_balance + 10

def test_withdraw():
    myAccount = Account('Makena', 100)
    init_balance = myAccount.get_balance()
    myAccount.withdraw(10)
    assert myAccount.get_balance() == init_balance - 10
"""
# **Objective:** Test exception handling for the `deposit` and `withdraw` methods. Feel free to google for examples on how to test for exceptions.
# **Extend `test_bank.py`** to include tests for wrong inputs. Include docstrings in your test cases.

def test_deposit_negative_amount():
    # TODO

def test_withdraw_more_than_balance():
    # TODO

def test_withdraw_negative_amount():
    # TODO
"""