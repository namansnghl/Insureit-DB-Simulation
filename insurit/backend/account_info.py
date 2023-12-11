import os


# Function to update the email of the customer
def updateEmail(connection, customer_id):
    cursor = connection.cursor()
    email = input('Enter your new Email:')
    query = "UPDATE customer SET email = %s WHERE Customer_id = %s"
    cursor.execute(query, (email, customer_id))
    connection.commit()
    print('Email has been updated successfully!')


# Function to update the phone number of the customer
def updatePhone(connection, customer_id):
    cursor = connection.cursor()
    phone = input('Enter your new Phone Number:')
    query = "UPDATE customer SET Phone = %s WHERE Customer_id = %s"
    cursor.execute(query, (phone, customer_id))
    connection.commit()
    print('Phone Number has been updated successfully!')


# Function to update the addresss of the customer
def updateAddress(connection, customer_id):
    cursor = connection.cursor()
    address = input('Enter your new Address:')
    query = "UPDATE customer SET Address = %s WHERE Customer_id = %s"
    cursor.execute(query, (address, customer_id))
    connection.commit()
    print('Address has been updated successfully!')

# Function to display the menu
def menu():
    print('WARNING: Changing account settings')
    print('1. Update Email')
    print('2. Update Phone')
    print('3. Update Address')
    print('4. Cancel')
    return int(input('Your choice: '))

# Function to handle user input and call the appropriate update function
def chsettings(connection, customer_id, option=None):
    # If the option is not provided, display the menu
    if not option:
        option = menu()

    # Perform the chosen action based on the user's input
    if option == 1:
        updateEmail(connection, customer_id)
    elif option == 2:
        updatePhone(connection, customer_id)
    elif option == 3:
        updateAddress(connection, customer_id)
    elif option == 4:
        return 0 # User chose to cancel, return 0
    else:
        # If an invalid option is selected, recursively call the function with the same parameters
        chsettings(connection, customer_id, option)
