
import pandas as pd
import sqlite3

# Load cleaned sales data
df = pd.read_csv("data/cleaned_sales.csv")

# Create SQLite database and sales table
with sqlite3.connect("sales.db") as conn:
    df.to_sql("sales", conn, if_exists="replace", index=False)

print("SQLite database created successfully!")
print("Sales table is ready for SQL queries.")
