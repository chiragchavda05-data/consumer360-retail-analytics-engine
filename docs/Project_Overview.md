# Consumer360 – Retail Analytics Engine (Project Overview)

## Purpose
Consumer360 is a retail analytics system designed to convert raw transaction data into actionable business insights. It helps identify high-value customers, churn risks, retention behavior, and cross-sell opportunities.

## Business Problem
The retailer was running generic marketing campaigns without understanding:
- Who the best customers are (high value)
- Which customers are likely to churn
- How retention changes over time
- Which products are frequently purchased together

## Solution Summary
This project builds an end-to-end pipeline:
**PostgreSQL Star Schema → Python Analytics Engine → Power BI Dashboards**

Key outputs:
- RFM segmentation for every customer
- Cohort retention heatmap
- CLV proxy scoring for customer prioritization
- Market basket product-pair insights
- Automated pipeline to refresh dashboard data

## Deliverables
- Cleaned and modeled data in PostgreSQL (Star Schema)
- Python scripts for RFM, Cohort, CLV proxy, and Market Basket
- Power BI dashboard (3 pages)
- Pipeline automation script