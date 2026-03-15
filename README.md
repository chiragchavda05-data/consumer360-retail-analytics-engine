# 📊 Consumer360 – Retail Analytics Engine (Internship Project)

Consumer360 is an end-to-end retail analytics system that converts raw retail transactions into **business-ready insights** using a **PostgreSQL Star Schema**, a **Python analytics pipeline**, and **Power BI dashboards**.  
It is designed to help businesses identify **high-value customers**, detect **churn risk**, monitor **retention**, and support **cross-sell decisions**.

---

## 🚀 Project Objectives (Business Problem)

Retail businesses often face these problems:
- They don’t know **who their best customers are**
- They don’t know **who is about to churn**
- They don’t track **retention month-by-month**
- They don’t have product-level **cross-sell intelligence**
- Reporting is manual and not refreshable

**Consumer360 solves this by providing:**
- RFM Segmentation (1–5 scoring)
- Cohort Retention Analysis (heatmap)
- CLV Proxy Scoring (customer prioritization)
- Market Basket Analysis (product pair signals)
- Automated pipeline to regenerate outputs for Power BI refresh

---

## 🛠️ Tech Stack

- **Database:** PostgreSQL  
- **Modeling:** Star Schema (Fact + Dimensions)  
- **Python:** pandas, sqlalchemy, psycopg2  
- **BI:** Power BI Desktop  
- **Automation:** `run_pipeline.py` (single-run pipeline)

---

## 📁 Repository Structure
```
consumer360-retail-analytics-engine/
├── data/
│   └── retail.csv
│
├── docs/
│ ├── Project_Overview.md
│ ├── Architecture.md
│ ├── User_Guide.md
│ ├── Insights_Summary.md
│ └── Screenshots.md
│
├── sql/
│   ├── 01_create_schema.sql
│   ├── 02_create_dimension_tables.sql
│   ├── 03_create_fact_table.sql
│   ├── 04_create_staging.sql
│   ├── 05_load_dimensions.sql
│   ├── 06_load_fact.sql
│   ├── 07_analysis_queries.sql
│
├── Python/
│ ├── config.example.py
│ ├── db_connection.py
│ ├── data_loader.py
│ ├── rfm_analysis.py
│ ├── cohort_analysis.py
│ ├── market_basket.py
│ ├── clv_generate.py
│ └── run_pipeline.py
│
├── Rfm Analysis.pbix
├── README.md
└── .gitignore

```
---
## 🧱 Week-wise Work (Week 1 to Week 4)

This project is built exactly according to the internship requirements.

### ✅ Week 1 — Data Engineering & Schema
**Goal:** Build a clean and scalable data model for analytics.

**What I did:**
- Imported raw retail dataset into PostgreSQL staging table (`retail.stg_orders`)
- Cleaned and standardized nulls, date formats, and data types
- Implemented **Star Schema**:
  - `retail.fact_sales`
  - `retail.dim_customer`
  - `retail.dim_product`
  - `retail.dim_date`
- Ensured the model is analytics-ready for Python and Power BI

---

### 🐍 Week 2 — The Logic Core (Python)
**Goal:** Build the analytics engine in Python, connected to PostgreSQL.

**What I built:**
- **Database Connection Module**
  - `Python/db_connection.py`
- **Data Loader**
  - Pulls aggregated customer-level data for RFM directly from SQL
  - `Python/data_loader.py`
- **RFM Segmentation (1–5 Scoring)**
  - Recency, Frequency, Monetary scoring using quintiles
  - Segment labels: Champions, Loyal, At Risk, Hibernating, etc.
  - `Python/rfm_analysis.py`
- **Cohort Analysis Logic**
  - Cohort month = first purchase month
  - Cohort index = month difference
  - Retention matrix generated for Power BI heatmap
  - `Python/cohort_analysis.py`
- **Market Basket Analysis**
  - Order-level product pair frequency (cross-sell signals)
  - `Python/market_basket.py`
- **CLV Proxy Generation**
  - CLV score derived from Monetary + normalized Frequency
  - Generates `clv_results.csv` for Page 3
  - `Python/clv_generate.py`

---

### 📊 Week 3 — Dashboard Construction & Validation (Power BI)
**Goal:** Build interactive dashboards and validate analytics output.

**Power BI File:** `Rfm Analysis.pbix`

**Dashboard Pages:**
1. **Page 1 – RFM Executive Summary**
   - Total Revenue, Total Customers, Avg Revenue per Customer, Total Orders
   - Customer distribution by segment
   - Revenue contribution by segment
   - Top customers table + segment slicer

2. **Page 2 – Cohort Retention & Lifecycle**
   - Retention heatmap (cohort matrix)
   - Overall retention, Month 1 retention, Best cohort retention KPIs
   - Retention trend line chart
   - Benchmarks + insights

3. **Page 3 – Strategic Customer Intelligence**
   - Total customers analyzed, Avg CLV, Total profit
   - Top high value customers
   - Profit by region and by category
   - High value distribution by region
   - Top profit sub-categories
   - Executive insights box

**Validation Performed:**
- Checked that “Champions” segment reflects high spend
- Revenue distribution and average spend are consistent with business logic

---

### 🤖 Week 4 — Automation & Handoff
**Goal:** Run full pipeline end-to-end and refresh dashboard outputs.

**What I did:**
- Created a single execution pipeline:
  - `Python/run_pipeline.py`
- Pipeline regenerates (overwrites) outputs:
  - `data/rfm_results.csv`
  - `data/clv_results.csv`
  - `data/cohort_retention.csv`
  - `data/market_basket_results.csv`
- Power BI refresh loads latest outputs (Refresh All)

---

## 📈 Output Files (Auto-Generated)

| File | Purpose |
|------|---------|
| `rfm_results.csv` | Customer-level RFM metrics + segments |
| `clv_results.csv` | CLV proxy score + rank for prioritization |
| `cohort_retention.csv` | Cohort retention matrix for heatmap |
| `market_basket_results.csv` | Frequent product pairs for cross-sell |

---

## 📌 How to Run This Project (For Anyone Cloning the Repo)

### 1) Clone the repo
```bash
git clone https://github.com/chiragchavda05-data/consumer360-retail-analytics-engine.git
cd consumer360-retail-analytics-engine
```
### 2) Setup database credentials (IMPORTANT)
This repo does NOT include real passwords.
Create your local config file:

-Copy Python/config.example.py

-Rename it to Python/config.py

Update your DB password locally

### 3) Install Python dependencies
```
pip install pandas sqlalchemy psycopg2
```

### 4) Run the full analytics pipeline
```
cd Python
python run_pipeline.py
```

### 5) Refresh Power BI dashboard

Open:
Rfm Analysis.pbix

Then:
Home → Refresh All



## 🚧 Development Status
-Stage 1 (SQL – Data Modeling): Completed ✅

-Stage 2 (Python - Rfm Analysis): Completed ✅

-Stage 3 (Power Bi - Dashboard): Completed ✅

-Stage 4 (Automataion & Validation):Completed ✅

-Project Status : **COMPLETED** ✅

## 🧑‍💻 Author
**Chirag Chavda**
