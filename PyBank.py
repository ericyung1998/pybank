
# coding: utf-8

# In[6]:

# -*- coding: utf-8 -*-

import getpass as g # import used to hid password entries

width = 44 # width of the interface printed screens
login_tried = 0 # tracks login attempts
endProgram = False # determines if program should end

account = {
        "admin":{"password": "password",
                   "balance": {"USD": 1000,
                                "HKD": 10000,
                               },
                                
                            },
        "eric":{"password": "123",
                   "balance": {"HKD": 15,
                                "CNY": 20,
                                "EUR": 50,
                               },
                                
                            },
        }
                   
currency = {
            "USD" : {
                    "USD" : 1,
                    "HKD" : 7.831600,
                    "JPY" : 7.831600/0.074600,
                    "CNY" : 7.831600/1.103100,
                    "EUR" : 7.831600/8.769800,
                    },
            "HKD" : {
                    "USD" : 1/7.862800,
                    "HKD" : 1,
                    "JPY" : 1/0.074600,
                    "CNY" : 1/1.103100,
                    "EUR" : 1/8.769800,
                    },
            "JPY" : {
                    "USD" : 0.073740/7.862800,
                    "HKD" : 0.073740,
                    "JPY" : 1,
                    "CNY" : 0.073740/1.103100,
                    "EUR" : 0.073740/8.769800,
                    },
            "CNY" : {
                    "USD" : 1.088200/7.862800,
                    "HKD" : 1.088200,
                    "JPY" : 1.088200/0.074600,
                    "CNY" : 1,
                    "EUR" : 1.088200/8.769800,
                    },
            "EUR" : {
                    "USD" : 8.640000/7.862800,
                    "HKD" : 8.640000,
                    "JPY" : 8.640000/0.074600,
                    "CNY" : 8.640000/1.103100,
                    "EUR" : 1,
                    },
        }

### Task 2 balance checking function
            
def check_balance(account, login):

    str_USD = '' # str to store the currency account and amount
    str_HKD = '' # str to store the currency account and amount
    str_JPY = '' # str to store the currency account and amount
    str_CNY = '' # str to store the currency account and amount
    str_EUR = '' # str to store the currency account and amount

    bool_USD_exist = False # bool to store and determine existent of currency account
    bool_HKD_exist = False # bool to store and determine existent of currency account
    bool_JPY_exist = False # bool to store and determine existent of currency account
    bool_CNY_exist = False # bool to store and determine existent of currency account
    bool_EUR_exist = False # bool to store and determine existent of currency account

## combines the currency and currency amount into a string after determining the existent of the currency account
    for existing_currency in account[login]['balance'].keys():
        if existing_currency == 'USD':
            str_USD = "USD ($): " + str(account[login]['balance']['USD'])
            bool_USD_exist = True
        elif existing_currency == 'HKD':
            str_HKD = "HKD ($): " + str(account[login]['balance']['HKD'])
            bool_HKD_exist = True
        elif existing_currency == 'JPY':
            str_JPY = "JPY (¥): " + str(account[login]['balance']['JPY'])
            bool_JPY_exist = True
        elif existing_currency == 'CNY':
            str_CNY = "CNY (¥): " + str(account[login]['balance']['CNY'])
            bool_CNY_exist = True
        elif existing_currency == 'EUR':
            str_EUR = "EUR (€): " + str(account[login]['balance']['EUR'])
            bool_EUR_exist = True

## always prints the existing currencies in a predetermined order (shows the account balance screen)
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Check Account Balance".center(width)))
    print("## {} ##".format("".center(width)))
    if bool_USD_exist == True:
        print("## {} ##".format(str_USD.ljust(width)))
    if bool_HKD_exist == True:
        print("## {} ##".format(str_HKD.ljust(width)))
    if bool_JPY_exist == True:
        print("## {} ##".format(str_JPY.ljust(width)))
    if bool_CNY_exist == True:
        print("## {} ##".format(str_CNY.ljust(width)))
    if bool_EUR_exist == True:
        print("## {} ##".format(str_EUR.ljust(width)))
    print("## {} ##".format("".center(width)))
    print("##################################################")
    print("")
          
    return False
          
