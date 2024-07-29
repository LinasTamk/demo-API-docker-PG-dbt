SELECT
    *
FROM {{ ref('stg_product')}}
ORDER BY 1