# Account_menu()
# ++ one function for each menu item
import os

def menu():
    print('WELCOME TO INSURIT!')
    print('-----------------------------')
    print('Menu')
    print('1. Create an account')
    print('2. Login')
    print('3. Exit')
    print('-----------------------------')

def runInsurit():
    menu()
    n = int(input('Please choose an option'))
    if n==1:
        #userType() 
    if n==2:
        #login()
    if n==3:
        os.system('cls')
        print('---Thank you---')
    else:
        os.system('cls')
        runInsurit()