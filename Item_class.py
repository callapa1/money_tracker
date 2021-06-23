class Item():
    def __init__(self, title, amount, month):
        self.title = title
        self.month = month
        self.amount = amount
    def describe(self):
        print(f"{self.title}: {self.amount} kr, from month {self.month}")