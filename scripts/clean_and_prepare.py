import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# === PATHS ===
RAW_CSV_PATH = r"C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data\raw_flipkart_data.csv.csv"
CLEANED_CSV_PATH = r"C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data\cleaned_data.csv"

# === LOAD CSV ===
df = pd.read_csv(RAW_CSV_PATH)
print("📌 Original columns:")
print(list(df.columns))

# === RENAME AND FILL REQUIRED COLUMNS ===
df = df.rename(columns={
    "uniq_id": "product_id",
    "brand": "brand",
    "product_name": "product_name"
})

# Add missing columns with fake/mock data
df["order_id"] = ["ORD" + str(i).zfill(5) for i in range(len(df))]
df["category"] = df["product_category_tree"].str.extract(r"'([^']+)'").fillna("General")
df["vendor_name"] = np.random.choice(["VendorX", "ShopSmart", "DealMart", "TopSeller"], size=len(df))
df["cost_price"] = np.random.randint(100, 5000, size=len(df))
df["selling_price"] = df["cost_price"] + np.random.randint(20, 500, size=len(df))
df["quantity_sold"] = np.random.randint(1, 50, size=len(df))
df["order_date"] = [datetime.today().date() - timedelta(days=random.randint(0, 365)) for _ in range(len(df))]
df["inventory_stock"] = np.random.randint(0, 200, size=len(df))

# Calculate totals and profit
df["total_sales"] = df["selling_price"] * df["quantity_sold"]
df["total_cost"] = df["cost_price"] * df["quantity_sold"]
df["profit"] = df["total_sales"] - df["total_cost"]

# Retain only required columns
required_columns = [
    "order_id", "product_id", "product_name", "brand", "category", "vendor_name",
    "cost_price", "selling_price", "quantity_sold", "order_date",
    "inventory_stock", "total_sales", "total_cost", "profit"
]
df = df[required_columns]

# Save cleaned CSV
df.to_csv(CLEANED_CSV_PATH, index=False)
print("✅ Cleaned CSV saved at:", CLEANED_CSV_PATH)
print(df.head())
