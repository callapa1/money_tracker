from Account_class import Account
from functions import *

list = get_file()
file = list[0]
filename = list[1]
selection = 0

if file == '' and filename == '':
    account = Account()
else:
    account = process_file(file)

welcome_text()

while selection == 0:
    print(f"\nYou have currently {account.get_balance()} kr in your account.")

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
        save_quit(account, filename)
    elif selection == 5:
        break

print("Goodbye!")
