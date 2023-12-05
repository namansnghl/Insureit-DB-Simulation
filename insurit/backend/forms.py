import mysql.connector
from datetime import datetime, timedelta
from .views import view_policy

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




def create_new_claim(connection, customer_id):
    try:
        # Get input from the user
        claim_amount = int(input("Enter claim amount: "))
        listt = view_policy(connection, customer_id)
        
        if listt:
            holder_idx = int(input("Choose your policy (Enter index) - "))
            auto_present = any('Auto' in value for value in listt.values())
            home_present = any('Home' in value for value in listt.values())

            if auto_present:
                holder_id_query = f"SELECT Holder_id FROM Policy_Holder WHERE Auto_Policy_id = {listt[holder_idx][0]}"
            elif home_present:
                holder_id_query = f"SELECT Holder_id FROM Policy_Holder WHERE Home_Policy_id = {listt[holder_idx][0]}"

            with connection.cursor() as cursor:
                cursor.execute(holder_id_query)
                holder_id = cursor.fetchone()[0]

            with connection.cursor() as cursor:
                # Call the stored procedure
                cursor.callproc('CreateNewClaim', (claim_amount, date.today(), holder_id))

            # Commit the changes
            connection.commit()

            print("New claim created successfully!")

    except (mysql.connector.Error, ValueError) as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor
        if cursor:
            cursor.close()    
