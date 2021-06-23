from Account_class import Account
import json
from Colors_class import colors
from Item_class import Item

# -1 GET FILE
def get_file():
    file = ""
    selection = -1
    options = [1,2]
    filename = 0
    txt_options = ['Enter 1 to open a file',
                   'Enter 2 to create a new file']

    while selection not in options:
        for txt in txt_options:
            print(txt)
        try:
            selection = int(input("·"))
            assert selection in options
        except ValueError:
            print("Enter a valid input")
        except AssertionError:
            print("Selection not valid")

    if selection == 1:
        while filename == 0:
            filename = input("Enter your txt file name: ")
            try:
                file = open(f"{filename}.txt", "r")
            except FileNotFoundError:
                print("File not found")
                filename = 0
        string = file.read()
        file.close()

        return [string, filename]

    elif selection == 2:
        return ''

def process_file(file):
    file = eval(file)
    history = file['history']
    balance = file['balance']

    account = Account()
    account.balance = balance

    for item in history:
        entry = Item(
            item['title'],
            item['amount'],
            item['month']
        )
        account.history.append(entry)
    return account

# 0
def get_main_selection():
    selection = -1
    txt_options = ["Pick an option:",
               f"({colors.VIOLET}1{colors.ENDC}) Show items (All{colors.BLUE}/{colors.ENDC}Expense(s){colors.BLUE}/{colors.ENDC}Income(s))",
               f"({colors.VIOLET}2{colors.ENDC}) Add New Expense{colors.BLUE}/{colors.ENDC}Income",
               f"({colors.VIOLET}3{colors.ENDC}) Edit Item (edit, remove)",
               f"({colors.VIOLET}4{colors.ENDC}) {colors.BOLD}Save{colors.ENDC} and Quit",
               f"({colors.RED}5{colors.ENDC}) Quit without saving"
              ]
    options = [x+1 for x in range(len(txt_options))]

    while selection not in options:
        for txt in txt_options:
            print(txt)
        try:
            selection = int(input("·"))
            assert selection in options
        except ValueError:
            print("Enter a valid input")
        except AssertionError:
            print("Selection not valid")

    return selection

# 1 SHOW
def show_function(account):
    selection = -1
    options = {1:'All', 2:'Expense(s)', 3:'Income(s)'}
    txt_options = ["Pick an option:",
                f"({colors.VIOLET}1{colors.ENDC}) Show All (BY Title{colors.BLUE}/{colors.ENDC}Amount{colors.BLUE}/{colors.ENDC}Month)",
                f"({colors.VIOLET}2{colors.ENDC}) Show Expense(s) (BY Title{colors.BLUE}/{colors.ENDC}Amount{colors.BLUE}/{colors.ENDC}Month)",
                f"({colors.VIOLET}3{colors.ENDC}) Show Income(s) (BY Title{colors.BLUE}/{colors.ENDC}Amount{colors.BLUE}/{colors.ENDC}Month)"
                # f"({colors.VIOLET}4{colors.ENDC}) Back"
              ]

    while selection not in options.keys():
        for txt in txt_options:
            print(txt)
        try:
            selection = int(input("·"))
            assert selection in options.keys()
        except ValueError:
            print("Enter a valid input")
        except AssertionError:
            print("Selection not valid")

    # Specify by title, amount or month
    print(f"Show {options[selection]}:")
    show_select = show_by()

    if show_select == 1:
        account.show_by_title()
    elif show_select == 2:
        account.show_by_amount()
    elif show_select == 3:
        account.show_by_month()
    elif show_select == 4:
        account.show_by_title_r()
    elif show_select == 5:
        account.show_by_amount_r()
    elif show_select == 6:
        account.show_by_month_r()

def show_by():
    selection = -1
    txt_opt = [f"({colors.VIOLET}1{colors.ENDC}) By Title (alphabetically)",
                f"({colors.VIOLET}2{colors.ENDC}) By Amount (lower first)",
                f"({colors.VIOLET}3{colors.ENDC}) By Month (lower first)",
                f"({colors.VIOLET}4{colors.ENDC}) By Title (alphabetically reversed)",
                f"({colors.VIOLET}5{colors.ENDC}) By Amount (higher first)",
                f"({colors.VIOLET}6{colors.ENDC}) By Month (higher first)"
                ]
    show_opt = [x+1 for x in range(len(txt_opt))]

    while selection not in show_opt:
        for txt in txt_opt:
            print(txt)
        try:
            selection = int(input("·"))
            assert selection in show_opt
        except ValueError:
            print("Enter a valid input")
        except AssertionError:
            print("Selection not valid")

    return selection

# 2 ADD
def add_function(account):
    selection = -1
    options = {1:'Expense', 2:'Income'}
    txt_options = [
                f"({colors.VIOLET}1{colors.ENDC}) Add Expense",
                f"({colors.VIOLET}2{colors.ENDC}) Add Income"
                # f"({colors.VIOLET}4{colors.ENDC}) Back"
              ]

    while selection not in options.keys():
        for txt in txt_options:
            print(txt)
        try:
            selection = int(input("·"))
            assert selection in options.keys()
        except ValueError:
            print("Enter a valid option")
    add_item(selection, account)

def add_item(selection, account):
    txt = {1:'Expense', 2:'Income'}
    item_type = txt[selection]
    print(f"Describe your {item_type}:")

    item = new_item(item_type)
    account.add_item(item)
    print(f"{item_type} successfully added!")

def new_item(item_type):
    title = ''
    amount = ''
    month = -1

    while len(title) < 1:
        try:
            title = input(f"Enter the {item_type} title: ")
            assert len(title) > 0
            if title == "remove":
                title = ''
                print("Title name can not be 'remove'")
        except AssertionError:
            print("Write something")
            title = ''

    if title == "remove":
        return "remove"

    while type(amount) == str:
        try:
            amount = float(input(f"Enter the {item_type} amount: "))
        except ValueError:
            print("Enter only numbers separated by a dot.")
            amount = ''

    while month < 1 or month > 12:
        try:
            month = int(input(f"Enter the {item_type} month (1-12): "))
            assert 1 <= month <= 12
        except AssertionError:
            print("Enter a valid number of month (1-12)")

    item = Item(title, amount, month)
    return item

# 3 EDIT
def edit_function(account):
    selection = 0

    print("Select entry to edit:")
    account.full_show()
    while selection < 1 or selection > len(account.history):
        try:
            selection = int(input("Select the item: "))
            assert 1 <= selection <= len(account.history)
        except AssertionError:
            print("Select an item from the list")
            selection = 0
        except ValueError:
            print("Enter a valid input")
            selection = 0

    print("Type 'remove' in the title to remove the item instead")
    account.history[selection-1] = new_item('new')
    if account.history[selection-1] == "remove":
        del account.history[selection-1]
        print("Item removed")
    else:
        print("Item edited")
    account.full_show()

# 4 SAVE AND QUIT
def save_quit(account, file):
    file_name = ''
    if file == "":
        file_name = input("Type your file name: ")
    else:
        file_name = file
    data = {}
    data['history'] = []

    data['balance'] = account.balance
    for item in account.history:
        data['history'].append({
            'title': item.title,
            'month': item.month,
            'amount': item.amount
        })

    with open(f'{file_name}.txt', 'w') as outfile:
        json.dump(data, outfile)
