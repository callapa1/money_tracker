class Account:
    def __init__(self):
        self.history = []
        self.balance = 0

    def get_balance(self):
        self.balance = 0
        for item in self.history:
            self.balance += item.amount
        return self.balance

    def add_item(self, item):
        self.history.append(item)

    def full_show(self):
        i = 1
        for item in self.history:
            print(i, end =" ")
            item.describe()
            i += 1

    def show_by_title(self):
        items = sorted(self.history, key=lambda item: item.title)
        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_amount(self):
        items = sorted(self.history, key=lambda item: item.amount)
        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_month(self):
        items = sorted(self.history, key=lambda item: item.month)
        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_title_r(self):
        items = sorted(self.history, key=lambda item: item.title)[::-1]
        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_amount_r(self):
        items = sorted(self.history, key=lambda item: item.amount)[::-1]
        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_month_r(self):
        items = sorted(self.history, key=lambda item: item.month)[::-1]
        for item in items:
            print("-", end=" ")
            item.describe()
