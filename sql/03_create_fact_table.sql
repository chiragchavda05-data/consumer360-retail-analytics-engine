CREATE TABLE retail.fact_sales (

    sales_id SERIAL PRIMARY KEY,

    order_id VARCHAR(30),

    customer_id VARCHAR(20),
    product_id VARCHAR(30),
    order_date DATE,

    sales NUMERIC(10,2),
    quantity INT,
    discount NUMERIC(5,2),
    profit NUMERIC(10,2),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES retail.dim_customer(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES retail.dim_product(product_id),

    CONSTRAINT fk_date
        FOREIGN KEY (order_date)
        REFERENCES retail.dim_date(date_id)

);

