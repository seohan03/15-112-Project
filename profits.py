class Profits():
    
    def __init__(self, moneyMade, moneySpent, peopleServed):
        self.made = moneyMade
        self.spent = moneySpent
        self.served = peopleServed
    
    def getNetProfit(self):
        return self.made - self.spent