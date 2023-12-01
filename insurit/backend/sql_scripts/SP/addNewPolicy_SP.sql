USE `insurit`;
DROP procedure IF EXISTS `AddNewPolicy`;

DELIMITER $$
USE `insurit`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddNewPolicy`(
    IN policy_name VARCHAR(255),
    IN policy_type VARCHAR(255),
    IN description VARCHAR(255),
    IN policy_active_flag VARCHAR(255),
    IN sum_assured INTEGER,
    IN tenure INTEGER,
    IN policy_table VARCHAR(50)
)
BEGIN
    SET @sql_query = CONCAT(
        'INSERT INTO ', policy_table, 
        ' (Name, Type, Description, Policy_active_flag, Sum_assured, Tenure, Policy_type) VALUES (?, ?, ?, ?, ?, ?, ?)'
    );
    
    SET @p_name = policy_name;
    SET @p_type = policy_type;
    SET @p_desc = description;
    SET @p_active_flag = policy_active_flag;
    SET @p_sum_assured = sum_assured;
    SET @p_tenure = tenure;
    SET @p_table = policy_table;

    PREPARE stmt FROM @sql_query;
    EXECUTE stmt USING @p_name, @p_type, @p_desc, @p_active_flag, @p_sum_assured, @p_tenure, @p_table;
    DEALLOCATE PREPARE stmt;    

END$$

DELIMITER ;