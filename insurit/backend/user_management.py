# create user() --This function takes the input from the user (Customer or Agent) and then calls the respective function.
def userType(connection, n):
    if n == 1:
        createCustomer(connection)
    else:
        createAgent(connection)


# create Cust() -- This function is used to create a new customer.
def createCustomer(connection):
    cursor = connection.cursor()
    # Gather customer information from user input
    Name = input("Enter customer name:")
    Phone = input("Enter customer phone (without country code):")
    Email = input("Enter customer email:")
    Address = input("Enter customer Address:")
    Driving_license = input("Please type Yes if customer has a Driving license, otherwise No - ")
    Age = int(input("Enter customer age:"))
    # SQL query to insert customer data into the 'Customer' table
    query = """INSERT INTO 
    Customer (Name, Phone, Email, Address,Driving_license,Age) values (%s,%s,%s,%s,%s,%s)"""
    vals = (Name, Phone, Email, Address, Driving_license, Age)
    cursor.execute(query, vals)
    connection.commit()
    print('Customer registration is successful\nDefault username is first name and password is full name\n')


# create Agent() This function is used to create a new agent.
def createAgent(connection):
    cursor = connection.cursor()
    # Gather agent information from user input
    Name = input("Enter agent name:")
    Email = input("Enter agent email:")
    Phone = input("Enter agent phone (without country code):")
    Salary = int(input("Enter agent Salary:"))
    # SQL query to insert agent data into the 'Agents' table
    query = """INSERT INTO 
    Agents (Name, Email, Phone, Salary) values (%s,%s,%s,%s)"""
    vals = (Name, Email, Phone, Salary)
    cursor.execute(query, vals)
    connection.commit()
    print('---Thanks for registering. Agent registration is successful.---')
