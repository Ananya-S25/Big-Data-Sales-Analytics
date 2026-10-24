
import sqlite3
from pathlib import Path

# Connect to the database
conn = sqlite3.connect("sales.db")

# Read the saved SQL queries
sql_text = Path("sql/sales_queries.sql").read_text(
    encoding="utf-8"
)

# Split the file into individual queries
queries = [
    query.strip()
    for query in sql_text.split(";")
    if query.strip()
]

# Execute each query and display the results
for number, query in enumerate(queries, start=1):
    print(f"\n{'=' * 50}")
    print(f"QUERY {number}")
    print("=" * 50)

    try:
        cursor = conn.execute(query)
        rows = cursor.fetchall()

        # Show column names
        print([column[0] for column in cursor.description])

        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("SQL error:", error)

conn.close()
print("\nSQL analysis completed.")