### Task 3: Cash Withdrawal
    
def cash_withdrawal(account, login):

    str_USD = '' # str to store the currency account and amount
    str_HKD = '' # str to store the currency account and amount
    str_JPY = '' # str to store the currency account and amount
    str_CNY = '' # str to store the currency account and amount
    str_EUR = '' # str to store the currency account and amount

    bool_USD_exist = False # bool to store and determine existent of currency account
    bool_HKD_exist = False # bool to store and determine existent of currency account
    bool_JPY_exist = False # bool to store and determine existent of currency account
    bool_CNY_exist = False # bool to store and determine existent of currency account
    bool_EUR_exist = False # bool to store and determine existent of currency account
    
    list_currency_position = [] # list to store the order of the existing currency account
    
    menu_withdraw = 0 # variable that store user input and is used to check if input is correct, otherwise it'll loop
    
    menu_withdraw_amount_loop = True # bool that determines to continue looping of asking user for withdraw amount input
    
    menu_withdraw_accept = 0 # variable that store user input and is used to check if input is correct, otherwise it'll loop
    
    str_currency_account = '' # str to store the currency account inputed by user

## combines the currency account and its order after determining the existent of the currency account
    for existing_currency in account[login]['balance'].keys():
        if existing_currency == 'USD':
            str_USD = str(len(list_currency_position)+1)+". USD ($)"
            bool_USD_exist = True
            list_currency_position.append('USD')
        elif existing_currency == 'HKD':
            str_HKD = str(len(list_currency_position)+1)+". HKD ($)"
            bool_HKD_exist = True
            list_currency_position.append('HKD')
        elif existing_currency == 'JPY':
            str_JPY = str(len(list_currency_position)+1)+". JPY (¥)"
            bool_JPY_exist = True
            list_currency_position.append('JPY')
        elif existing_currency == 'CNY':
            str_CNY = str(len(list_currency_position)+1)+". CNY (¥)"
            bool_CNY_exist = True
            list_currency_position.append('CNY')
        elif existing_currency == 'EUR':
            str_EUR = str(len(list_currency_position)+1)+". EUR (€)"
            bool_EUR_exist = True
            list_currency_position.append('EUR')

## loops the menu of the withdraw screen until user enters the appropriate option (shows the cash withdrawal account screen)      
    while not menu_withdraw in range(1,len(list_currency_position)+1):
        
        print("")
        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Select Cash Withdrawal Account".center(width)))
        print("## {} ##".format("".center(width)))
        if bool_USD_exist == True:
            print("## {} ##".format(str_USD.ljust(width)))
        if bool_HKD_exist == True:
            print("## {} ##".format(str_HKD.ljust(width)))
        if bool_JPY_exist == True:
            print("## {} ##".format(str_JPY.ljust(width)))
        if bool_CNY_exist == True:
            print("## {} ##".format(str_CNY.ljust(width)))
        if bool_EUR_exist == True:
            print("## {} ##".format(str_EUR.ljust(width)))
        print("## {} ##".format("".center(width)))
        print("##################################################")
        print("")

## try to store the input by user, if input is string and cannot be converted to integer, continue the while loop        
        try:
            menu_withdraw = int(input("Choose your account: "))
        except:
            continue

## if the user enters an appropriate option proceed to the next screen   
    else:
        
        while menu_withdraw_amount_loop:

