with stg_raw_data as (
    select
        *,
        DENSE_RANK() over (order by category, sub_category, product_name) as product_new_id,
        DENSE_RANK() over (order by customer_id, customer_name, segment, country, city, state, postal_code, region) as customer_new_id
    from {{ source('src_smarket', 'smarket_raw') }}
)

select * from stg_raw_data