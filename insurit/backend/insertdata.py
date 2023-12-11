def insertdata(connection):
    # Create a cursor to interact with the database
    cursor = connection.cursor()

    try:
        # Call the stored procedure 'insertdata' using the cursor
        cursor.callproc('insertdata')
        # Commit the changes to the database
        connection.commit()
        # Display a success message
        print("Successfully inserted the data.")
    except Exception as e:
        # If an exception occurs, display an error message
        print(f"Error: {e}")
    finally:
        cursor.close()

#insertdata()