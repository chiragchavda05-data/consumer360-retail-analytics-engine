import pandas as pd

def run_clv_generate(df_rfm: pd.DataFrame) -> pd.DataFrame:
    """
    Create CLV proxy score from RFM output.
    Keeps it simple + internship-friendly.
    """

    # safety
    df = df_rfm.copy()

    # avoid divide-by-zero
    max_freq = df["frequency"].max() if df["frequency"].max() != 0 else 1

    # Simple CLV proxy score (same idea you already used)
    # Higher monetary + higher frequency => higher CLV score
    df["clv_score"] = df["monetary"] * (1 + (df["frequency"] / max_freq))

    # Rank (1 = best)
    df["clv_rank"] = df["clv_score"].rank(ascending=False, method="dense").astype(int)

    return df


def save_clv_results(df_with_clv: pd.DataFrame, output_path: str):
    clv_cols = [
        "customer_id",
        "customer_name",
        "segment",
        "region",
        "frequency",
        "monetary",
        "last_purchase_date",
        "recency",
        "r_score",
        "f_score",
        "m_score",
        "clv_score",
        "clv_rank",
    ]

    # keep only existing cols
    clv_cols = [c for c in clv_cols if c in df_with_clv.columns]

    df_with_clv[clv_cols].to_csv(output_path, index=False)
    print(f"✓ CLV results saved: {output_path}")