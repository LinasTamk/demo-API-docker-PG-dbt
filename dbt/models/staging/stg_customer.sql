SELECT
    customer_new_id,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
FROM {{ ref('stg_raw_data') }}