import pandas as pd


def calculate_rfm(df):
    """
    Calculate Recency, Frequency, Monetary scores
    and assign customer segments.
    """

    # Ensure date format
    df['last_purchase_date'] = pd.to_datetime(df['last_purchase_date'])

    # Analysis reference date (latest date in dataset)
    analysis_date = df['last_purchase_date'].max()

    # =========================
    # RFM METRICS
    # =========================

    # Recency (days since last purchase)
    df['recency'] = (analysis_date - df['last_purchase_date']).dt.days

    # R Score (lower recency = better score)
    df['r_score'] = pd.qcut(
        df['recency'],
        5,
        labels=[5, 4, 3, 2, 1]
    ).astype(int)

    # F Score
    df['f_score'] = pd.qcut(
        df['frequency'].rank(method='first'),
        5,
        labels=[1, 2, 3, 4, 5]
    ).astype(int)

    # M Score
    df['m_score'] = pd.qcut(
        df['monetary'],
        5,
        labels=[1, 2, 3, 4, 5]
    ).astype(int)

    # =========================
    # SEGMENT ASSIGNMENT
    # =========================

    def assign_segment(row):
        r, f, m = row['r_score'], row['f_score'], row['m_score']

        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"
        elif f >= 4 and m >= 4:
            return "Loyal Customers"
        elif r >= 4 and f <= 2:
            return "New Customers"
        elif r <= 2 and (f >= 4 or m >= 4):
            return "At Risk"
        elif r <= 2 and f <= 2:
            return "Hibernating"
        else:
            return "Potential"

    df['segment'] = df.apply(assign_segment, axis=1)

    print("✓ RFM calculation completed")

    return df