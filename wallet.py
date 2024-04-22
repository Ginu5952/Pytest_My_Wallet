class InsufficientAmount(Exception):
    pass


class Wallet():
    def __init__(self,initial_amount=0) :
        self.balance = initial_amount

    def spend_cash(self,cash_spend):
        if self.balance < cash_spend:
            raise InsufficientAmount('Not enough available to spend {}'.format(cash_spend))
        else:
            self.balance -= cash_spend

    def add_cash(self,cash_add):
        self.balance += cash_add