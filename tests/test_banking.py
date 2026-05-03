import pytest
from gh200.banking import BankAccount, InsufficientFundsError


def test_deposit():
    acc = BankAccount("Amit", 100)
    assert acc.deposit(50) == 150


def test_withdraw():
    acc = BankAccount("Amit", 100)
    assert acc.withdraw(40) == 60


def test_withdraw_insufficient_funds():
    acc = BankAccount("Amit", 50)

    with pytest.raises(InsufficientFundsError):
        acc.withdraw(100)


def test_deposit_invalid():
    acc = BankAccount("Amit")

    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_transfer():
    acc1 = BankAccount("Amit", 200)
    acc2 = BankAccount("Bob", 50)

    acc1.transfer(acc2, 100)

    assert acc1.balance == 100
    assert acc2.balance == 150
