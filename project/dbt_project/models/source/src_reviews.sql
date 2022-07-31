{{
	config(
		materialized="incremental" ,
		alias="src_reviews" ,
		schema="dev" ,
		unique_key="LISTING_ID"
	)
}}

WITH RAW_REVIEWS AS (
	SELECT * 
	FROM AIRBNB.PUBLIC.RAW_REVIEWS
)

SELECT
	LISTING_ID ,
	DATE AS REVIEW_DATE ,
	REVIEWER_NAME ,
	COMMENTS AS REVIEW_TEXT ,
	SENTIMENT AS REVIEW_SENTIMENT 
FROM
	RAW_REVIEWS