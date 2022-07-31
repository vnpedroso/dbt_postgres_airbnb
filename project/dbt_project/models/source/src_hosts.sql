{{
	config(
		materialized="incremental" ,
		alias="src_hosts" ,
		schema="dev" ,
		unique_key="HOST_ID"
	)
}}

WITH RAW_HOSTS AS (
	SELECT *
	FROM AIRBNB.PUBLIC.RAW_HOSTS
)

SELECT
	ID AS HOST_ID ,
	NAME AS HOST_NAME ,
	IS_SUPERHOST ,
	CREATED_AT ,
	UPDATED_AT 
FROM 
	RAW_HOSTS