## try to store the withdraw amount input by user, if input is string and cannot be converted to integer, continue to while loop            
            try:
                if menu_withdraw == 1:
                    amount = int(input("Enter the amount of "+ list_currency_position[0]+" you want to withdraw: "))
                    str_currency_account = list_currency_position[0]
                if menu_withdraw == 2:
                    amount = int(input("Enter the amount of "+ list_currency_position[1]+" you want to withdraw: "))
                    str_currency_account = list_currency_position[1]
                if menu_withdraw == 3:
                    amount = int(input("Enter the amount of "+ list_currency_position[2]+" you want to withdraw: "))
                    str_currency_account = list_currency_position[2]
                if menu_withdraw == 4:
                    amount = int(input("Enter the amount of "+ list_currency_position[3]+" you want to withdraw: "))
                    str_currency_account = list_currency_position[3]
                if menu_withdraw == 5:
                    amount = int(input("Enter the amount of "+ list_currency_position[4]+" you want to withdraw: "))
                    str_currency_account = list_currency_position[4]
            except:
                continue

## checks if the input amount is withdrawable (less than max, more than min, and more than in currency account)
            if amount >= 50000:
                print("The maximum amount of each withdraw transaction is limited to $50,000")
            elif amount <= 0:
                print("Amount of withdraw transaction cannot be less than $1")
            else:
                if amount > account[login]['balance'][str_currency_account]:
                    print("Withdrawal amount exceed " + str_currency_account + " account amount")
                    print("")
                    break
                else:
                    
                    menu_withdraw_amount_loop = False #if pass all validation looping will be false
                    
                    account[login]['balance'][str_currency_account] = round(account[login]['balance'][str_currency_account] - amount,2)
                    
## delete account login balance key if withdraw amount in the currency account left is 0
                    
                    if account[login]['balance'][str_currency_account] == 0:
                        print("Amount left in " + str(str_currency_account) + " account is 0 (account will be deleted)")
                        del account[login]['balance'][str_currency_account]

## loops the menu of the withdraw accept screen until user enters the appropriate option  (shows the withdraw accepted screen)                   
                    while not menu_withdraw_accept in range(1,3):
                        
                        print("")
                        print("##################################################")
                        print("## {} ##".format("".center(width)))
                        print("## {} ##".format("Withdraw Accepted".center(width)))
                        print("## {} ##".format("".center(width)))
                        print("## {} ##".format("1. Check Balance".ljust(width)))
                        print("## {} ##".format("2. Exit".ljust(width)))
                        print("## {} ##".format("".center(width)))
                        print("##################################################")
                        print("")
                        
                        try:
                            menu_withdraw_accept = int(input("Enter the Option: "))
                            print("")
                        except:
                            continue
                        
## if the user enters an appropriate option proceed to the next screen                          
                    else:
                        
                        if menu_withdraw_accept == 1:
                            check_balance(account, login)
                        elif menu_withdraw_accept == 2:
                            break

    return False

#### Task 4: Transfer money to other user
    
def transfer(account, login):

    str_USD = '' # str to store the currency account and amount
    str_HKD = '' # str to store the currency account and amount
    str_JPY = '' # str to store the currency account and amount
    str_CNY = '' # str to store the currency account and amount
    str_EUR = '' # str to store the currency account and amount

    bool_USD_exist = False # bool to store and determine existent of currency account
    bool_HKD_exist = False # bool to store and determine existent of currency account
    bool_JPY_exist = False # bool to store and determine existent of currency account
    bool_CNY_exist = False # bool to store and determine existent of currency account
    bool_EUR_exist = False # bool to store and determine existent of currency account
    
    list_currency_position = [] # list to store the order of the existing currency account
    
    list_recipients = [] # list to store the order of the existing recipeints
    
    menu_transfer = 0  # variable that store user input and is used to check if input is correct, otherwise it'll loop
    
    transfer_loop_account = False # bool that determines to continue looping of asking user for transfer account input
    
    transfer_loop_amount = False # bool that determines to continue looping of asking user for transfer amount input
    
    recipient_chosen = 0 # integer to store the recipient inputted by user
    
    menu_transfer_accept = 0 # variable that store user input and is used to check if input is correct, otherwise it'll loop
    
    terminate = False # bool that determines whether to terminate the transfer process

