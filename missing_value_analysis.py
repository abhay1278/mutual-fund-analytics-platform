import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(df[df["yoy_growth_pct"].isnull()])