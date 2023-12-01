
def insertdata(connection):
    cursor = connection.cursor()

    try:
        cursor.callproc('insertdata')
        connection.commit()
        print("Successfully inserted the data.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

#insertdata()