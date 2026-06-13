import pandas as pd

funds = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

risk_input = input(
    "Enter Risk Appetite (Low / Moderate / High): "
)

risk_map = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High"]
}

filtered = funds[
    funds["risk_grade"].isin(
        risk_map.get(
            risk_input,
            []
        )
    )
]

recommendations = (
    filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)