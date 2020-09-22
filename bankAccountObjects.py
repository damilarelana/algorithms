class BankAccount(object):
    def __init__(self, balance, depositAmount=0.0, withdrawalAmount=0.0):
        self.balance = int(balance)

    def deposit(self, depositAmount):
        self.balance += depositAmount

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.balance:
            return "invalid transaction"
        else:
            self.balance = self.balance - withdrawalAmount


class MinimumBalanceAccount(BankAccount):
    def __init__(self, newbalance, depositAmount=0.0, withdrawalAmount=0.0):
        self.balance = int(newbalance)