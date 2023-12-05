USE `insurit`;
DROP procedure IF EXISTS `CreateNewClaim`;

DELIMITER $$
USE `insurit`$$
CREATE PROCEDURE CreateNewClaim(
    IN p_Claim_amount INTEGER,
    IN p_Date DATE,
    IN p_Holder_id INTEGER
)
BEGIN
    INSERT INTO Claim (Claim_amount, Date, Holder_id)
    VALUES (p_Claim_amount, p_Date, p_Holder_id);
END$$

DELIMITER ;