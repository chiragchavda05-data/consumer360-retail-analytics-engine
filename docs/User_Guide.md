# User Guide (How to Run)

## Prerequisites
- PostgreSQL installed and running
- Python 3.x installed
- Power BI Desktop installed

## Step 1: Configure Database
Update DB credentials in:
`python/config.py`

Example:
```python
DB_CONFIG = {
  "user": "postgres",
  "password": "YOUR_PASSWORD",
  "host": "localhost",
  "port": "5432",
  "database": "consumer360_db"
}

## Step 2: Install Dependencies

Open terminal in project root and run:
pip install pandas sqlalchemy psycopg2

## Step 3: Run Full Analytics Pipeline

From project root:

cd python
python run_pipeline.py

This generates/overwrites these files inside /data:

rfm_results.csv
clv_results.csv
cohort_retention.csv
market_basket_results.csv

## Step 4: Refresh Power BI Dashboard

-Open the Power BI report file (.pbix)
-Go to Home → Refresh All
-The dashboard updates from the latest CSV outputs.

Notes (Updating Data / New Dataset)
-If a new retail dataset is provided in the same structure, load it into PostgreSQL (staging → star schema).

Then run the pipeline again:

cd python
python run_pipeline.py

Finally refresh Power BI (Home → Refresh All) to see updated results.