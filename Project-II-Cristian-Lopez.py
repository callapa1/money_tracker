from Account_class import Account
from functions import *

file = get_file()

if file == '':
    account = Account()
else:
    process_file(file)
    account = 0

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