use insurit;
CREATE VIEW AgentPerformance AS
SELECT
    A.Agent_id,
    A.Name AS Agent_Name,
    COUNT(DISTINCT C.Customer_id) AS Num_Customers,
    COUNT(DISTINCT PH.Holder_id) AS Num_Policies,
    SUM(T.Amount) AS Total_Sales
FROM
    Agents A
LEFT JOIN
    Policy_Holder PH ON A.Agent_id = PH.Agent_id
LEFT JOIN
    Customer C ON PH.Customer_id = C.Customer_id
LEFT JOIN
    Transactions T ON PH.Holder_id = T.Holder_id
GROUP BY
    A.Agent_id, A.Name;
