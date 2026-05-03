class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than 0")

        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance")

        self.balance -= amount
        return self.balance

    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)
        return self.balance
