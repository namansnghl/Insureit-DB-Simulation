# Account_menu()
# ++ one function for each menu item

import os

#function to update the email of the customer
def updateEmail(connection, customer_id):
    cursor = connection.cursor()
    print("Hi! Set up your new email")
    email = input('Enter your new Email:')
    query = "UPDATE customer SET email = %s WHERE Customer_id = %s"
    cursor.execute(query,(email,customer_id))
    connection.commit()
    print('Email has been updated successfully!')

#function to update the phone number of the customer
def updatePhone(connection, customer_id):
    cursor = connection.cursor()
    print("Hi! Set up your new phone number")
    phone = input('Enter your new Phone Number:')
    query = "UPDATE customer SET Phone = %s WHERE Customer_id = %s"
    cursor.execute(query,(phone,customer_id))
    connection.commit()
    print('Phone Number has been updated successfully!')

#function to update the addresss of the customer
def updateAddress(connection, customer_id):
    cursor = connection.cursor()
    print("Hi! Set your new home address")
    address = input('Enter your new Address:')
    query = "UPDATE customer SET Address = %s WHERE Customer_id = %s"
    cursor.execute(query,(address,customer_id))
    connection.commit()
    print('Address has been updated successfully!')


def menu():
    print('WELCOME TO INSURIT!')
    print('-----------------------------')
    print('Menu')
    print('1. Update Email')
    print('2. Update Phone')
    print('3. Update Address')
    print('4. Cancel')
    print('-----------------------------')

def runInsurit(connection, customer_id, option=None):
    menu()
    #option = int(input('Please choose an option'))
    print('\n')
    if option==1:
        print('\n')
        updateEmail(customer_id)
        print('\n')
    if option==2:
        print('\n')
        updatePhone(customer_id)
        print('\n')
    if option==3:
        print('\n')
        updateAddress(customer_id)
        print('\n')
    if option==4:
        return 0
    else:
        os.system('cls')
        runInsurit()