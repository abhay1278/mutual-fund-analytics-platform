import pandas as pd
import numpy as np

nav = pd.read_csv(
    "data/processed/nav_with_returns.csv"
)

var_results = []

for fund in nav["amfi_code"].unique():

    returns = (
        nav[
            nav["amfi_code"] == fund
        ]["daily_return"]
        .dropna()
    )

    var_95 = np.percentile(
        returns,
        5
    )

    cvar_95 = returns[
        returns <= var_95
    ].mean()

    var_results.append(
        [
            fund,
            var_95,
            cvar_95
        ]
    )

var_df = pd.DataFrame(
    var_results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)

print(
    var_df.sort_values(
        "VaR_95"
    ).head()
)

var_df.to_csv(
    "data/processed/var_cvar_report.csv",
    index=False
)

print(
    "VaR/CVaR report saved"
)


import matplotlib.pyplot as plt

key_funds = [
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

plt.figure(figsize=(12,6))

for fund in key_funds:

    fund_data = nav[
        nav["amfi_code"] == fund
    ].copy()

    returns = (
        fund_data["daily_return"]
        .dropna()
    )

    rolling_sharpe = (
        returns.rolling(90).mean()
        /
        returns.rolling(90).std()
    ) * np.sqrt(252)

    plt.plot(
        rolling_sharpe.index,
        rolling_sharpe,
        label=str(fund)
    )

plt.title(
    "Rolling 90-Day Sharpe Ratio"
)

plt.xlabel(
    "Trading Days"
)

plt.ylabel(
    "Sharpe Ratio"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "data/processed/rolling_sharpe_chart.png"
)

plt.close()

print(
    "Rolling Sharpe chart saved successfully"
)




transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# First transaction date for each investor

first_txn = (
    transactions.groupby("investor_id")
    ["transaction_date"]
    .min()
    .reset_index()
)

first_txn["cohort_year"] = (
    first_txn["transaction_date"]
    .dt.year
)

transactions = transactions.merge(
    first_txn[
        ["investor_id", "cohort_year"]
    ],
    on="investor_id"
)

cohort_summary = (
    transactions.groupby("cohort_year")
    .agg(
        avg_investment=(
            "amount_inr",
            "mean"
        ),
        total_invested=(
            "amount_inr",
            "sum"
        ),
        investors=(
            "investor_id",
            "nunique"
        )
    )
)

print("\nCohort Analysis")

print(cohort_summary)

cohort_fund = (
    transactions.groupby(
        ["cohort_year", "amfi_code"]
    )
    .size()
    .reset_index(
        name="count"
    )
)

top_fund_per_cohort = (
    cohort_fund.sort_values(
        "count",
        ascending=False
    )
    .groupby("cohort_year")
    .first()
)

print("\nTop Fund Preference")

print(top_fund_per_cohort)





sip_txns = transactions[
    transactions["transaction_type"]
    == "SIP"
].copy()

sip_txns = sip_txns.sort_values(
    ["investor_id", "transaction_date"]
)

sip_results = []

for investor in sip_txns["investor_id"].unique():

    investor_data = sip_txns[
        sip_txns["investor_id"]
        == investor
    ]

    if len(investor_data) < 6:
        continue

    gaps = (
        investor_data["transaction_date"]
        .diff()
        .dt.days
        .dropna()
    )

    avg_gap = gaps.mean()

    status = (
        "At-Risk"
        if avg_gap > 35
        else "Healthy"
    )

    sip_results.append(
        [
            investor,
            avg_gap,
            status
        ]
    )

sip_continuity = pd.DataFrame(
    sip_results,
    columns=[
        "investor_id",
        "avg_gap_days",
        "status"
    ]
)

print("\nSIP Continuity Summary")

print(
    sip_continuity["status"]
    .value_counts()
)

print("\nTop At-Risk Investors")

print(
    sip_continuity[
        sip_continuity["status"]
        == "At-Risk"
    ].head()
)





holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

holdings["weight_decimal"] = (
    holdings["weight_pct"] / 100
)

hhi = (
    holdings.groupby("amfi_code")
    ["weight_decimal"]
    .apply(
        lambda x: (x**2).sum()
    )
    .reset_index()
)

hhi.columns = [
    "amfi_code",
    "HHI"
]

print("\nMost Concentrated Funds")

print(
    hhi.sort_values(
        "HHI",
        ascending=False
    ).head(10)
)

print("\nMost Diversified Funds")

print(
    hhi.sort_values(
        "HHI"
    ).head(10)
)