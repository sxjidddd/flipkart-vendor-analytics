import pandas as pd
import mysql.connector

# MySQL connection config
config = {
    "host": "localhost",
    "user": "root",
    "password": "S121001a",
    "database": "flipkart_vendor_db"
}

# Output Excel file path
output_path = r"C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data/vendor_data.xlsx"

try:
    conn = mysql.connector.connect(**config)
    query = "SELECT * FROM vendor_data"
    df = pd.read_sql(query, conn)

    df.to_excel(output_path, index=False)
    print(f"✅ Exported {len(df)} rows to Excel at: {output_path}")

except Exception as e:
    print("❌ Export failed:", e)

finally:
    if conn.is_connected():
        conn.close()
        print("🔌 MySQL connection closed.")
