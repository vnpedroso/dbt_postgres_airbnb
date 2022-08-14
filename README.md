# dbt_postgres_airbnb
A DBT project created on airbnb review and listings data from Berlin (inspired on dbtlearn.com courses)

(data obtainable at insideairbnb.com, dbtlearn.com or in raw_data folder)

# python environent set up and dbt installation

1. Create an env using the 3.8.13 version of python. If you use anaconda, like me, run the following in your terminal:
"conda create -n <environment_name> python==3.8.13"

2. Install the POSTGRES dbt connector inside the environment you created:
"pip install dbt-postgres"

3. Install the PYSCOPG2 library to create py scripts to connect to postgres. If you use anaconda, like me, run the following inside the environment:
"conda install psycopg2"

# creating database and raw tables

1. Go to pgAdmin and create your "airbnb" database

2. Decompress RAW_TABLES.zip file

3. Add your credentials to the creating_raw_tables.py, run the script once! Afterwards your tables will have been created. Replace the necessary info in the script (username, password, file path, etc.)

# start dbt project 

1. In the correct python environment, run "dbt init <project_name>"" in the chosen folder for you project

2. In "~/.dbt/" modify the "profile.yml" file to set the proper connections, database, accesses for dbt and postgres. Check https://docs.getdbt.com/reference/warehouse-profiles/postgres-profile for more information(
