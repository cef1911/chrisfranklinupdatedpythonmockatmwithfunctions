import random
import validation
import database

# database = {
#     7012190042: ['Chris', 'Franklin', 'cef1911@hotmail.com', 'TestPass1', 200]
# } 
#currentBalance = 0


def init():

    print("Welcome to bank ChrisBank let's register you so you can use the ATM, first we will establish an account for you")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
            
        login()
    elif(haveAccount == 2):      
        register()
    else:
        print("You have selected a invalid option")
        init()


def login():
    print("******** Login ********")

    accountNumberFromUser = input("What is your account number? \n")

    is_valid_account_number = account_number_validation(accountNumberFromUser)

    if is_valid_account_number:
        password = input("What is your password \n")

        for accountNumber,userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    bankOperation(userDetails)
    
        print('Invalid account or password')
        login()
    
    else:
        init()

def account_number_validation(accountNumber):
    if account_number_validation:

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalid Account Number, account number should be an integer")
                return False
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Account Number cannot be less or more than 10 digits")
            return False

    
    else:
        print("Account Number is a required field")
        return False


def register():   
    print("****** Register ******")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    is_user_created = database.create(accountNumber, [first_name, last_name, email, password, 0])

    if is_user_created:


        print("Your Account Has been created")
        print(" == === ===== ===== ===")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print(" == === ===== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
 
    selectedOption = 1
 
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):  
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        exit()

    else:
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance

    withdraw = float(input("How much would you like to withdraw?"))
    print('Take your cash')

def depositOperation():
    print("Deposit Operations")
     # get current balance
     # get amount to deposit
     # add deposited amount to currenct balance
     # deduct withdrawn amount form current balance
     # print('Do you want to do something else?')
     # if they say yes they get directed to the bank operations again
     # if they say no they are exited out the system with a print statement 
     # that says take your card

def generationAccountNumber(): 
    return random.randrange(1111111111,9999999999)

def set_current_balance(userDetails, balance):
    userDetails[4] = balance

def get_current_balance(userDetails):
    return userDetails[4]

def logout():
    login()
    
init()