import pandas as pd

print("SCRIPT STARTED")

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

print(nav.head())

print("\nDaily Return Statistics:")
print(nav["daily_return"].describe())

nav.to_csv(
    "data/processed/nav_with_returns.csv",
    index=False
)

print("\nFile Saved Successfully")

# CAGR Calculation

cagr_results = []

for fund in nav["amfi_code"].unique():

    fund_data = nav[
        nav["amfi_code"] == fund
    ].sort_values("date")

    nav_start = fund_data["nav"].iloc[0]
    nav_end = fund_data["nav"].iloc[-1]

    years = (
        fund_data["date"].max()
        -
        fund_data["date"].min()
    ).days / 365.25

    cagr = (
        (nav_end / nav_start)
        ** (1 / years)
        - 1
    )

    cagr_results.append(
        [fund, cagr]
    )

cagr_df = pd.DataFrame(
    cagr_results,
    columns=[
        "amfi_code",
        "cagr"
    ]
)

print("\nTop CAGR Funds")

print(
    cagr_df
    .sort_values(
        "cagr",
        ascending=False
    )
    .head(10)
)

import os

os.makedirs("reports", exist_ok=True)

cagr_df.to_csv(
    "reports/cagr_results.csv",
    index=False
)

print(os.getcwd())
print("CAGR file saved successfully")

import numpy as np

rf = 0.065

sharpe_results = []

for fund in nav["amfi_code"].unique():

    fund_returns = nav[
        nav["amfi_code"] == fund
    ]["daily_return"].dropna()

    mean_return = fund_returns.mean()

    std_return = fund_returns.std()

    sharpe = (
        (mean_return - rf/252)
        /
        std_return
    ) * np.sqrt(252)

    sharpe_results.append(
        [fund, sharpe]
    )

sharpe_df = pd.DataFrame(
    sharpe_results,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)

print("\nTop Sharpe Ratio Funds")

print(
    sharpe_df
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(10)
)

sharpe_df.to_csv(
    "data/processed/sharpe_ratio.csv",
    index=False
)

print(
    "\nSharpe Ratio file saved successfully"
)

# Sortino Ratio
rf_daily = 0.065 / 252
sortino_results = []

for fund in nav["amfi_code"].unique():

    returns = (
        nav[nav["amfi_code"] == fund]
        ["daily_return"]
        .dropna()
    )

    downside_returns = returns[
        returns < 0
    ]

    downside_std = downside_returns.std()

    mean_return = returns.mean()

    sortino = (
        (mean_return - rf_daily)
        / downside_std
    ) * np.sqrt(252)

    sortino_results.append(
        [fund, sortino]
    )

sortino_df = pd.DataFrame(
    sortino_results,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

sortino_df = sortino_df.sort_values(
    "sortino_ratio",
    ascending=False
)

print("\nTop Sortino Funds")

print(sortino_df.head(10))

sortino_df.to_csv(
    "data/processed/sortino_ratio.csv",
    index=False
)

print(
    "\nSortino file saved successfully"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

print(benchmark.columns)
print(benchmark.head())


from scipy.stats import linregress

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

nifty50 = benchmark[
    benchmark["index_name"] == "NIFTY50"
].copy()

nifty50 = nifty50.sort_values(
    "date"
)

nifty50["benchmark_return"] = (
    nifty50["close_value"]
    .pct_change()
)

alpha_beta_results = []


for fund in nav["amfi_code"].unique():

    fund_returns = nav[
        nav["amfi_code"] == fund
    ][["date", "daily_return"]]

    merged = pd.merge(
        fund_returns,
        nifty50[
            ["date", "benchmark_return"]
        ],
        on="date",
        how="inner"
    )

    merged = merged.dropna()

    if len(merged) < 20:
        continue

    slope, intercept, r, p, stderr = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )

    beta = slope
    alpha = intercept * 252

    alpha_beta_results.append(
        [fund, alpha, beta]
    )


    alpha_beta_df = pd.DataFrame(
    alpha_beta_results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

alpha_beta_df = alpha_beta_df.sort_values(
    "alpha",
    ascending=False
)

print("\nTop Alpha Funds")

print(alpha_beta_df.head(10))

alpha_beta_df.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print(
    "\nAlpha Beta file saved successfully"
)


# Maximum Drawdown

drawdown_results = []

for fund in nav["amfi_code"].unique():

    fund_data = (
        nav[nav["amfi_code"] == fund]
        .sort_values("date")
        .copy()
    )

    fund_data["running_max"] = (
        fund_data["nav"]
        .cummax()
    )

    fund_data["drawdown"] = (
        fund_data["nav"]
        /
        fund_data["running_max"]
        - 1
    )

    max_dd = (
        fund_data["drawdown"]
        .min()
    )

    drawdown_results.append(
        [fund, max_dd]
    )

drawdown_df = pd.DataFrame(
    drawdown_results,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
)

drawdown_df = drawdown_df.sort_values(
    "max_drawdown"
)

print("\nWorst Drawdowns")

print(drawdown_df.head(10))

drawdown_df.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print(
    "\nMaximum Drawdown file saved successfully"
)

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(performance.columns)



performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

scorecard = performance[
    [
        "amfi_code",
        "scheme_name",
        "return_3yr_pct",
        "expense_ratio_pct"
    ]
].copy()

scorecard = scorecard.merge(
    sharpe_df,
    on="amfi_code"
)

scorecard = scorecard.merge(
    alpha_beta_df[
        ["amfi_code", "alpha"]
    ],
    on="amfi_code"
)

scorecard = scorecard.merge(
    drawdown_df,
    on="amfi_code"
)

scorecard["return_rank"] = (
    scorecard["return_3yr_pct"]
    .rank(pct=True)
)

scorecard["sharpe_rank"] = (
    scorecard["sharpe_ratio"]
    .rank(pct=True)
)

scorecard["alpha_rank"] = (
    scorecard["alpha"]
    .rank(pct=True)
)

scorecard["expense_rank"] = (
    (-scorecard["expense_ratio_pct"])
    .rank(pct=True)
)

scorecard["drawdown_rank"] = (
    (-scorecard["max_drawdown"])
    .rank(pct=True)
)

scorecard["fund_score"] = (

    scorecard["return_rank"] * 30 +

    scorecard["sharpe_rank"] * 25 +

    scorecard["alpha_rank"] * 20 +

    scorecard["expense_rank"] * 15 +

    scorecard["drawdown_rank"] * 10

)

scorecard = scorecard.sort_values(
    "fund_score",
    ascending=False
)

print("\nTop Fund Scorecards")

print(
    scorecard[
        [
            "scheme_name",
            "fund_score"
        ]
    ].head(10)
)

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print(
    "\nFund Scorecard saved successfully"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

print(
    benchmark["index_name"]
    .unique()
)
