use insurit;
CREATE VIEW view_my_policy AS
SELECT p.Holder_id, p.Customer_id, p.Home_Policy_id, p.Auto_Policy_id, h.Name as homePolicyName, a.Name as autoPolicyName, status_of_policy, StartDate, ExpiryDate, RenewDate, at_risk_flag, Agent_id 
FROM policy_holder p
LEFT JOIN homepolicy_detail h on h.Home_Policy_id = p.Home_Policy_id
LEFT JOIN autopolicy_detail a on a.Auto_Policy_id = p.Auto_Policy_id;

