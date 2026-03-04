import os
from data_loader import load_data
from rfm_analysis import calculate_rfm
from cohort_analysis import run_cohort_analysis
from market_basket import run_market_basket
from clv_generate import run_clv_generate, save_clv_results

DATA_PATH = "../data"

def run_full_pipeline():

    print("\n🚀 Starting Consumer360 Analytics Pipeline...\n")

    os.makedirs(DATA_PATH, exist_ok=True)

    # ======================
    # RFM
    # ======================
    df = load_data()
    df_rfm = calculate_rfm(df)
    df_rfm.to_csv(f"{DATA_PATH}/rfm_results.csv", index=False)
    print("✓ RFM results saved")
    
    # ======================
    # CLV (from RFM output)
    # ======================
    df_rfm_clv = run_clv_generate(df_rfm)
    save_clv_results(df_rfm_clv, f"{DATA_PATH}/clv_results.csv")

    # ======================
    # Cohort
    # ======================
    retention = run_cohort_analysis()
    retention.to_csv(f"{DATA_PATH}/cohort_retention.csv")
    print("✓ Cohort results saved")

    # ======================
    # Market Basket
    # ======================
    basket_df = run_market_basket()
    basket_df.to_csv(f"{DATA_PATH}/market_basket_results.csv", index=False)
    print("✓ Market Basket results saved")

    print("\n✅ PIPELINE EXECUTED SUCCESSFULLY\n")

if __name__ == "__main__":
    run_full_pipeline()