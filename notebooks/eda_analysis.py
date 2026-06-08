import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries Loaded Successfully")

nav = pd.read_csv("data/raw/02_nav_history.csv")

print(nav.head())

print("\nShape:")
print(nav.shape)

print("\nSummary Statistics:")
print(nav.describe())

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

print(aum.head())

plt.figure(figsize=(10,5))

sns.barplot(
    data=aum,
    x="fund_house",
    y="aum_crore"
)

plt.xticks(rotation=45)

plt.title("AUM by Fund House")

plt.show()

investor = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

plt.figure(figsize=(8,5))

sns.countplot(
    data=investor,
    x="age_group"
)

plt.title("Investor Age Groups")

plt.show()
sns.histplot(nav["nav"])

investor = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

plt.figure(figsize=(8,5))

sns.countplot(
    data=investor,
    x="age_group"
)

plt.title("Investor Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Investors")

plt.tight_layout()

plt.savefig(
    "reports/charts/investor_age_group_distribution.png"
)

plt.close()

print("Investor Age Group Chart Saved Successfully")