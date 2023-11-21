# View 1. view_policy() for customers
def view_policy(connection,customer_id):
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
#id = int(input('Enter your customer id:'))
#print('\n')
#Calling the function
#view_my_policy(id)

# view_claims()
# show_dues() #SP NAMAN
# show_customers()