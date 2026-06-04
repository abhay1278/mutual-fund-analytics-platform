import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("Scheme Name:")
print(data["meta"]["scheme_name"])

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

nav_df.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("CSV Saved Successfully")