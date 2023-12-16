# Insureit - Insurance Provider Simulation

## Jump to


## System Description
InsureIt is a system developed to facilitate the sale of automobiles and homeowners' insurance to clients, 
all while effectively overseeing the interactions with agents and policyholders. It has the following features:
<ol>
<li>The system is a CLI-based application where clients can create accounts and browse through a list 
of insurances they qualify for and later purchase insurance through an agent.</li>
<li>The insurance premium is a dynamically computed value for clients, considering specific 
parameters related to the insured asset.</li>
<li>Agents have access to a private portal to view and manage their clients.</li>
<li>The internal leadership has access to an analytical dashboard view which shows the policy & agent 
performances. This view refreshes as we refresh the data on the tables.</li>
<li>The project places greater emphasis on the efficiency of creating the system concerning data 
storage, loading, and access.</li>
<li>In addition, we also prioritize the development of helper scripts designed to facilitate the loading 
of data feeds and the updating of analytical views</li>
</ol>


## Setting Up the Application
Before we can begin setting up the application we need to make sure we have the following requirements met.
<ul><li>Downloaded the application from here to local.</li>
<li>MySQL Database and a client.</li>
<li>Python Installation.</li>
<li>A virtual environment preferably Conda Environment.</li>
<li>A package manager like pip or conda.</li></ul>
The following are the main steps required to be performed to set up the project.
<ul>
  <li><b>Setting up Database on MySQL</b></li>
  <li><b>Setting up Conda environment</b></li>
  <li><b>Installing Insurit</b></li>         {MAKE THIS LIKE JUMP TO}
</ul>

### Setting up Database on MySQL
To find all the SQL scripts for setup go to the local path insurit/backend/sql_scripts from the main folder Insureit-DB-Simulation on your system. This sub-folder contains all the DDL, Triggers, SP, Functions, Views, and DML scripts.
We will execute the following scripts before we start inserting data. All the below paths are relative to the sub-folder `insurit/backend/sql_scripts`:
1. create_ddl.sql - Running this script will create a schema insurit on the database along with DDLs of all the tables.
Note: This script also inserts the default credentials for root user.
2. CreatingallTriggers
a. /Triggers/gen_creds_trigg.sql
3. CreatingallFunctions
a. /Functions/calPremium.sql
b. /Functions/create_auth_func.sql
c. /Functions/function_getcustomerdetails.sql
4. CreatingallStored-Procedures
a. /SP/CreateNewClaim_SP.sql b. /SP/addNewPolicy_SP.sql
c. /SP/insertdata_sp.sql
5. CreatingallViews
a. /Views/agentPerformance.sql b. /Views/pending_claims.sql
c. /Views/view_my_policy.sql
