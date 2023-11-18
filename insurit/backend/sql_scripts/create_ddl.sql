create database IF NOT EXISTS insurit;
use insurit;

CREATE TABLE IF NOT EXISTS Customer (
  Customer_id integer PRIMARY KEY,
  Name varchar(255),
  Phone varchar(255),
  Email varchar(255),
  Address varchar(255),
  Driving_license varchar(255),
  Age integer
);

CREATE TABLE IF NOT EXISTS Secrets (
    Customer_id INTEGER PRIMARY KEY,
    USERNAME VARCHAR(10),
    SECRET VARCHAR(20),
    FOREIGN KEY (Customer_id) REFERENCES CUSTOMER(Customer_id)
);

CREATE TABLE IF NOT EXISTS Agents(
  Agent_id integer PRIMARY KEY,
  Name varchar(255),
  Email varchar(255),
  Phone varchar(255),
  Salary integer
);

CREATE TABLE AutoPolicy_detail (
    Auto_Policy_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Type VARCHAR(255),
    Description VARCHAR(255),
    Policy_active_flag VARCHAR(255),
    Sum_assured INTEGER,
    Tenure INTEGER,
    Policy_type VARCHAR(255)
);

CREATE TABLE HomePolicy_detail (
    Home_Policy_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Type VARCHAR(255),
    Description VARCHAR(255),
    Policy_active_flag VARCHAR(255),
    Sum_assured INTEGER,
    Tenure INTEGER,
    Policy_type VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS Report_Details (
  Report_id integer PRIMARY KEY,
  Date date,
  Damage_amount integer
);

CREATE TABLE IF NOT EXISTS Finance_details (
  SSN integer,
  Customer_id integer PRIMARY KEY,
  Account_Number varchar(255),
  Income integer,
  Bank_name varchar(255),
  Credit_History varchar(255),
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
); 

CREATE TABLE IF NOT EXISTS Loan(
  LoanId varchar(255) PRIMARY KEY,
  LoanType varchar(255),
  Tenure integer,
  Amount integer,
  Customer_id integer,
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
);


CREATE TABLE IF NOT EXISTS Policy_Holder (
  Holder_id integer PRIMARY KEY,
  Customer_id integer,
  Home_Policy_id integer,
  Auto_Policy_id integer,
 -- Policy_type varchar(255),
  status_of_policy varchar(255),
  StartDate date,
  ExpiryDate date,
  RenewDate date,
  at_risk_flag varchar(255),
  Agent_id integer,
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
  FOREIGN KEY (Auto_Policy_id) REFERENCES AutoPolicy_detail(Auto_Policy_id),
  FOREIGN KEY (Home_Policy_id) REFERENCES HomePolicy_detail(Home_Policy_id),
  FOREIGN KEY (Agent_id) REFERENCES Agents(Agent_id)
);


CREATE TABLE IF NOT EXISTS Vehicle_Details (
  Asset_id integer PRIMARY KEY,
  Model_type varchar(255),
  Name varchar(255),
  Manufacturer varchar(255),
  Age integer,
  Damage varchar(255),
  Owner_number integer,
  Holder_id integer,
  LoanId varchar(255),
  FOREIGN KEY (Holder_id) REFERENCES Policy_Holder(Holder_id),
  FOREIGN KEY (LoanId) REFERENCES Loan(LoanId)
);

CREATE TABLE IF NOT EXISTS Home_Details(
  Asset_id integer PRIMARY KEY,
  Address varchar(255),
  Carpet_area integer,
  Construction_type varchar(255),
  Estimated_market_value integer,
  Year_built integer,
  Holder_id integer,
  LoanId varchar(255),
  FOREIGN KEY (Holder_id) REFERENCES Policy_Holder(Holder_id),
  FOREIGN KEY (LoanId) REFERENCES Loan(LoanId)
);

CREATE TABLE IF NOT EXISTS Transactions(
  Transaction_id varchar(255) PRIMARY KEY,
  Date date,
  status_of_transaction varchar(255),
  Amount integer,
  Customer_id integer,
  Holder_id integer,
  FOREIGN KEY (Holder_id) REFERENCES Policy_Holder(Holder_id),
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
);

CREATE TABLE IF NOT EXISTS Claim(
  Claim_id integer PRIMARY KEY,
  Claim_amount integer,
  Date date,
  Holder_id integer,
  claim_status varchar(1) DEFAULT 'P',
  foreign key(Holder_id) references Policy_Holder(Holder_id)
);


CREATE TABLE IF NOT EXISTS Report(
	Report_id integer,
    Asset_id_vehicle integer,
    Asset_id_home integer,
    Claim_id integer,
    PRIMARY KEY(Report_id, Claim_id),
    FOREIGN KEY(Asset_id_vehicle) REFERENCES Vehicle_Details(Asset_id),
    FOREIGN KEY(Asset_id_home) REFERENCES Home_Details(Asset_id),
    FOREIGN KEY (Claim_id) references Claim(Claim_id)
);

commit;