## combines the currency account and its order after determining the existent of the currency account    
    for existing_currency in account[login]['balance'].keys():
        if existing_currency == 'USD':
            str_USD = str(len(list_currency_position)+1)+". USD ($)"
            bool_USD_exist = True
            list_currency_position.append('USD')
        elif existing_currency == 'HKD':
            str_HKD = str(len(list_currency_position)+1)+". HKD ($)"
            bool_HKD_exist = True
            list_currency_position.append('HKD')
        elif existing_currency == 'JPY':
            str_JPY = str(len(list_currency_position)+1)+". JPY (¥)"
            bool_JPY_exist = True
            list_currency_position.append('JPY')
        elif existing_currency == 'CNY':
            str_CNY = str(len(list_currency_position)+1)+". CNY (¥)"
            bool_CNY_exist = True
            list_currency_position.append('CNY')
        elif existing_currency == 'EUR':
            str_EUR = str(len(list_currency_position)+1)+". EUR (€)"
            bool_EUR_exist = True
            list_currency_position.append('EUR')

## loops the menu of the transfer screen until user enters the appropriate option (shows the cash transfer accounts screen)          
    while not menu_transfer in range(1,len(list_currency_position)+1):

        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Select Cash Transfer Account".center(width)))
        print("## {} ##".format("".center(width)))
        if bool_USD_exist == True:
            print("## {} ##".format(str_USD.ljust(width)))
        if bool_HKD_exist == True:
            print("## {} ##".format(str_HKD.ljust(width)))
        if bool_JPY_exist == True:
            print("## {} ##".format(str_JPY.ljust(width)))
        if bool_CNY_exist == True:
            print("## {} ##".format(str_CNY.ljust(width)))
        if bool_EUR_exist == True:
            print("## {} ##".format(str_EUR.ljust(width)))
        print("## {} ##".format("".center(width)))
        print("##################################################")
        print("")

## try to store the input by user, if input is string and cannot be converted to integer, continue the while loop         
        try:
            menu_transfer = int(input("Choose your account: "))
        except:
            continue
 
## if the user enters an appropriate option proceed to the next screen        
    else:

## loops the menu of the transfer screen until user enters the appropriate option (shows the transferable recipients screen)        
        while not transfer_loop_account:
            
            list_recipients = [] ## clears the recipients list so the number doesn't not increase everytime it loops
            
            print("")
            print("##################################################")
            print("## {} ##".format("".center(width)))
            print("## {} ##".format(("Select "+list_currency_position[menu_transfer-1]+" Cash Transfer Recipient").center(width)))
            print("## {} ##".format("".center(width)))
            for accounts in account.keys():
                if login != accounts:
                    print("## {} ##".format((str(len(list_recipients)+1)+". "+accounts.capitalize()).ljust(width)))
                    list_recipients.append(accounts)                  
            print("## {} ##".format("".center(width)))
            print("##################################################")
            print("")
            
            transfer_loop_account = True ## stops the loop temporarily, but if validation fails, it will loop

## try to store the input by user, if input is string and cannot be converted to integer or if the entered integer is out of bound, continue the while loop
            try:
                recipient_chosen = int(input("Enter the Option: "))
                if recipient_chosen > len(list_recipients) or recipient_chosen <= 0:
                    transfer_loop_account = False
            except:
                transfer_loop_account = False
            
## loops the transfer screen amount input until user enters the appropriate input 
        while not transfer_loop_amount:

## try to store the input by user, if input is string and cannot be converted to integer or if the entered integer is out of bound, continue the while loop
            try:
                if list_currency_position[menu_transfer-1] in account[list_recipients[recipient_chosen-1]]['balance'].keys():
                    transfer_amount = int(input("Enter the amount of "+ list_currency_position[menu_transfer-1]+" to transfer to "+str(list_recipients[recipient_chosen-1]).capitalize()+": "))

