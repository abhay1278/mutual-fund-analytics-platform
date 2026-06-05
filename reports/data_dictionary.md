# Data Dictionary

## 1. fund_master

| Column             | Description                         |
| ------------------ | ----------------------------------- |
| amfi_code          | Unique AMFI scheme code             |
| fund_house         | Mutual fund company                 |
| scheme_name        | Name of the mutual fund scheme      |
| category           | Fund category (Equity, Debt, etc.)  |
| sub_category       | Fund sub-category                   |
| plan               | Direct or Regular plan              |
| launch_date        | Fund launch date                    |
| benchmark          | Benchmark index                     |
| expense_ratio_pct  | Annual fund expense ratio (%)       |
| exit_load_pct      | Exit load charged on redemption (%) |
| min_sip_amount     | Minimum SIP amount                  |
| min_lumpsum_amount | Minimum lump sum investment         |
| fund_manager       | Fund manager name                   |
| risk_category      | Risk level of fund                  |
| sebi_category_code | SEBI classification code            |

---

## 2. nav_history

| Column    | Description             |
| --------- | ----------------------- |
| amfi_code | Mutual fund scheme code |
| date      | NAV date                |
| nav       | Net Asset Value         |

---

## 3. aum_by_fund_house

| Column         | Description                          |
| -------------- | ------------------------------------ |
| date           | Reporting date                       |
| fund_house     | Fund house name                      |
| aum_lakh_crore | Assets Under Management (Lakh Crore) |
| aum_crore      | Assets Under Management (Crore)      |
| num_schemes    | Number of schemes managed            |

---

## 4. monthly_sip_inflows

| Column                    | Description                      |
| ------------------------- | -------------------------------- |
| month                     | Reporting month                  |
| sip_inflow_crore          | SIP inflow amount                |
| active_sip_accounts_crore | Active SIP accounts              |
| new_sip_accounts_lakh     | Newly registered SIP accounts    |
| sip_aum_lakh_crore        | SIP AUM                          |
| yoy_growth_pct            | Year-over-year growth percentage |

---

## 5. category_inflows

| Column           | Description       |
| ---------------- | ----------------- |
| month            | Reporting month   |
| category         | Fund category     |
| net_inflow_crore | Net inflow amount |

---

## 6. industry_folio_count

| Column              | Description     |
| ------------------- | --------------- |
| month               | Reporting month |
| total_folios_crore  | Total folios    |
| equity_folios_crore | Equity folios   |
| debt_folios_crore   | Debt folios     |
| hybrid_folios_crore | Hybrid folios   |
| others_folios_crore | Other folios    |

---

## 7. scheme_performance

| Column           | Description      |
| ---------------- | ---------------- |
| amfi_code        | Scheme code      |
| scheme_name      | Fund name        |
| return_1yr_pct   | 1-Year return    |
| return_3yr_pct   | 3-Year return    |
| return_5yr_pct   | 5-Year return    |
| alpha            | Alpha metric     |
| beta             | Beta metric      |
| sharpe_ratio     | Sharpe ratio     |
| sortino_ratio    | Sortino ratio    |
| max_drawdown_pct | Maximum drawdown |

---

## 8. investor_transactions

| Column             | Description                 |
| ------------------ | --------------------------- |
| investor_id        | Unique investor ID          |
| transaction_date   | Transaction date            |
| transaction_type   | SIP, Lumpsum, or Redemption |
| amount_inr         | Transaction amount          |
| state              | Investor state              |
| city               | Investor city               |
| age_group          | Investor age group          |
| gender             | Investor gender             |
| annual_income_lakh | Annual income               |
| kyc_status         | KYC verification status     |

---

## 9. portfolio_holdings

| Column            | Description          |
| ----------------- | -------------------- |
| amfi_code         | Scheme code          |
| stock_symbol      | Stock ticker         |
| stock_name        | Company name         |
| sector            | Industry sector      |
| weight_pct        | Portfolio weight (%) |
| market_value_cr   | Market value (Crore) |
| current_price_inr | Current stock price  |
| portfolio_date    | Portfolio date       |

---

## 10. benchmark_indices

| Column      | Description          |
| ----------- | -------------------- |
| date        | Trading date         |
| index_name  | Benchmark index name |
| close_value | Closing index value  |
