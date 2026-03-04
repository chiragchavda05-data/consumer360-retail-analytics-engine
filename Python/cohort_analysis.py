import pandas as pd
from db_connection import get_engine

def run_cohort_analysis():

    engine = get_engine()

    query = """
    SELECT customer_id, order_date
    FROM retail.fact_sales
    """

    df = pd.read_sql(query, engine)

    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_month'] = df['order_date'].dt.to_period('M')
    df['cohort_month'] = df.groupby('customer_id')['order_month'].transform('min')
    df['cohort_index'] = (df['order_month'] - df['cohort_month']).apply(lambda x: x.n)

    cohort_data = df.groupby(['cohort_month', 'cohort_index'])['customer_id'].nunique().reset_index()

    cohort_table = cohort_data.pivot(index='cohort_month',
                                     columns='cohort_index',
                                     values='customer_id')

    cohort_size = cohort_table.iloc[:, 0]
    retention = cohort_table.divide(cohort_size, axis=0)

    print("✓ Cohort Analysis Completed")

    return retention