## checks if the input amount is transferable (less than max, more than min, and less than currency account)                         
                    if transfer_amount >= 10000:
                        print("The maximum amount of each withdraw transaction is limited to $10,000")
                        continue
                    elif transfer_amount <= 0:
                        print("Amount of withdraw transaction cannot be less than $1")
                        continue
                    else:
                        if transfer_amount > account[login]['balance'][list_currency_position[menu_transfer-1]]:
                            print("Transfer amount exceed " + list_currency_position[menu_transfer-1] + " account amount")
                            print("")
                            terminate = True
                            break
                        else:
                            transfer_loop_amount = True ## if pass all validation, stops the loop

## calculation of the currency accounts
                            account[login]['balance'][list_currency_position[menu_transfer-1]] = account[login]['balance'][list_currency_position[menu_transfer-1]] - transfer_amount ## deduct own currency account
                            
                            account[list_recipients[recipient_chosen-1]]['balance'][list_currency_position[menu_transfer-1]] = account[list_recipients[recipient_chosen-1]]['balance'][list_currency_position[menu_transfer-1]] + transfer_amount # add to recipient currency account
                                
## delete account login balance key if withdraw amount in the currency account left is 0
                            if account[login]['balance'][list_currency_position[menu_transfer-1]] == 0:
                                print("Amount left in " + str(list_currency_position[menu_transfer-1]) + " account is 0 (account will be deleted)")
                                del account[login]['balance'][list_currency_position[menu_transfer-1]]

## if transfer recipient doesn't own the selected currency account, the transfer process will terminate and return to main menu                           
                else:
                    print("Transfer Recipient: " + str(list_recipients[recipient_chosen-1]).capitalize() + " doesn't have " + list_currency_position[menu_transfer-1] + " account")
                    print("")
                    terminate = True
                    break
                    
            except:
                continue
            
## checks if the transfer process should be terminated
        if terminate == False:
## loops the menu of the transfer accept screen until user enters the appropriate option  (shows the transfer accepted screen) 
            while not menu_transfer_accept in range(1,3):
                
                print("")
                print("##################################################")
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("Transfer Accepted".center(width)))
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("1. Check Balance".ljust(width)))
                print("## {} ##".format("2. Exit".ljust(width)))
                print("## {} ##".format("".center(width)))
                print("##################################################")
                print("")
    
                try:
                    menu_transfer_accept = int(input("Enter the Option: "))
                    print("")
                except:
                    continue
                
## if the user enters an appropriate option proceed to the next screen 
            else:
                if menu_transfer_accept == 1:
                    check_balance(account, login)
                if menu_transfer_accept == 2:

                    return False

#### Task 5: Currency Exchange
    
def currency_exchange(account, login):

    str_USD = '' # str to store the currency account and amount
    str_HKD = '' # str to store the currency account and amount
    str_JPY = '' # str to store the currency account and amount
    str_CNY = '' # str to store the currency account and amount
    str_EUR = '' # str to store the currency account and amount

    bool_USD_exist = False # bool to store and determine existent of currency account
    bool_HKD_exist = False # bool to store and determine existent of currency account
    bool_JPY_exist = False # bool to store and determine existent of currency account
    bool_CNY_exist = False # bool to store and determine existent of currency account
    bool_EUR_exist = False # bool to store and determine existent of currency account
    
    list_currency_position = [] # list to store the order of the existing currency account
    
    list_currency_position2 = ['USD','HKD','JPY','CNY','EUR'] # list to store the predetermined order of the currency accounts (will be used to rearrange dictionary order)
    
    FROM_currency = 0 # integer to store the FROM_currency inputted by user
    TO_currency = 0 # integer to store the TO_currency inputted by user
    
    currency_exchange_loop = False # bool that determines to continue looping of asking user for currency exhcange amount input
    
    menu_currencyex_accept = 0 # variable that store user input and is used to check if input is correct, otherwise it'll loop
 
