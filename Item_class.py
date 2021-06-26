from Colors_class import colors

class Item():
    def __init__(self, title, amount, month):
        self.title = title
        self.month = month
        self.amount = amount

    def describe(self):
        if self.amount > 0:
            print(f"{self.title}: {colors.GREEN}+{self.amount:.2f}{colors.ENDC} kr, from month {self.month}")
        else:
            print(f"{self.title}: {colors.RED}{self.amount:.2f}{colors.ENDC} kr, from month {self.month}")