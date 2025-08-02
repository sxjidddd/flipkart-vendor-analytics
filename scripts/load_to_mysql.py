import pandas as pd
import mysql.connector
from mysql.connector import Error

# === CONFIGURATION ===
CSV_PATH = r"C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data\cleaned_data.csv"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "S121001a",
    "database": "flipkart_vendor_db"
}

# === LOAD CSV ===
try:
    df = pd.read_csv(CSV_PATH)
    print("✅ CSV loaded. Preview:")
    print(df.head())
except FileNotFoundError:
    print("❌ CSV file not found at:", CSV_PATH)
    exit()

# === CONNECT TO DATABASE ===
try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("✅ Connected to MySQL")

    insert_query = """
        INSERT INTO vendor_data (
            order_id, product_id, product_name, brand, category,
            vendor_name, cost_price, selling_price, quantity_sold,
            order_date, inventory_stock, total_sales, total_cost, profit
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Replace NaN with None for SQL compatibility
    df = df.where(pd.notnull(df), None)

    inserted_rows = 0
    for _, row in df.iterrows():
        values = tuple(row[col] for col in [
            "order_id", "product_id", "product_name", "brand", "category",
            "vendor_name", "cost_price", "selling_price", "quantity_sold",
            "order_date", "inventory_stock", "total_sales", "total_cost", "profit"
        ])
        cursor.execute(insert_query, values)
        inserted_rows += 1

    conn.commit()
    print(f"✅ Inserted {inserted_rows} rows into `vendor_data`.")

except Error as e:
    print("❌ Database error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("🔌 MySQL connection closed.")
