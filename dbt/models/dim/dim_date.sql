
with date_spine as (
    select
        TO_CHAR(date_day, 'YYYYMMDD') AS date_id,
        date_day as full_date_description,
        extract(dow from date_day) as day_of_week,
        to_char(date_day, 'Month') as calendar_month,
        extract(quarter from date_day) as calendar_quarter,
        extract(year from date_day) as calendar_year,
        'F' || extract(year from date_day) || '-' || lpad(extract(month from date_day)::text, 2, '0') as fiscal_year_month,
        case when extract(dow from date_day) in (0, 6) then 'Holiday' else 'Non-Holiday' end as holiday_indicator,
        case when extract(dow from date_day) in (0, 6) then 'Weekend' else 'Weekday' end as weekday_indicator
    from {{ ref('date_spine') }}
)

select * from date_spine
