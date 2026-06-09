import sqlite3
import pandas as pd

conn = sqlite3.connect("mutual_fund.db")

query = """
SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()