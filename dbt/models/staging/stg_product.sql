WITH RankedProducts AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY product_new_id ORDER BY product_new_id) AS rn
    FROM
        {{ ref('stg_raw_data') }}
)
SELECT
    product_new_id,
    product_id,
    category,
    sub_category,
    product_name
FROM
    RankedProducts
WHERE
    rn = 1
ORDER BY 1