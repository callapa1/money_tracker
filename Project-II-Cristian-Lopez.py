from Account_class import Account
from functions import *

file = get_file()
selection = 0

if file == '':
    account = Account()
else:
    account = process_file(file)

print("Welcome to TrackMoney")

while selection == 0:
    print(f"You have currently {account.get_balance()} kr on your account.")

    selection = get_main_selection()

    if selection == 1:
        show_select = show_function(account)
        selection = 0
    elif selection == 2:
        add_select = add_function(account)
        selection = 0
    elif selection == 3:
        edit_select = edit_function(account)
        selection = 0
    elif selection == 4:
        save_quit(account, file)
    elif selection == 5:
        break

print("Goodbye!")