## combines the currency account and its order after determining the existent of the currency account   
    for existing_currency in account[login]['balance'].keys():
        if existing_currency == 'USD':
            str_USD = str(len(list_currency_position)+1)+". USD ($)"
            bool_USD_exist = True
            list_currency_position.append('USD')
        elif existing_currency == 'HKD':
            str_HKD = str(len(list_currency_position)+1)+". HKD ($)"
            bool_HKD_exist = True
            list_currency_position.append('HKD')
        elif existing_currency == 'JPY':
            str_JPY = str(len(list_currency_position)+1)+". JPY (¥)"
            bool_JPY_exist = True
            list_currency_position.append('JPY')
        elif existing_currency == 'CNY':
            str_CNY = str(len(list_currency_position)+1)+". CNY (¥)"
            bool_CNY_exist = True
            list_currency_position.append('CNY')
        elif existing_currency == 'EUR':
            str_EUR = str(len(list_currency_position)+1)+". EUR (€)"
            bool_EUR_exist = True
            list_currency_position.append('EUR')

## loops the menu of the exchange screen until user enters the appropriate option, also determines the FROM_currency in user account (shows the currency exchange account "from" screen)          
    while not FROM_currency in range(1,len(list_currency_position)+1):
        
        print("")
        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Select Currency Exchange Account (FROM)".center(width)))
        print("## {} ##".format("".center(width)))
        if bool_USD_exist == True:
            print("## {} ##".format(str_USD.ljust(width)))
        if bool_HKD_exist == True:
            print("## {} ##".format(str_HKD.ljust(width)))
        if bool_JPY_exist == True:
            print("## {} ##".format(str_JPY.ljust(width)))
        if bool_CNY_exist == True:
            print("## {} ##".format(str_CNY.ljust(width)))
        if bool_EUR_exist == True:
            print("## {} ##".format(str_EUR.ljust(width)))
        print("## {} ##".format("".center(width)))
        print("##################################################")
        print("")
              
## try to store the input by user, if input is string and cannot be converted to integer, continue the while loop               
        try:
            FROM_currency = int(input("Select account for currency to exchange from: "))
        except:
            continue

## if the user enters an appropriate option proceed to the next screen           
    else:

## loops the menu of the exchange screen until user enters the appropriate option (shows the currency exchange account "to" screen)            
        while not TO_currency in [1,2,3,4,5]:
            print("")
            print("##################################################")
            print("## {} ##".format("".center(width)))
            print("## {} ##".format(("Select Currency Exchange Account (TO)").center(width)))
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("1. USD ($)".ljust(width)))
            print("## {} ##".format("2. HKD ($)".ljust(width)))
            print("## {} ##".format("3. JPY (¥)".ljust(width))) 
            print("## {} ##".format("4. CNY (¥)".ljust(width))) 
            print("## {} ##".format("5. EUR (€)".ljust(width))) 
            print("## {} ##".format("".center(width)))
            print("##################################################")
            print("")

## try to store the input by user, if input is string and cannot be converted to integer, continue the while loop              
            try:
                TO_currency = int(input("Select account for currency to exchange to: "))
            except:
                continue
 
## if the user enters an appropriate option proceed to the next screen          
        else:

## loops the exchange currency amount input until user enters the appropriate input 
            while not currency_exchange_loop:
            
                #float validation checking missing
                try:
                    exchange_amount_input = int(input("Enter amount of "+ list_currency_position2[TO_currency-1] + " to get: "))
                    currency_exchange_loop = True
                    
                    if exchange_amount_input <= 0:
                        print("Currency exchange amount cannot be less than $1")
                        currency_exchange_loop = False
                        continue
                    
                    exchange_amount_total_TO = account[login]['balance'][list_currency_position[FROM_currency-1]] * currency[list_currency_position[FROM_currency-1]][list_currency_position2[TO_currency-1]]

                    exchange_amount_total_FROM = exchange_amount_input * 1/(currency[list_currency_position[FROM_currency-1]][list_currency_position2[TO_currency-1]])

                    if exchange_amount_total_TO > exchange_amount_input: ## EXCHANGE
                        if list_currency_position2[TO_currency-1] in account[login]['balance']: ## CURRENCY ACCOUNT EXISTS
                            
                            account[login]['balance'][list_currency_position2[TO_currency-1]] = round(account[login]['balance'][list_currency_position2[TO_currency-1]] + exchange_amount_input,2) ## ADD THE EXCHANGED CURRENCY TO_currency account
                            account[login]['balance'][list_currency_position[FROM_currency-1]] = round(account[login]['balance'][list_currency_position[FROM_currency-1]] - exchange_amount_total_FROM,2) ## SUBTRACT THE EXCHANGE CURRENCY FROM_currency account
                                
