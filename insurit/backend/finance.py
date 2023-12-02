# fetch_finance() #Fetch the finance details of the customer with c_id
# make_payment(policy_number, username) #Transcations table mai entry, and jo bhi policy number, uske corresponding mai Due date change (Policy_Holder)

# check_dues() # With username, map the customer_id and check Policies which are due


def fetch_finance_details(connection, customer_id):
    try:
        # Creating a cursor object
        cursor = connection.cursor()

        query = f"SELECT * FROM Finance_details WHERE Customer_id = {customer_id}"

        cursor.execute(query)
        customer_details = cursor.fetchone()

        if customer_details:
            # Printing the customer details
            print("Customer Details:")
            print(f"Customer ID: {customer_details[1]}")
            print(f"SSN: {customer_details[0]}")
            print(f"Account Number: {customer_details[2]}")
            print(f"Income: {customer_details[3]}")
            print(f"Bank Name: {customer_details[4]}")
            print(f"Credit History: {customer_details[5]}")
        else:
            print(f"No customer found with Customer ID {customer_id}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        
        cursor.close()



#Below function would check Due dates of policies within 7 days of the current date and show the details of those customers
def check_due_dates(connection):
    try:
        cursor = connection.cursor()

        current_date = datetime.now().date()
        seven_days_from_now = current_date + timedelta(days=7)

        query = f"SELECT * FROM Policy_Holder WHERE ExpiryDate BETWEEN '{current_date}' AND '{seven_days_from_now}'"

        cursor.execute(query)

        due_policies = cursor.fetchall()

        if due_policies:
            print("Policy Holders with Due Dates within the Next 7 Days:")
            for policy in due_policies:
                print(f"Holder ID: {policy[0]}")
                print(f"Customer ID: {policy[1]}")
                print(f"Home Policy ID: {policy[2]}")
                print(f"Auto Policy ID: {policy[3]}")
                print(f"Status of Policy: {policy[4]}")
                print(f"Start Date: {policy[5]}")
                print(f"Expiry Date: {policy[6]}")
                print(f"Renew Date: {policy[7]}")
                print(f"At Risk Flag: {policy[8]}")
                print(f"Agent ID: {policy[9]}")
                print("-----")

        else:
            print("No policies with due dates within the next 7 days.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Closing the cursor
        cursor.close()



#For the make_payment method, another method has to be defined which will extractd details needed in make_payment method
def get_policy_holder_id(connection, customer_id, policy_type):
    try:
        cursor = connection.cursor()

        # Determine whether it's an Auto Policy or Home Policy
        policy_column = 'Auto_Policy_id' if policy_type.lower() == 'auto' else 'Home_Policy_id'

        # Query to get Holder_id based on Customer_id and Policy_Type
        query = f"SELECT Holder_id FROM Policy_Holder WHERE Customer_id = {customer_id} AND {policy_column} = {policy_id}"

        cursor.execute(query)
        holder_id = cursor.fetchone()

        return holder_id[0] if holder_id else None

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()

def make_payment(connection, policy_id, customer_id):
    try:
        cursor = connection.cursor()
        amount = int(input("Enter the amount: "))
        policy_type = input("Enter Policy Type: Auto or Home: ")

        # Get the current date
        current_date = datetime.now().date()

        # Get Holder_id based on Customer_id and Policy_Type
        holder_id = get_policy_holder_id(connection, customer_id, policy_type)

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

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
