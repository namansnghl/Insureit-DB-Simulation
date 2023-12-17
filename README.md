# Insureit - Insurance Provider Simulation

## Jump to


## System Description
InsureIt is a system developed to facilitate the sale of automobiles and homeowners' insurance to clients, 
all while effectively overseeing the interactions with agents and policyholders. It has the following features:
1. The system is a CLI-based application where clients can create accounts and browse through a list of insurances they qualify for and later purchase insurance through an agent.
2. The insurance premium is a dynamically computed value for clients, considering specific parameters related to the insured asset.
3. Agents have access to a private portal to view and manage their clients.
4. The internal leadership has access to an analytical dashboard view that shows the policy and agent performances. This view refreshes as we update the data in the tables.
5. The project places a greater emphasis on the efficiency of creating the system concerning data storage, loading, and access.
6. In addition, we also prioritize the development of helper scripts designed to facilitate the loading of data feeds and the updating of analytical views.

## Setting Up the Application
Before we can begin setting up the application, ensure that the following requirements are met:
1. **Download the application** from here to your local machine.
2. **MySQL Database and Client:**
   Make sure you have a MySQL database installed along with a client for interaction.
3. **Python Installation:**
   Ensure Python is installed on your machine.
4. **Virtual Environment:**
   Set up a virtual environment, preferably using Conda.
5. **Package Manager:**
   Have a package manager installed, such as pip or Conda.

Now, you can proceed with the following main steps to set up the project:


### Setting up Database on MySQL
To find all the SQL scripts for setup go to the local path insurit/backend/sql_scripts from the main folder Insureit-DB-Simulation on your system. This sub-folder contains all the DDL, Triggers, SP, Functions, Views, and DML scripts.
We will execute the following scripts before we start inserting data. All the below paths are relative to the sub-folder `insurit/backend/sql_scripts`:
1. **create_ddl.sql**
   - Running this script will create a schema `insurit` on the database along with DDLs of all the tables.
   - Note: This script also inserts the default credentials for the root user.
2. **Creating all Triggers**
   1. `/Triggers/gen_creds_trigg.sql`
3. **Creating all Functions**
   1. `/Functions/calPremium.sql`
   2. `/Functions/create_auth_func.sql`
   3. `/Functions/function_getcustomerdetails.sql`
4. **Creating all Stored Procedures**
   1. `/SP/CreateNewClaim_SP.sql`
   2. `/SP/addNewPolicy_SP.sql`
   3. `/SP/insertdata_sp.sql`
5. **Creating all Views**
   - a. `/Views/agentPerformance.sql`
   - b. `/Views/pending_claims.sql`
   - c. `/Views/view_my_policy.sql`

Once we have the basic setup we can insert all the data into our tables. To do so we can either login to insurit application as root user and execute the command `database --reset RESET` which inserts all the data using the stored-procedure or we can execute .sql files in the following order.
1. *customers.sql*
2. *agents.sql*
3. *autopolicy_detail.sql*
4. *homepolicy_detail.sql*
5. *finance_details.sql*
6. *loan.sql*
7. *policy_holder.sql*
8. *vehicle_details.sql*
9. *home_details.sql*
10. *transactions.sql*
11. *claim.sql*
12. *report.sql*
13. *report_details.sql*

### Setting up Conda Virtual Environment
The main folder of the project has an *`environments.yml`* file which contains a list of all the packages we need to install in the virtual environment. When working on Anaconda/Conda it is straightforward to use this file and create a virtual Environment.
In Terminal or Command Prompt run the following command `conda env create -f environments.yml`
This command uses the environments.yml file to create a new virtual environment in Anaconda - insurit_env - and downloads all the required python packages in that environment. Once it has been executed we have fulfilled all package installation requirements to run Insurit. 

`conda activate insurit_env`- with this command we can enable the virtual environment and follow steps further.

### Installing Insurit as a Package
The main folder of the project contains two setup files - `install.bat` and `install.sh`. For windows PC we will run the `install.bat` file in command prompt and for linux based system and Macs we run the command bash `install.sh` in terminal. Make sure these files are run inside the virtual environment.


## Starting the application
