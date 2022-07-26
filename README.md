# dbt_postgres_airbnb
A DBT project created on airbnb review and listings data from Berlin (inspired on dbtlearn.com courses)

(data obtainable at insideairbnb.com, dbtlearn.com or in raw_data folder)

# python environent set up and dbt installation

1. Create an env using the 3.8.13 version of python. If you use anaconda, like me, run the following in your terminal:
"conda create -n <environment_name> python==3.8.13"

2. Install the POSTGRES dbt connector inside the environment you created:
"pip install dbt-postgres"

3. Install the PYSCOPG2 library to create py scripts to connect to postgres. If you use anaconda, like me, run the following inside the environment:
"conda install -c conda-forge psycopg2"

# creating database and raw tables

1. Go to pgAdmin and create your "airbnb" database

2. Decompress RAW_TABLES.zip file

3. Run the script _creating_raw_tables.py_. Type your postgres username and password when required. Afterwards your tables will have been created. Replace the necessary info in the script (username, password, file path, etc.)

# create your profiles.yml file

1. create a dbt hidden directory inside your home folder

2. create a profiles.yml file inside the dbt hidden directory

3. add the content of the dbt_project_airbnb/creating_profile.txt inside ~/.dbt/profiles.yml

4. Modify the profiles.yml file with your postgres credentials and save it

# play around with your dbt project

1. dbt --version -> checks the version of dbt

2. dbt run -> runs the project locally

3. dbt deps -> runs and install packages and other dependencies

4. dbt compile -> compiles all the models, but do not run them (very useful for debugging)

5. dbt test -> runs all tests in your project

obs - check more commands on dbt official documentation: https://docs.getdbt.com/docs/building-a-dbt-project/documentation


