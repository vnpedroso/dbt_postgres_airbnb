#necessary imports
import psycopg2


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
cpinto_raw_listings = '''
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
						FROM '<YOUR_FILE_PATH>\\RAW_LISTINGS.CSV' 
						DELIMITER ','
						CSV HEADER
					  '''

cpinto_raw_reviews = '''
						COPY RAW_REVIEWS
							(listing_id, 
							date, 
							reviewer_name, 
							comments, 
							sentiment)
						FROM '<YOUR_FILE_PATH>\\RAW_REVIEWS.CSV'
						DELIMITER ','
						CSV HEADER
					  '''

cpinto_raw_hosts = '''
						COPY RAW_HOSTS
							(id, 
							name, 
							is_superhost, 
							created_at, 
							updated_at)
						FROM '<YOUR_FILE_PATH>\\RAW_HOSTS.csv'
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

		