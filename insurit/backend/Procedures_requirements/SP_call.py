## Install the required library first
#pip install mysql-connector-python


import mysql.connector

def read_database_config(file_path="requirements.txt"):
    with open(file_path, 'r') as file:
        config = {line.split('=')[0]: line.split('=')[1].strip() for line in file}
    return config

def add_new_policy(policy_name, policy_type, description, policy_active_flag, sum_assured, tenure, policy_table):
    config = read_database_config()

    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    cursor = connection.cursor()

    try:
        cursor.callproc('AddNewPolicy', (policy_name, policy_type, description, policy_active_flag, sum_assured, tenure, policy_table))
        connection.commit()
        print("Policy added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Take input from the user
policy_name = input("Enter policy name: ")
policy_type = input("Enter policy type: ")
description = input("Enter description: ")
policy_active_flag = input("Enter policy active flag: ")
sum_assured = int(input("Enter sum assured: "))
tenure = int(input("Enter tenure: "))
policy_table = input("Enter table name (AutoPolicy_detail or HomePolicy_detail): ")


# Call the function with user input
add_new_policy(policy_name, policy_type, description, policy_active_flag, sum_assured, tenure, policy_table)
