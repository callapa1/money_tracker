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

    def show_by_title(self, selection):
        # 1 = ALL, 2 = EXPENSES, 3 = INCOME
        items = sorted(self.history, key=lambda item: item.title)
        if selection == 2:
            items = filter(lambda item: item.amount < 0, items)
        elif selection == 3:
            items = filter(lambda item: item.amount > 0, items)

        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_amount(self, selection):
        items = sorted(self.history, key=lambda item: item.amount)
        if selection == 2:
            items = filter(lambda item: item.amount < 0, items)
        elif selection == 3:
            items = filter(lambda item: item.amount > 0, items)

        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_month(self, selection):
        items = sorted(self.history, key=lambda item: item.month)
        if selection == 2:
            items = filter(lambda item: item.amount < 0, items)
        elif selection == 3:
            items = filter(lambda item: item.amount > 0, items)

        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_title_r(self, selection):
        items = sorted(self.history, key=lambda item: item.title)[::-1]
        if selection == 2:
            items = filter(lambda item: item.amount < 0, items)
        elif selection == 3:
            items = filter(lambda item: item.amount > 0, items)

        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_amount_r(self, selection):
        items = sorted(self.history, key=lambda item: item.amount)[::-1]
        if selection == 2:
            items = filter(lambda item: item.amount < 0, items)
        elif selection == 3:
            items = filter(lambda item: item.amount > 0, items)

        for item in items:
            print("-", end=" ")
            item.describe()

    def show_by_month_r(self, selection):
        items = sorted(self.history, key=lambda item: item.month)[::-1]
        if selection == 2:
            items = filter(lambda item: item.amount < 0, items)
        elif selection == 3:
            items = filter(lambda item: item.amount > 0, items)

        for item in items:
            print("-", end=" ")
            item.describe()
