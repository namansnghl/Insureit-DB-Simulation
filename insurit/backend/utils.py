#importing other files as packages
from .finance import fetch_finance_details, make_payment
from .views import view_policy

#importing libraries
import mysql.connector
from datetime import datetime, timedelta
import pandas as pd
# Below function would take parameters such as policy_id, age, sum_assured, tenure and policy_type apart from connection

def calculate_premium(connection):
    try:
        #establishing connection
        cursor = connection.cursor()
        print("Fill below to Calculate an Estimate of the Premium\n")
        #setting up variables asking input from users
        policy_id = input("Enter Policy ID: ")
        age = int(input("Enter age of the customer: "))
        sum_assured = int(input("Enter total sum assured for the following policy: "))
        tenure = int(input("Enter the tenure period: "))
        policy_type = input("Enter Policy type: HomePolicy or AutoPolicy: ")

        # Calling the MySQL stored function using a SELECT statement
        cursor.execute('SELECT CalculatePremium(%s, %s, %s, %s, %s) AS premium', (policy_id, age, sum_assured, tenure, policy_type))

        #fetching the data from tables
        result = cursor.fetchone()

        if result is not None:
            # The premium value is the first element in the result tuple
            premium_value = result[0]
            print(premium_value)
            return premium_value
        else:
            print("Error: Unable to retrieve premium value.")
            return None

    #handling error with exception
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None

    finally:
        if cursor:
            #closing the cursor
            cursor.close()


# Claim_approvals would return a dataframe with all the approvals only
def get_approved_claims(connection):
    try:
        #establishing connection 
        cursor = connection.cursor(dictionary=True)

        # SQL query to select all data for approved claims
        query = "SELECT * FROM CLAIM WHERE claim_status = 'A'"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        approved_claims = cursor.fetchall()

        #creating dataframe of the fetched data
        claims_df = pd.DataFrame(approved_claims)

        print(claims_df)

        return claims_df


    except mysql.connector.Error as err:
        # Handle MySQL errors here
        print(f"MySQL Error: {err}")
        return None

    finally:
        # Close the cursor
        if cursor:
            cursor.close()


#function to pay for policies which uses other methods
def pay_policy(connection, id):
    listt = view_policy(connection, id)
    if listt:
        #asking user for the policy number for which to pay
        holder_idx = int(input("Choose your policy (Enter index) - "))
        print("Confirm Bank details:")
        #calling function
        fetch_finance_details(connection, id)
        input("Press Enter to continue")
        #calling function
        make_payment(connection, listt[holder_idx][0], id, listt[holder_idx][1])