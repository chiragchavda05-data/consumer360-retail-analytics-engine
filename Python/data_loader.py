import pandas as pd
from db_connection import get_engine

def load_data():
    """
    Load aggregated customer sales data
    from retail schema for RFM analysis
    """

    engine = get_engine()

    query = """
    SELECT 
        c.customer_id,
        c.customer_name,
        c.region,
        COUNT(DISTINCT fs.order_id) AS frequency,
        SUM(fs.sales) AS monetary,
        MAX(fs.order_date) AS last_purchase_date
    FROM retail.dim_customer c
    INNER JOIN retail.fact_sales fs
        ON c.customer_id = fs.customer_id
    GROUP BY 
        c.customer_id, 
        c.customer_name,
        c.region
    ORDER BY c.customer_id;
    """

    df = pd.read_sql(query, engine)

    print(f"✓ Loaded {len(df)} customers from database")

    return df