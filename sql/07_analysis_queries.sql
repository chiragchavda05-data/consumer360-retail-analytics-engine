-- 1. Calculate Total Sales Revenue
-- This query returns overall revenue generated
SELECT SUM(sales) AS total_sales
FROM retail.fact_sales;

-- 2.Sales By Region
-- This query calculates total sales revenue for each region
SELECT c.region, SUM(f.sales) AS total_sales
FROM retail.fact_sales f
JOIN retail.dim_customer c
ON f.customer_id = c.customer_id
GROUP BY c.region;

-- 3. Sales By Product Category
-- This query calculates total sales revenue for each product category
SELECT p.category, SUM(f.sales) AS total_sales
FROM retail.fact_sales f
JOIN retail.dim_product p
ON f.product_id = p.product_id
GROUP BY p.category;

-- 4. Monthly Sales Trends
-- This query calculates total sales revenue for each month
SELECT d.month, SUM(f.sales) AS total_sales
FROM retail.fact_sales f
JOIN retail.dim_date d
ON f.order_date = d.date_id
GROUP BY d.month;

-- 5. Top 5 Customers By Sales
-- This query identifies the top 5 customers based on total sales revenue
SELECT customer_id, SUM(sales) AS total_spent
FROM retail.fact_sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;
