DELIMITER //

CREATE FUNCTION GetCustomersForAgent(agentID INT)
RETURNS VARCHAR(4000)
READS SQL DATA
BEGIN
    DECLARE result VARCHAR(4000);
    
    -- Implementation logic to retrieve customer details for a particular agent
    -- ...

    SELECT
        GROUP_CONCAT(CONCAT(c.Customer_id, ',', c.Name, ',', c.Phone, ',', c.Email, ',', c.Address, ',', c.Driving_License, ',',
        ph.Home_Policy_id, ',', ph.Auto_Policy_id, ',',ph.status_of_policy , ',',ph.StartDate,',',ph.ExpiryDate, ',', ph.RenewDate, ',', ph.at_risk_flag) SEPARATOR ';')
    INTO
        result
    FROM
        Customer c
    INNER JOIN
        Policy_Holder ph ON c.Customer_id = ph.Customer_id
    WHERE
        ph.Agent_id = agentID;

    RETURN result;
END //

DELIMITER ;




