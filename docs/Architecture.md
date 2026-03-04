# Architecture (End-to-End Flow)

## Data Flow
1) Raw retail data (Retail.csv)
2) PostgreSQL staging and star schema
3) Python analytics pipeline
4) CSV outputs for Power BI
5) Power BI dashboards refresh from outputs

## Star Schema (PostgreSQL)
Schema: `retail`

- `stg_orders` (raw staging table)
- `fact_sales` (sales transactions)
- `dim_customer`
- `dim_product`
- `dim_date`

## Python Analytics Layer
Scripts:
- `data_loader.py` → pulls customer-level aggregated data for RFM
- `rfm_analysis.py` → RFM scoring + segments
- `cohort_analysis.py` → retention matrix
- `clv_generate.py` → CLV proxy score + rank
- `market_basket.py` → product pair frequency
- `run_pipeline.py` → runs full pipeline and generates outputs

## Output Files (Power BI Inputs)
Stored in `/data`:
- `rfm_results.csv`
- `clv_results.csv`
- `cohort_retention.csv`
- `market_basket_results.csv`

## Power BI Dashboard Pages
- Page 1: RFM Executive Overview
- Page 2: Cohort Retention Analysis
- Page 3: Strategic Customer Intelligence