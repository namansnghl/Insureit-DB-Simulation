import mysql.connector

def read_database_config(file_path="requirements.txt"):
    with open(file_path, 'r') as file:
        config = {line.split('=')[0]: line.split('=')[1].strip() for line in file}
    return config

def view_my_policy(customer_id):
    config = read_database_config()

    connection = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],        
    database=config["database"]
    )
    
    cursor = connection.cursor()
    view = f"SELECT * FROM view_my_policy WHERE Customer_id = {id}" 
    cursor.execute(view)
    policies = cursor.fetchall()
    if not policies:
        print('Oops! No policies found for this customer. Try with a different Customer ID.')
    else:
        i = 0
        for policy in policies:
            i+=1
            print("---- Policy",i,"----")
            print("Holder id:",policy[0])
            print("Customer id:",policy[1])
            print("Home_Policy_id:",policy[2])
            print("Auto_Policy_id:",policy[3])
            print("Home Policy Name:",policy[4])
            print("Auto Policy Name:",policy[5])
            print("Status of policy:",policy[6])
            print("Start Date:",policy[7])
            print("Expiry Date:",policy[8])
            print("Renew Date:",policy[9])
            print("at_risk_flag:",policy[10])
            print("Agent_id:",policy[11])
            print("\n")
    cursor.close()

#Taking input from the customer
id = int(input('Enter your customer id:'))
print('\n')
#Calling the function
view_my_policy(id)