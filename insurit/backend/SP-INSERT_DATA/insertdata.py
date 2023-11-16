import mysql.connector

def read_database_config(file_path="requirements.txt"):
    with open(file_path, 'r') as file:
        config = {line.split('=')[0]: line.split('=')[1].strip() for line in file}
    return config

def insertdata():
    config = read_database_config()

    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    cursor = connection.cursor()

    try:
        cursor.callproc('insertdata')
        connection.commit()
        print("Successfully inserted the data.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

insertdata()