## delete account login balance key if withdraw amount in the currency account left is 0
                                    
                            if account[login]['balance'][list_currency_position[FROM_currency-1]] == 0:
                                print("Amount left in " + str(list_currency_position[FROM_currency-1]) + " account is 0 (account will be deleted)")
                                del account[login]['balance'][list_currency_position[FROM_currency-1]]
                            
                        else: ## CURRENCY ACCOUNT DOESN"T EXIST

                            account[login]['balance'][str(list_currency_position2[TO_currency-1])] = 0 # CREATE NEW CURRENCY ACCOUNT IF IT DOESN'T EXIST

                            account[login]['balance'][list_currency_position2[TO_currency-1]] = round(account[login]['balance'][list_currency_position2[TO_currency-1]] + exchange_amount_input,2) ## ADD THE EXCHANGED CURRENCY TO_currency account
                            account[login]['balance'][list_currency_position[FROM_currency-1]] = round(account[login]['balance'][list_currency_position[FROM_currency-1]] - exchange_amount_total_FROM,2) ## SUBTRACT THE EXCHANGE CURRENCY FROM_currency account
                                
## delete account login balance key if withdraw amount in the currency account left is 0
                                    
                            if account[login]['balance'][list_currency_position[FROM_currency-1]] == 0:
                                print("Amount left in " + str(list_currency_position[FROM_currency-1]) + " account is 0 (account will be deleted)")
                                del account[login]['balance'][list_currency_position[FROM_currency-1]]
                                    
## function to rearrange the dictionary order through zipping lists - this because by adding a new currency account to the dictionary, it messes up the order of the currency displayed in other functions (withdraw, transfer, view balance)                      
                            
                            list_currency_order = [] # empty list used to store the current order of the currency accounts
                            list_currency_order2 = [0,1,2,3,4] # list used to store the revised order of the currency accounts - given initial values because we are replacing values of the list through the index
                            list_currency_order3 = [0,1,2,3,4] # list used to store the revised order of the currency accounts amounts - given initial values because we are replacing values of the list through the index 

                            dict_temp = {} # temporary dictionary created to store the revised order of the currency accounts (key) and currency accounts amounts (value), will be used to replace the dictionary in account[login]['balance']

                            for accounts in account[login]['balance']:
                                list_currency_order.append(accounts)

                            for accounts in list_currency_order:
                                if accounts == "USD":
                                    list_currency_order2[0] = "USD"
                                    list_currency_order3[0] = account[login]['balance']['USD']
                                elif accounts == "HKD":
                                    list_currency_order2[1] = "HKD"
                                    list_currency_order3[1] = account[login]['balance']['HKD']
                                elif accounts == "JPY":
                                    list_currency_order2[2] = "JPY"
                                    list_currency_order3[2] = account[login]['balance']['JPY']
                                elif accounts == "CNY":
                                    list_currency_order2[3] = "CNY"
                                    list_currency_order3[3] = account[login]['balance']['CNY']
                                elif accounts == "EUR":
                                    list_currency_order2[4] = "EUR"
                                    list_currency_order3[4] = account[login]['balance']['EUR']

                            dict_temp = dict(zip(list_currency_order2,list_currency_order3))

                            account[login]['balance'] = dict_temp
                            
                    else: ## NO EXCHANGE                    
                        currency_exchange_loop = False
                        print("Exchange amount exceed " + str(list_currency_position[FROM_currency-1])+ " account amount")
                        print("")
                        break
                       
                except:
                    continue

