SELECT
    DISTINCT customer_new_id,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
FROM {{ ref('stg_customer')}}
order by 1