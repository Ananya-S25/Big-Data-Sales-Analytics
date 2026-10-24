
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load cleaned data
df = pd.read_csv("data/cleaned_sales.csv")

# Create output folder for charts
Path("screenshots").mkdir(exist_ok=True)

# 1. Monthly revenue
monthly = df.groupby("YearMonth")["Revenue"].sum().sort_index()

print("\nMONTHLY REVENUE")
print(monthly.round(2))

# Plot monthly revenue
monthly.plot(kind="line", marker="o", figsize=(12, 5))
plt.title("Monthly Revenue Trend")
plt.xlabel("Year-Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/monthly_revenue.png")
plt.close()

# 2. Top 10 products by revenue
top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY REVENUE")
print(top_products.round(2))

top_products.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig("screenshots/top_products.png")
plt.close()

# 3. Top 10 countries by revenue
top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 COUNTRIES")
print(top_countries.round(2))

top_countries.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.tight_layout()
plt.savefig("screenshots/country_sales.png")
plt.close()

# 4. Customer purchasing patterns
customers = (
    df.dropna(subset=["CustomerID"])
    .groupby("CustomerID")
    .agg(
        TotalSpend=("Revenue", "sum"),
        TotalOrders=("InvoiceNo", "nunique"),
        TotalItems=("Quantity", "sum")
    )
    .sort_values("TotalSpend", ascending=False)
)

print("\nTOP 10 CUSTOMERS")
print(customers.head(10).round(2))

customers.to_csv("data/customer_sales.csv")

print("\nAnalysis complete. Charts saved in screenshots/.")
