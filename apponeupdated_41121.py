import random

database = {} #dictionary
currentBalance = 0

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

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()
    

def register(): 
    print("****** Register ******")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == === ===== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == === ===== ===== ===")

    login()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1] ) )
 
    selectedOption = input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit ")

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
    withdraw = float(input("How much would you like to withdraw?"))
    print('Take your cash')

def depositOperation():
    print("Deposit Operations")

def generationAccountNumber(): 

    return random.randrange(1111111111,9999999999)
init()