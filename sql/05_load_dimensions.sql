INSERT INTO retail.dim_customer (
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
)
SELECT DISTINCT
    TRIM(customer_id),
    COALESCE(TRIM(customer_name), 'Unknown'),
    COALESCE(TRIM(segment), 'Unknown'),
    COALESCE(TRIM(country), 'Unknown'),
    COALESCE(TRIM(city), 'Unknown'),
    COALESCE(TRIM(state), 'Unknown'),
    COALESCE(postal_code, '00000'),
    COALESCE(TRIM(region), 'Unknown')
FROM retail.stg_orders
ON CONFLICT (customer_id) DO NOTHING;


INSERT INTO retail.dim_product (
    product_id,
    product_name,
    category,
    sub_category
)
SELECT DISTINCT
    TRIM(product_id),
    COALESCE(TRIM(product_name), 'Unknown'),
    COALESCE(TRIM(category), 'Unknown'),
    COALESCE(TRIM(sub_category), 'Unknown')
FROM retail.stg_orders
ON CONFLICT (product_id) DO NOTHING;


INSERT INTO retail.dim_date (
    date_id,
    year,
    month,
    day
)
SELECT DISTINCT
    order_date,
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date),
    EXTRACT(DAY FROM order_date)
FROM retail.stg_orders;
