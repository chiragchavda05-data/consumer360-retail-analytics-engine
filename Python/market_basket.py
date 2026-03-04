import pandas as pd
from itertools import combinations
from collections import Counter

def run_market_basket():

    df = pd.read_csv("../data/Retail.csv")

    print(f"Loaded {len(df)} rows")

    basket = df.groupby('order_ID')['Product_Name'].apply(list)

    pair_counter = Counter()

    for items in basket:
        unique_items = set(items)
        pairs = combinations(unique_items, 2)
        pair_counter.update(pairs)

    basket_df = pd.DataFrame(pair_counter.items(), columns=['Product Pair', 'Count'])
    basket_df = basket_df.sort_values(by='Count', ascending=False)

    print("✓ Market Basket Analysis Completed")

    return basket_df