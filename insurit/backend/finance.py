#importing libraries
import mysql.connector
from datetime import datetime, timedelta

#function fetch finance details of a user based on Customer_id
def fetch_finance_details(connection, customer_id):
    try:
        # Creating a cursor object
        cursor = connection.cursor()
        #SQL statement 
        query = f"SELECT * FROM Finance_details WHERE Customer_id = {customer_id}"

        cursor.execute(query)
        customer_details = cursor.fetchone()

        if customer_details:
            # Printing the customer details
            print(f"Customer ID: {customer_details[1]}")
            print(f"Account Number: {customer_details[2]}")
            print(f"Bank Name: {customer_details[4]}")
        else:
            print(f"No customer found with Customer ID {customer_id}")
    
    #handling error with exception
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        #closing the cursor
        cursor.close()



#Below function would check Due dates of policies within 7 days of the current date and show the details of those customers
def check_due_dates(connection):
    try:
        #establishing cursor object for connection 
        cursor = connection.cursor()
        #setting up variables
        seven_days_from_now = datetime.now().date() + timedelta(days=7)
        seven_days_from_now_str = seven_days_from_now.strftime("%m-%d-%Y")
        #SQL statemnt to execute
        query = f"""SELECT C.NAME, C.EMAIL, HOME_POLICY_ID, Auto_Policy_id FROM INSURIT.Policy_Holder PH
LEFT JOIN INSURIT.CUSTOMER C ON PH.CUSTOMER_ID = C.CUSTOMER_ID 
WHERE (HOME_POLICY_ID is not Null OR AUTO_POLICY_ID is not null)
AND PH.RENEWDATE BETWEEN CURDATE() AND STR_TO_DATE('{seven_days_from_now_str}','%m-%d-%Y');"""
        #Executing Query
        cursor.execute(query)
        #fetching data from DB
        due_policies = cursor.fetchall()

        #Condition for Due_dates
        if due_policies:
            print("Below customers have Due Dates within the Next 7 Days:")
            for policy in due_policies:
                if policy[-1] is None:
                    print(f"{policy[0]}, {policy[1]}, HOME_POLICY - {policy[2]}")
                else:
                    print(f"{policy[0]}, {policy[1]}, AUTO_POLICY - {policy[2]}")
            print()
        else:
            print("No policies with due dates within the next 7 days.")
    #handling errors with exception
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        
    finally:
        # Closing the cursor
        cursor.close()



#For the make_payment method, another method has to be defined which will extractd details needed in make_payment method
def get_policy_holder_id(connection, customer_id, policy_type, policy_id):
    try:
        #establishing connection
        cursor = connection.cursor()

        # Determine whether it's an Auto Policy or Home Policy
        policy_column = 'Auto_Policy_id' if policy_type.lower() == 'auto' else 'Home_Policy_id'

        # Query to get Holder_id based on Customer_id and Policy_Type
        query = f"SELECT Holder_id FROM Policy_Holder WHERE Customer_id = {customer_id} AND {policy_column} = {policy_id}"
        #executing query
        cursor.execute(query)
        holder_id = cursor.fetchone()
        
        return holder_id[0] if holder_id else None
    #handling error with exception
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        #closing the cursor
        cursor.close()

#defining a function to make payments for user
def make_payment(connection, policy_id, customer_id, policy_type):
    try:
        #establishing connection
        cursor = connection.cursor()
        amount = int(input("Enter the amount: "))

        # Get the current date
        current_date = datetime.now().date()

        # Get Holder_id based on Customer_id and Policy_Type
        holder_id = get_policy_holder_id(connection, customer_id, policy_type, policy_id)

        if holder_id is not None:
            # Update RenewDate in Policy_Holder table
            query_update_renew_date = f"UPDATE Policy_Holder SET RenewDate = '{current_date}' WHERE Holder_id = {holder_id}"
            cursor.execute(query_update_renew_date)

            # Insert data into Transactions table
            query_insert_transaction = f"INSERT INTO Transactions (Date, status_of_transaction, Amount, Customer_id, Holder_id) VALUES ('{current_date}', 'Completed', {amount}, {customer_id}, {holder_id})"
            cursor.execute(query_insert_transaction)

            # Commit the changes
            connection.commit()

            print(f"Payment successfully processed for Customer ID: {customer_id}, Policy ID: {policy_id}")

        else:
            print(f"No matching policy found for Customer ID: {customer_id}, Policy ID: {policy_id}, and Policy Type: {policy_type}")

    #handling error with exception
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        #closing cursor
        cursor.close()