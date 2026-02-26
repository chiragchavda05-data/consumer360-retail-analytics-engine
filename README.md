# consumer360-retail-analytics-engine

## Project Description
Consumer360 is a retail analytics project designed to help
e-commerce businesses identify high-value customers, detect
churn risks, and understand customer buying behavior using
structured data and analytics.

---

## Business Use Case
A mid-sized e-commerce retailer is facing low performance
from generic marketing campaigns. This project aims to build
a data-driven analytics foundation that enables targeted
customer engagement and informed business decisions.

---

## Project Scope
The project will be developed in multiple stages.

Current Focus:
- SQL-based data modeling
- Star schema design
- Clean and scalable database foundation

Future stages will include advanced analytics and visualization.

---

## Repository Structure
```
consumer360-retail-analytics-engine/
├── data/
│   └── retail.csv

├── sql/
│   ├── 01_create_schema.sql
│   ├── 02_create_dimension_tables.sql
│   ├── 03_create_fact_table.sql
│   ├── 04_create_staging.sql
│   ├── 05_load_dimensions.sql
│   ├── 06_load_fact.sql
│   ├── 07_analysis_queries.sql

├── python/              ✅ NEW
│   ├── 01_db_connection.py
│   ├── 02_rfm_analysis.py
│   ├── 03_clv_model.py   (later)
│
├── requirements.txt     ✅ NEW
├── README.md
└── .gitignore

```

---

## Tools & Technologies
- PostgreSQL
- pgAdmin
- Git & GitHub

---

## Development Status
Stage 1 (SQL – Data Modeling): Completed
Stage 2 (Python - Rfm Analysis): Ongoing
