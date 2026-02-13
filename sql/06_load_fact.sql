INSERT INTO retail.fact_sales (
    order_id,
    customer_id,
    product_id,
    order_date,
    sales,
    quantity,
    discount,
    profit
)
SELECT
    TRIM(order_id),
    TRIM(customer_id),
    TRIM(product_id),
    order_date::DATE,
    sales::NUMERIC,
    quantity::INT,
    discount::NUMERIC,
    profit::NUMERIC
FROM retail.stg_orders;

