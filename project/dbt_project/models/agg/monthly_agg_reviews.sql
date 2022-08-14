{{
	config(
		materialized="incremental" ,
		alias="monthly_agg_reviews" ,
		schema="dev",
		unique_key="DATE_SENTIMENT_ID"
	)
}}

WITH review_cte AS (
	SELECT *
	FROM {{ref('fct_reviews')}}
)

SELECT
	COUNT(*) AS REVIEW_TOTALS ,
	REVIEW_SENTIMENT ,
	TO_CHAR(REVIEW_DATE,'MM-YYYY') AS MONTH_YEAR,
	EXTRACT (MONTH FROM REVIEW_DATE) AS MONTH,
	EXTRACT (YEAR FROM REVIEW_DATE) AS YEAR,
	{{dbt_utils.surrogate_key(['EXTRACT (MONTH FROM REVIEW_DATE)',
							   'EXTRACT (YEAR FROM REVIEW_DATE)',
							   'REVIEW_SENTIMENT'])}} AS DATE_SENTIMENT_ID
FROM  review_cte
GROUP BY
	REVIEW_SENTIMENT,
	MONTH_YEAR,
	MONTH,
	YEAR,
	DATE_SENTIMENT_ID
ORDER BY
	YEAR DESC,
	MONTH DESC