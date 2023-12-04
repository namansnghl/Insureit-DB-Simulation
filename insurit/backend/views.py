# View 1. view_policy() for customers
def view_policy(connection, customer_id):
    cursor = connection.cursor()
    view = f"SELECT * FROM view_my_policy WHERE Customer_id = {customer_id}"
    cursor.execute(view)
    policies = cursor.fetchall()
    list_pol = {}
    if not policies:
        print('Oops! No policies found for this user.')
    else:
        i = 0
        print(f"These are the policies you own. id {customer_id}")
        for policy in policies:
            i += 1
            if policy[2]:
                print(f"{i}. Home {policy[2]} {policy[4]}")
                list_pol[i] = [policy[2], 'Home']
            elif policy[3]:
                print(f"{i}. Auto {policy[3]} {policy[5]}")
                list_pol[i] = [policy[3], 'Auto']
    cursor.close()
    return list_pol


# view_claims()
def viewClaims(connection, customer_id):
    cursor = connection.cursor()
    query = f"SELECT c.customer_id, c.name AS Customer_Name, cl.Claim_id, cl.Claim_amount, cl.Date, cl.claim_status, cl.Holder_id from claim cl join policy_holder ph on ph.Holder_id = cl.Holder_id join customer c on c.Customer_id = ph.Customer_id WHERE c.Customer_id = {customer_id};"
    cursor.execute(query)
    claims = cursor.fetchall()
    print("Customer ID:", claims[0][0])
    print("Customer Name:", claims[0][1])
    print("\n")
    i = 0
    for claim in claims:
        i += 1
        print("---- Claim", i, "----")
        print("Claim ID:", claim[2])
        print("Claim Amount:", claim[3])
        print("Date of claim:", claim[4])
        print("Claim status:", claim[5])
        print("Holder ID:", claim[6])
        print("\n")


# show_dues() #SP NAMAN
def pendingClaims(connection):
    cursor = connection.cursor()
    sql = f"SELECT CLAIM_ID, CLAIM_AMOUNT, POLICY_STATUS, PAST_REJECTS FROM INSURIT.PENDING_CLAIMS ORDER BY CLAIM_DT ASC;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print()
    print("{: <15} | {: <15} | {: <15} | {: <15}".format("CLAIM ID", "AMOUNT", "POLICY STATUS", "PAST REJECTS"))
    print("{:-<15}|{:-<15}|{:-<15}|{:-<15}".format("", "", "", ""))
    for row in result:
        print("{: <15} | {: <15} | {: <15} | {: <15}".format(row[0], row[1], row[2], row[3]))
    cursor.close()
    print()


# show_customers() -- This is for agents and admin to show the customers.
def showCustomers(connection, agent_id):
    cursor = connection.cursor()
    view = f"SELECT GetCustomersForAgent({agent_id})"
    cursor.execute(view)
    result = cursor.fetchone()[0]
    rows = [row.split(',') for row in result.split(';') if row]
    columns = ['Customer_ID', 'Name', 'Phone', 'Email', 'Address', 'Driving_License',
               'Home_Policy_ID', 'Auto_Policy_ID', 'Policy_Status', 'Start_Date', 'Expiry_Date', 'Renew_Date',
               'At_Risk_Flag']

    df = pd.DataFrame(rows, columns=columns)
    print(df)
    cursor.close()
