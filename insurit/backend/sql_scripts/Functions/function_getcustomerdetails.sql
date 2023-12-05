DELIMITER //

CREATE FUNCTION GetCustomersForAgent(agentID INT)
RETURNS VARCHAR(4000)
READS SQL DATA
BEGIN
    DECLARE result VARCHAR(4000);
    
    -- Implementation logic to retrieve customer details for a particular agent
    -- ...

    SELECT
        GROUP_CONCAT(CONCAT(c.Customer_id, ',', c.Name, ',', COALESCE(ph.Home_Policy_id, ''), ',', COALESCE(ph.Auto_Policy_id, '')) SEPARATOR ';')
    INTO
        result
    FROM
        Policy_Holder ph
    LEFT JOIN
        customer c ON c.Customer_id = ph.Customer_id
    WHERE
        ph.Agent_id = agentID;

    RETURN result;
END //

DELIMITER ;




