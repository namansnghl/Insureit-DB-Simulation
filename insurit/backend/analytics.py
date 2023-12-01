import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Agent Performance 
def agentPerformance(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM AgentPerformance;"
    cursor.execute(query)
    result = cursor.fetchall()
    cols = ['Agent ID','Agent Name','Number of Customers','Number of Policies sold','Total Sales']
    agent_df = pd.DataFrame(result,columns=cols)
    agent_df['Total Sales'].fillna(0, inplace=True)
    agent_df['Total Sales'] = pd.to_numeric(agent_df['Total Sales'])
    print('Here is how your agents performed!')
    
    # Top 3 Agents with Maximum Sales
    top_sales_agents = agent_df.nlargest(3, 'Total Sales')

    # Top 3 Agents with Maximum Number of Customers
    top_customers_agents = agent_df.nlargest(3, 'Number of Customers')

    # Top 3 Agents with Maximum Policies Sold
    top_policies_agents = agent_df.nlargest(3, 'Number of Policies sold')

    print("Top 3 Agents with Maximum Sales:")
    print(top_sales_agents)

    print("\nTop 3 Agents with Maximum Number of Customers:")
    print(top_customers_agents)

    print("\nTop 3 Agents with Maximum Policies Sold:")
    print(top_policies_agents)
    
    # Bar Chart for Number of Customers
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Agent Name', y='Number of Customers', data=agent_df, label='Number of Customers', color='blue')
    plt.title('Number of Customers by Agent')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show

    # Bar Chart for Number of Policies sold
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Agent Name', y='Number of Policies sold', data=agent_df, label='Number of Policies sold', color='orange')
    plt.title('Number of Policies sold by Agent')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    # Pie Chart for Total Sales
    plt.figure(figsize=(8, 8))
    plt.pie(agent_df['Total Sales'], labels=agent_df['Agent Name'], autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Total Sales by Agent')
    plt.show()