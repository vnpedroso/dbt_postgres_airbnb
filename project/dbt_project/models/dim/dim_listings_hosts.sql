{{
	config(
		materialized="incremental" ,
		alias="dim_listings_hosts" ,
		schema="dev" ,
		unique_key="LISTING_HOST_ID"
	)
}}

WITH listings AS (
	SELECT * 
	FROM {{ref('dim_listings')}}
),

hosts AS (
	SELECT *
	FROM {{ref('dim_hosts')}}
)

SELECT
	listings.CREATED_AT ,
	GREATEST(listings.UPDATED_AT, hosts.UPDATED_AT) AS UPDATED_AT ,
	listings.LISTING_ID ,
	listings.LISTING_NAME ,
	listings.ROOM_TYPE ,
	listings.minimum_nights ,
	listings.PRICE ,
	listings.HOST_ID ,
	hosts.HOST_NAME ,
	hosts.IS_SUPERHOST ,
	{{dbt_utils.surrogate_key(['LISTINGS.LISTING_ID','HOSTS.HOST_ID'])}} AS LISTING_HOST_ID
FROM listings
LEFT JOIN hosts
	ON listings.HOST_ID = hosts.HOST_ID