CREATE TABLE retail.dim_customer (

    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    region VARCHAR(50)

);

CREATE TABLE retail.dim_product (

    product_id VARCHAR(30) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(50),
    sub_category VARCHAR(50)

);

CREATE TABLE retail.dim_date (

    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT

);