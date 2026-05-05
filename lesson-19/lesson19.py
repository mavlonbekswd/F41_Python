import pandas as pd
import sqlite3
import numpy as np

# ==============================================
# 🏪 HOMEWORK 1: Analyzing Sales Data
# ==============================================

print("\n===== 🏪 HOMEWORK 1: Analyzing Sales Data =====")

sales_df = pd.read_csv("task/sales_data.csv")

# 1️⃣ Group by Category and calculate aggregates
category_stats = sales_df.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
)
print("\n1️⃣ Category-level Statistics:\n", category_stats)

# 2️⃣ Identify top-selling product in each category
top_products = (
    sales_df.groupby(["Category", "Product"])["Quantity"]
    .sum()
    .reset_index()
    .sort_values(["Category", "Quantity"], ascending=[True, False])
    .groupby("Category")
    .first()
)
print("\n2️⃣ Top-selling Product in Each Category:\n", top_products)

# 3️⃣ Find date with highest total sales (Quantity * Price)
sales_df["TotalSales"] = sales_df["Quantity"] * sales_df["Price"]
date_sales = sales_df.groupby("Date")["TotalSales"].sum().reset_index()
max_sales_date = date_sales.loc[date_sales["TotalSales"].idxmax()]
print("\n3️⃣ Date with Highest Total Sales:\n", max_sales_date)


# ==============================================
# 👥 HOMEWORK 2: Examining Customer Orders
# ==============================================

print("\n===== 👥 HOMEWORK 2: Customer Orders =====")

orders_df = pd.read_csv("task/customer_orders.csv")

# 1️⃣ Customers with ≥20 orders
orders_per_customer = orders_df.groupby("CustomerID")["OrderID"].count().reset_index()
active_customers = orders_per_customer[orders_per_customer["OrderID"] >= 20]
print("\n1️⃣ Customers with ≥20 Orders:\n", active_customers)

# 2️⃣ Customers with average product price > $120
avg_price_per_customer = orders_df.groupby("CustomerID")["Price"].mean().reset_index()
high_value_customers = avg_price_per_customer[avg_price_per_customer["Price"] > 120]
print("\n2️⃣ Customers with Average Price > $120:\n", high_value_customers)

# 3️⃣ Total quantity & price per product, filter total quantity <5
product_summary = orders_df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
).reset_index()
filtered_products = product_summary[product_summary["total_quantity"] >= 5]
print("\n3️⃣ Product Summary (Filtered by Quantity ≥5):\n", filtered_products)


# ==============================================
# 🌍 HOMEWORK 3: Population Salary Analysis
# ==============================================

print("\n===== 🌍 HOMEWORK 3: Population Salary Analysis =====")

# Connect to SQLite database
conn = sqlite3.connect("task/population.db")

# Read population data
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

print("\nPopulation Data Loaded Successfully!")
print(population_df.head())

# Read Excel Salary Band file
salary_bands = pd.read_excel("task/population_salary_analysis.xlsx")
print("\nSalary Band Table:\n", salary_bands)

# Define salary ranges manually
salary_ranges = [
    (0, 200000),
    (200001, 400000),
    (400001, 600000),
    (600001, 800000),
    (800001, 1000000),
    (1000001, 1200000),
    (1200001, 1400000),
    (1400001, 1600000),
    (1600001, 1800000),
    (1800001, float('inf'))
]

band_labels = salary_bands["Salary Band"]

# Assign Salary Band to each record
population_df["Salary Band"] = pd.cut(
    population_df["Salary"],
    bins=[r[0] for r in salary_ranges] + [salary_ranges[-1][1]],
    labels=band_labels,
    include_lowest=True
)

# Calculate overall stats per band
band_stats = population_df.groupby("Salary Band").agg(
    Percentage=("Salary", lambda x: round(len(x) / len(population_df) * 100, 2)),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median"),
    Population_Count=("Salary", "count")
).reset_index()

print("\n1️⃣ Overall Salary Band Statistics:\n", band_stats)

# Calculate same measures for each state
state_band_stats = population_df.groupby(["State", "Salary Band"]).agg(
    Percentage=("Salary", lambda x: round(len(x) / len(population_df) * 100, 2)),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median"),
    Population_Count=("Salary", "count")
).reset_index()

print("\n2️⃣ Salary Band Statistics by State:\n", state_band_stats.head())

# Save both outputs to Excel
with pd.ExcelWriter("task/population_salary_results.xlsx") as writer:
    band_stats.to_excel(writer, sheet_name="Overall_Stats", index=False)
    state_band_stats.to_excel(writer, sheet_name="State_Stats", index=False)

print("\n✅ Results saved to 'task/population_salary_results.xlsx'")
