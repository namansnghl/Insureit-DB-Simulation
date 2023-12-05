import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mpld3

#Agent Performance 
def agentPerformance(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM AgentPerformance;"
    cursor.execute(query)
    result = cursor.fetchall()
    cols = ['Agent ID', 'Agent Name', 'Number of Customers', 'Number of Policies sold', 'Total Sales']
    agent_df = pd.DataFrame(result, columns=cols)
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

    # Convert top agents' information to HTML
    top_sales_agents_html = top_sales_agents.to_html()
    top_customers_agents_html = top_customers_agents.to_html()
    top_policies_agents_html = top_policies_agents.to_html()

    # Save the HTML to a file
    with open("top_agents_info.html", "w") as html_file:
        html_file.write("<h2>Top 3 Agents with Maximum Sales</h2>")
        html_file.write(top_sales_agents_html)

        html_file.write("<h2>Top 3 Agents with Maximum Number of Customers</h2>")
        html_file.write(top_customers_agents_html)

        html_file.write("<h2>Top 3 Agents with Maximum Policies Sold</h2>")
        html_file.write(top_policies_agents_html)

    # Create a single figure for all the plots
    fig, axes = plt.subplots(nrows=3, figsize=(12, 18))

    # Bar Chart for Number of Customers
    sns.barplot(x='Agent Name', y='Number of Customers', data=agent_df, label='Number of Customers', color='blue', ax=axes[0])
    axes[0].set_title('Number of Customers by Agent')
    axes[0].tick_params(axis='x', rotation=45)
    axes[0].set_xticklabels(agent_df['Agent Name'], rotation=45)
    axes[0].legend()

    # Bar Chart for Number of Policies sold
    sns.barplot(x='Agent Name', y='Number of Policies sold', data=agent_df, label='Number of Policies sold', color='orange', ax=axes[1])
    axes[1].set_title('Number of Policies sold by Agent')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].set_xticklabels(agent_df['Agent Name'], rotation=45)
    axes[1].legend()

    # Pie Chart for Total Sales
    axes[2].pie(agent_df['Total Sales'], labels=agent_df['Agent Name'], autopct='%1.1f%%', startangle=90)
    axes[2].set_title('Distribution of Total Sales by Agent')

    # Save the figure as HTML
    html_fig = mpld3.fig_to_html(fig)

    # Save the HTML to a file or display it
    with open("agent_performance.html", "w") as html_file:
        html_file.write(html_fig)

    mpld3.show()