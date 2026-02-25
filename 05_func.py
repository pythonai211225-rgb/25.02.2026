
ICONS = {
    "bank": "🏦",
    "login": "🔐",
    "ok": "✅",
    "no": "❌",
    "menu": "📋",
    "money": "💸",
    "deposit": "➕",
    "withdraw": "➖",
    "transfer": "🔁",
    "balance": "💰",
    "user": "👤",
    "history": "🧾",
    "exit": "🚪",
    "warn": "⚠️",
}


#account      0     1        2     3   4    5
balance =   [300, 4000, 100_000, 5000, 0, 900]
passwords = ['000', '111', '222', '333', '444', '555']
# active   =  [True, True, True, False, False, True] -- bonus

'''
menu:
1. login
2. exit

login:
  account number? 2
  password? 222
  
menu:
1. deposit --> can deposit up to 10_000 without certificate, above need certificate
2. withdraw --> can withdraw and cannot get negative balance
3. transfer --> can transfer cannot get negative balance, into a valid account (active)
# 4. make active  --> only if not active  -- bonus
# 5. make not active --> only if active  -- bonus
6. exit to main menu
'''

def display_menu_login_exit():
    print('Menu:')
    print('1. Login')
    print('2. Exit')

def get_main_choice():
    choice = int(input('Choose 1-2:'))
    return choice

def get_account_number_from_user():
    account_number = int(input('whats the account number?'))
    return account_number

def check_if_valid(user_account_number, accounts):
    # account      0     1        2     3   4    5
    # accounts = [300, 4000, 100_000, 5000, 0, 900]
    if 0 <= user_account_number < len(accounts):
        valid = True
    else:
        valid = False
    return valid

    # return 0 <= user_account_number < len(balance):

def get_account_password():
    password = input('whats your password?')
    return password

def check_password_correct(user_account_number, user_password, passwords):
    # user_account_number 0
    # '000'
    # passwords = ['000', '111', '222', '333', '444', '555']
    if user_password == passwords[user_account_number]:
        return True
    else:
        return False

    # return user_password == passwords[user_account_number]

while True:
    display_menu_login_exit()
    main_choice = get_main_choice()
    if main_choice == 2:
        break
    if main_choice != 1:
        print('invalid choice')
        continue
    user_account_number = get_account_number_from_user()

    # if not check_if_valid(user_account_number, accounts):
    if check_if_valid(user_account_number, accounts) == False:
        print('account not valid...')
        continue
    user_password = get_account_password()
    if check_password_correct(user_account_number, user_password, passwords) == False:
        print('wrong password...')
        continue

    while True:
        display_account_menu()
        choice = get_account_menu_choice()
        match choice:
            case 1:deposit_amount = get_deposit_amount()
                   deposit(user_account_number, balance, deposit_amount)
                    continue
            case 2:withdraw_amount = get_withdraw_amount()
                   withdraw(user_account_number, balance, withdraw_amount)
            case 3:transfer_amount = get_transfer_amount()
                   trasfer_to_account = get_transfer_to_account(balance)
                    if check_if_valid(trasfer_to_account, accounts) == False:
                    print('account not valid...')
                        continue
                    transfer(user_account_number, balance, trasfer_to_account)
            case 4: break
            case _: print('invalid choice')


print('Goodbye ...')







