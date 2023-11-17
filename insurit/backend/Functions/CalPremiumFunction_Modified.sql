DELIMITER //

CREATE FUNCTION CalculatePremium_Modified(customer_id INT, sum_assured INT, tenure INT, policy_type VARCHAR(255))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE base_premium DECIMAL(10, 2);
    DECLARE customer_age INT;

    -- Retrieve age from Customers table
    SELECT Age INTO customer_age
    FROM Customers
    WHERE Customer_id = customer_id;

    -- Assume some logic for calculating a base premium based on policy type, sum assured, and tenure
    -- You may need to customize this logic according to your business requirements
    SET base_premium = 
        CASE
            WHEN policy_type = 'AutoPolicy' THEN sum_assured * 0.02 + tenure * 100
            WHEN policy_type = 'HomePolicy' THEN sum_assured * 0.01 + tenure * 150
            ELSE 0
        END;

    -- Apply age-based adjustment to the premium
    SET base_premium = 
        CASE
            WHEN customer_age >= 18 AND customer_age <= 25 THEN base_premium * 1.2 -- 20% increase for age 18-25
            WHEN customer_age > 65 THEN base_premium * 1.5 -- 50% increase for age over 65
            ELSE base_premium
        END;

    RETURN base_premium;
END //

DELIMITER ;
