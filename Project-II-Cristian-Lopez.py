from Account_class import Account
from functions import *

account = Account()

file = get_file()
# item1 = Item('renta', -3500, 1)
# item2 = Item('arenta', -1600, 6)
# item3 = Item('salario', 40500, 3)
# account.add_item(item1)
# account.add_item(item2)
# account.add_item(item3)

print("Welcome to TrackMoney")
print(f"You have currently {account.get_balance()} kr on your account.")

selection = get_main_selection()

if selection == 1:
    show_select = show_function(account)
elif selection == 2:
    add_select = add_function(account)
elif selection == 3:
    edit_select = edit_function(account)
elif selection == 4:
    save_quit(account, file)
print("\n", selection, " end")