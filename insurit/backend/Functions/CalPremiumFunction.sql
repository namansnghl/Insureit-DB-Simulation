DELIMITER //

CREATE FUNCTION CalculatePremium(policy_id INT, age INT, sum_assured INT, tenure INT, policy_type VARCHAR(255))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE base_premium DECIMAL(10, 2);

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
            WHEN age >= 18 AND age <= 25 THEN base_premium * 1.2 -- 20% increase for age 18-25
            WHEN age > 65 THEN base_premium * 1.5 -- 50% increase for age over 65
            ELSE base_premium
        END;

    RETURN base_premium;
END //

DELIMITER ;
