#Install the required library 
import mysql.connector

def read_database_config(file_path="requirements.txt"):
    with open(file_path, 'r') as file:
        config = {line.split('=')[0]: line.split('=')[1].strip() for line in file}
    return config

def calculate_premium(customer_id, sum_assured, tenure, policy_type):

    config = read_database_config()

    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    cursor = connection.cursor()

    try:
        # Call the CalculatePremium function
        cursor.callproc('CalculatePremium', (customer_id, sum_assured, tenure, policy_type))

        # Fetch the result from the stored function
        result = cursor.fetchone()

        if result:
            print(f"Calculated Premium: {result[0]}")
        else:
            print("Error: Unable to fetch result.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Take input from the user
customer_id = int(input("Enter customer ID: "))
sum_assured = int(input("Enter sum assured: "))
tenure = int(input("Enter tenure: "))
policy_type = input("Enter policy type (AutoPolicy or HomePolicy): ")

# Call the function with user input
calculate_premium(customer_id, sum_assured, tenure, policy_type)
