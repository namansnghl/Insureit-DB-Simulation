# create user() --This function takes the input from the user (Customer or Agent) and then calls the respective function.
def userType():
    print('-----Please choose your type-----')
    print('Type 1 for Agent')
    print('Type 2 for Customer')
    n = int(input('Your type?'))
    print('\n')
    if n==1:
        createCustomer()
        print('\n')
    else:
        createAgent()
        print('\n')

# create Cust() -- This function is used to create a new customer.
def createCustomer(connection):
    cursor = connection.cursor()
    Name = input("Enter your name:")
    Phone = input("Enter your phone (without country code):")
    Email = input("Enter your email:")
    Address = input("Enter your Address:")
    Driving_license = input("Please type Yes if you have a Driving license, otherwise No.")
    Age = int(input("Enter your age:"))
    query = """INSERT INTO 
    Customer (Name, Phone, Email, Address,Driving_license,Age) values (%s,%s,%s,%s,%s,%s)"""
    vals = (Name,Phone,Email,Address,Driving_license,Age)
    cursor.execute(query,vals)
    connection.commit()
    print('---Thanks for registering. Your registration is successful.---')

# create Agent() This function is used to create a new agent.
def createAgent(connection):
    cursor = connection.cursor()
    Name = input("Enter your name:")
    Email = input("Enter your email:")
    Phone = input("Enter your phone (without country code):")
    Salary = int(input("Enter your Salary:"))
    query = """INSERT INTO 
    Agents (Name, Email, Phone, Salary) values (%s,%s,%s,%s)"""
    vals = (Name, Email, Phone, Salary)
    cursor.execute(query,vals)
    connection.commit()
    print('---Thanks for registering. Agent registration is successful.---')