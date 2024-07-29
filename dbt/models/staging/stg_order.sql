
SELECT
    order_id,
    TO_CHAR(TO_DATE(order_date, 'DD/MM/YYYY'), 'YYYYMMDD') AS order_date_id,
    TO_CHAR(TO_DATE(ship_date, 'DD/MM/YYYY'), 'YYYYMMDD') AS ship_date_id,
    ship_mode,
    customer_new_id,
    product_new_id,
    cast(sum(sales) as DECIMAL(12, 2)) as sales
FROM {{ ref('stg_raw_data') }}
GROUP BY 1,2,3,4,5,6
