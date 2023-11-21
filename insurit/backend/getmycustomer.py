import mysql.connector
import pandas as pd

def read_database_config(file_path="requirements.txt"):
    with open(file_path, 'r') as file:
        config = {line.split('=')[0]: line.split('=')[1].strip() for line in file}
    return config

def getmycustomers(agent_id):
    config = read_database_config()

    connection = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],        
    database=config["database"]
    )
    
    cursor = connection.cursor()
    view = f"SELECT GetCustomersForAgent({agent_id})"
    cursor.execute(view)
    result = cursor.fetchone()[0]
    rows = [row.split(',') for row in result.split(';') if row]
    columns = ['Customer_ID', 'Name', 'Phone', 'Email', 'Address', 'Driving_License',
               'Home_Policy_ID', 'Auto_Policy_ID', 'Policy_Status', 'Start_Date', 'Expiry_Date', 'Renew_Date', 'At_Risk_Flag']
    
    df = pd.DataFrame(rows, columns=columns)
    print(df)
    cursor.close()

agent_id = int(input('Enter your agent id:'))
getmycustomers(agent_id)