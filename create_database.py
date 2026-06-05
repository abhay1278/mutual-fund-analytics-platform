import sqlite3

conn = sqlite3.connect(
    "mutual_fund.db"
)

print("Database Created")

conn.close()