from .finance import fetch_finance_details, make_payment
from .views import view_policy

# Below function would take parameters such as policy_id, age, sum_assured, tenure and policy_type apart from connection
# for the below params, take input directly when the agent is calling this function
def calculate_premium(connection):
    try:
        cursor = connection.cursor()
        print("Fill below to Calculate an Estimate of the Premium\n")
        policy_id = input("Enter Policy ID: ")
        age = int(input("Enter age of the customer: "))
        sum_assured = int(input("Enter total sum assured for the following policy: "))
        tenure = int(input("Enter the tenure period: "))
        policy_type = input("Enter Policy type: HomePolicy or AutoPolicy: ")

        # Calling the MySQL stored function
        cursor.callproc('CalculatePremium', (policy_id, age, sum_assured, tenure, policy_type))

        result = cursor.fetchone()

        if result is not None:
            # The premium value is the first element in the result tuple
            premium_value = result[0]
            print(premium_value)
            return premium_value
        else:
            print("Error: Unable to retrieve premium value.")
            return None

    except mysql.connector.Error as err:

        print(f"MySQL Error: {err}")
        return None

    finally:

        if cursor:
            cursor.close()


# Claim_approvals would return a dataframe with all the approvals only
def get_approved_claims(connection):
    try:
        cursor = connection.cursor(dictionary=True)

        # SQL query to select all data for approved claims
        query = "SELECT * FROM claim_table WHERE claim_status = 'A'"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        approved_claims = cursor.fetchall()

        return approved_claims

    except mysql.connector.Error as err:
        # Handle MySQL errors here
        print(f"MySQL Error: {err}")
        return None

    finally:
        # Close the cursor
        if cursor:
            cursor.close()


def pay_policy(connection, id):
    listt = view_policy(connection, id)
    if listt:
        holder_idx = int(input("Choose your policy (Enter index) - "))
        print("Confirm Bank details:")
        fetch_finance_details(connection, id)
        input("Press Any button to continue")
        make_payment(connection, listt[holder_idx][0], id, listt[holder_idx][1])