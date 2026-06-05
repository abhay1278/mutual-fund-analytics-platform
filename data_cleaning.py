import pandas as pd

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    print("\n" + "="*60)
    print("DATASET:", file)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    #Updated  

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

df["yoy_growth_pct"] = df["yoy_growth_pct"].fillna(0)

df.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)

print("Cleaning Completed")