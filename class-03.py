class TaipeiBank:
    def __init__(self, balance=0):
        self.balance = balance
    def printBalance(self):
        print(f'Balance: {self.balance}')
tb = TaipeiBank(1000)
tb.printBalance()
