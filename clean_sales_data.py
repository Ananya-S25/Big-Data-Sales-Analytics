
import pandas as pd
from pathlib import Path

# Load original dataset
df = pd.read_excel("data/Online Retail.xlsx")

print("Original rows:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows without essential sales information
df = df.dropna(
    subset=[
        "InvoiceNo", "StockCode", "Quantity",
        "InvoiceDate", "UnitPrice", "Country"
    ]
).copy()

# Exclude cancelled invoices
df = df[
    ~df["InvoiceNo"].astype(str).str.startswith("C")
].copy()

# Keep positive sales quantities and prices
df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

# Calculate revenue in pounds sterling
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Convert invoice dates
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Add monthly analysis columns
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# Save cleaned data
Path("data").mkdir(exist_ok=True)
df.to_csv("data/cleaned_sales.csv", index=False)

print("Cleaned rows:", len(df))
print("Total revenue (£):", round(df["Revenue"].sum(), 2))
print("Unique products:", df["StockCode"].nunique())
print("Unique customers:", df["CustomerID"].nunique())
print("Saved data/cleaned_sales.csv successfully!")
