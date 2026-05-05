import pandas as pd
import sqlite3

# ==============================================
# 🏪 Connect to Chinook Database
# ==============================================

conn = sqlite3.connect("chinook.db")

# ==============================================
# 🧾 HOMEWORK 1 — Customer Purchases Analysis
# ==============================================

print("\n===== 🧾 HOMEWORK 1: Customer Purchases Analysis =====")

# 1️⃣ Load invoices with customer info
query_invoices = """
SELECT
    c.CustomerId,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    i.InvoiceId,
    i.Total
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId;
"""

invoice_df = pd.read_sql_query(query_invoices, conn)

# Calculate total amount spent by each customer
total_spent = (
    invoice_df.groupby(["CustomerId", "CustomerName"])["Total"]
    .sum()
    .reset_index()
    .sort_values("Total", ascending=False)
)

# Display top 5 customers
top5_customers = total_spent.head(5)
print("\nTop 5 Customers by Total Purchase Amount:\n", top5_customers)

# ==============================================
# 💿 HOMEWORK 2 — Album vs. Individual Track Purchases
# ==============================================

print("\n===== 💿 HOMEWORK 2: Album vs. Track Purchases =====")

# Load invoice line + track + album info
query_purchases = """
SELECT
    i.CustomerId,
    t.TrackId,
    t.AlbumId,
    a.Title AS AlbumTitle
FROM InvoiceLine il
JOIN Invoice i ON il.InvoiceId = i.InvoiceId
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album a ON t.AlbumId = a.AlbumId;
"""

purchase_df = pd.read_sql_query(query_purchases, conn)

# Check if customer bought full album (all tracks from that album)
# Load album track counts
album_tracks = (
    purchase_df.groupby("AlbumId")["TrackId"].nunique().reset_index()
    .rename(columns={"TrackId": "TotalAlbumTracks"})
)

# Merge with purchase data
merged_df = purchase_df.merge(album_tracks, on="AlbumId", how="left")

# Count how many unique tracks each customer bought per album
customer_album_tracks = (
    merged_df.groupby(["CustomerId", "AlbumId"])
    .agg(TracksBought=("TrackId", "nunique"), TotalAlbumTracks=("TotalAlbumTracks", "max"))
    .reset_index()
)

# Determine if full album purchased or not
customer_album_tracks["PurchaseType"] = customer_album_tracks.apply(
    lambda x: "Full Album" if x["TracksBought"] == x["TotalAlbumTracks"] else "Individual Tracks",
    axis=1
)

# Summarize per customer
customer_preference = (
    customer_album_tracks.groupby("CustomerId")["PurchaseType"]
    .apply(lambda x: "Full Album" if all(pt == "Full Album" for pt in x) else "Individual Tracks")
    .reset_index()
)

# Calculate percentages
summary = (
    customer_preference["PurchaseType"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index()
    .rename(columns={"index": "Purchase Preference", "PurchaseType": "Percentage"})
)

print("\nCustomer Purchase Preference Summary (%):\n", summary)

# ==============================================
# ✅ Close Connection
# ==============================================

conn.close()
print("\n✅ Analysis Complete.")
