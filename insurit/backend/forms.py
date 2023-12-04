# create claims
# create policy KARAN

#The function below would take connection as a parameter and some other info 
#from user and would call the addNewPolicy SP to create a new policy under either HomePolicy_detail or AutoPolicy_detail
#Manager/admin input for the params below

import mysql.connector
from datetime import datetime, timedelta

def add_new_policy(connection):
    try:
        cursor = connection.cursor()

        print("Please fill out below details to Add a new Policy to the Insurit System.\n")
        policy_name = input("Enter the name of the Policy: ")
        policy_type = input("Enter Policy Name: HomePolicy or AutoPolicy: ")
        description = input("Enter the Description: ")
        policy_active_flag = "Y"
        sum_assured = int(input("Enter the sum assured for this policy: "))
        tenure = int(input("What's the Tenure: "))

        if policy_name == "HomePolicy": policy_table = "HomePolicy_detail"
        else:  policy_table = "AutoPolicy_detail" 


        # Set parameters for the stored procedure
        params = (policy_name, policy_type, description, policy_active_flag, sum_assured, tenure, policy_table)
        #take policy_table from policy_type variable.

        # Call the stored procedure
        cursor.callproc('AddNewPolicy', params)

        # Commit the changes
        connection.commit()

        print("New policy added successfully!")

    except mysql.connector.Error as err:
        # Handle MySQL errors here
        print(f"MySQL Error: {err}")

    finally:
        # Close the cursor
        if cursor:
            cursor.close()



#Please import the below library in the main file 
#import datetime from date

def create_new_claim(connection):
    try:
        # Get input from the user
        claim_amount = int(input("Enter claim amount: "))
        holder_id = int(input("Enter holder ID: "))

        cursor = connection.cursor()

        # Call the stored procedure
        #Note that the claim date for newly created row would be for currrent date only
        cursor.callproc('CreateNewClaim', (claim_amount, date.today(), holder_id))

        # Commit the changes
        connection.commit()

        print("New claim created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor
        cursor.close()
