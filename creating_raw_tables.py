#necessary imports
import psycopg2
import os


#creating connection
conn = psycopg2.connect(database="airbnb", 
						user=#YOUR_USERNAME 
						password=#YOUR_PASSWORD , 
						host="localhost", 
						port= "5432")
						# obs: 5432 is the default port in postgres and 'postgres' the default user

print('\n connection created')


#creating cursor
cur = conn.cursor()

print('\n cursor created')


#testing connection
cur.execute('SELECT VERSION()')

conn_test = cur.fetchone()
print(f'\n successfully connected to: {conn_test}')


#creating path variables
basepath = os.path.abspath('./raw_data').replace('\\','\\\\')

raw_sources = {'raw_listings_path':f'{basepath}\\\\raw_listings.csv',
			   'raw_hosts_path':f'{basepath}\\\\raw_listings.csv',
			   'raw_reviews_path':f'{basepath}\\\\raw_listings.csv'
			   }

# the code below creates a path variable for each table according to the above dictionary keys
for key,val in raw_sources.items():
	exec(key + '=val')


#creating tables queries
create_raw_listings = '''
					CREATE TABLE RAW_LISTINGS
 						(id INTEGER,
						listing_url TEXT,
						name TEXT,
						room_type VARCHAR(1000),
						minimum_nights INTEGER,
						host_id INTEGER,
						price TEXT,
						created_at TIMESTAMPTZ,
						updated_at TIMESTAMPTZ)
                      '''

create_raw_reviews = '''
					CREATE TABLE RAW_REVIEWS
						(listing_id INTEGER,
						date TIMESTAMPTZ,
						reviewer_name TEXT,
						comments TEXT,
						sentiment VARCHAR(500))
                     '''

create_raw_hosts =  '''
					CREATE TABLE RAW_HOSTS
						(id INTEGER,
						name VARCHAR(1000),
						is_superhost VARCHAR(500),
						created_at TIMESTAMPTZ,
						updated_at TIMESTAMPTZ)
                     '''

print('\n table creation queries successfully created')

#copy into queries
cpinto_raw_listings = f'''
						COPY RAW_LISTINGS 
							(id,
						    listing_url,
						    name,
						    room_type,
						    minimum_nights,
						    host_id,
						    price,
						    created_at,
						    updated_at)
						FROM {raw_listings_path}
						DELIMITER ','
						CSV HEADER
					  '''

cpinto_raw_reviews = f'''
						COPY RAW_REVIEWS
							(listing_id, 
							date, 
							reviewer_name, 
							comments, 
							sentiment)
						FROM {raw_listings_reviews}
						DELIMITER ','
						CSV HEADER
					  '''

cpinto_raw_hosts = f'''
						COPY RAW_HOSTS
							(id, 
							name, 
							is_superhost, 
							created_at, 
							updated_at)
						FROM {raw_listings_hosts}
						DELIMITER ','
						CSV HEADER
					  '''

print('\n copy into queries successfully created')


#executing queries

try:	
	cur.execute(create_raw_listings)
	print(f'\n RAW_LISTINGS successfully created')
	cur.execute(cpinto_raw_listings)
	print(f'copy into RAW_LISTINGS statement was successfull')

	cur.execute(create_raw_reviews)
	print(f'\n RAW_REVIEWS successfully created')
	cur.execute(cpinto_raw_reviews)
	print(f'copy into RAW_REVIEWS statement was successfull')

	cur.execute(create_raw_hosts)
	print(f'\n RAW_HOSTS successfully created')
	cur.execute(cpinto_raw_hosts)
	print(f'copy into RAW_HOSTS statement was successfull')

	#closing connection
	cur.close()
	print('\ncursor successfully closed')
	conn.commit()
	print('connection successfully commited')
	conn.close()
	print('connection successfully closed')
except (Exception, psycopg2.DatabaseError) as error:
	print(error)
finally:
	if conn is not None:
		conn.close()

		