## loops the menu of the exchange accept screen until user enters the appropriate option  (shows the exchange accepted screen)                 
                while not menu_currencyex_accept in range(1,3):
                    
                    print("")
                    print("##################################################")
                    print("## {} ##".format("".center(width)))
                    print("## {} ##".format("Currency Exchange Accepted".center(width)))
                    print("## {} ##".format("".center(width)))
                    print("## {} ##".format("1. Check Balance".ljust(width)))
                    print("## {} ##".format("2. Exit".ljust(width)))
                    print("## {} ##".format("".center(width)))
                    print("##################################################")
                    print("")

## if the user enters an appropriate option proceed to the next screen                         
                    try:
                        menu_currencyex_accept = int(input("Enter the Option: "))
                        print("")
                    except:
                        continue
                        
                else:
                    if menu_currencyex_accept == 1:
                        check_balance(account, login)
                    elif menu_currencyex_accept == 2:
                        break
                        
    return False
    
## welcome page

print("")
print("##################################################")
print("## {} ##".format("".center(width)))
print("## {} ##".format("Welcome to PyBank".center(width)))
print("## {} ##".format("".center(width)))
print("##################################################")
      
#### Task 1: login validation

bool_login_loop = True # bool to evaluate whether to continue the login loop
bool_login_failed = False # bool to evaluate whether login failed during the nested while loop

while bool_login_loop:
    
    print("")
    login = str(input("Username: "))
## Check the existence of username in account dictionary    
    if login in account:    
## Password input hidden with getpass import
        while True:     
            password = g.getpass(prompt='Password: ')           
            if account[login]['password'] == password:
                print("Login Success")
                print("")
                bool_login_loop = False
                break
            
            else:
                print("Invalid Password ({} attempt left)".format(2-login_tried))
                login_tried += 1
## Maximum number of login attempts does not exceed 3 (for both Username and Password)                            
            if login_tried > 2:
                endProgram = True
                bool_login_loop = False
                bool_login_failed = True
                print("Login Failed")
                print("")
                break 
               
    else:
        print("Invalid Username ({} attempts left)".format(2-login_tried))    
        login_tried += 1
## Maximum number of login attempts does not exceed 3 (for both Username and Password)
    if login_tried > 2 and bool_login_failed == False:
        endProgram = True
        bool_login_loop = False
        print("Login Failed")
        print("")
            
####### Task 1 End

while not endProgram:
## menu page
    menuoption = ""

    while not menuoption in ["1", "2", "3", "4","5"]: 
        
        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Select Service".center(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("1. Cash Withdrawal ".ljust(width)))
        print("## {} ##".format("2. Transfer".ljust(width)))
        print("## {} ##".format("3. Account Balance".ljust(width)))
        print("## {} ##".format("4. Currency Exchange".ljust(width)))
        print("## {} ##".format("5. Exit".ljust(width)))
        print("## {} ##".format("".center(width)))
        print("##################################################")
              
        print("")
        menuoption = input("Enter the option: ")
        print("")

    else:
        if menuoption == "1":
            endProgram = cash_withdrawal(account, login)
            input("Press Enter to continue...")
            print("")
            
        elif menuoption == "2":
            endProgram = transfer(account, login)
            input("Press Enter to continue...")
            print("")
            
        elif menuoption == "3":
            endProgram = check_balance(account, login)
            input("Press Enter to continue...")
            print("")
            
        elif menuoption == "4":
            endProgram = currency_exchange(account, login)
            input("Press Enter to continue...")
            print("")
            
        elif menuoption == "5":
            endProgram = True

input("Press Enter to end the program...")