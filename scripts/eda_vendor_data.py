# vendor_eda_analysis.py

"""
Step-by-step Exploratory Data Analysis (EDA) for Flipkart Vendor Data
Steps:
1. Initial EDA
2. Monthly Trends
3. Vendor Performance
4. Category Insights
5. Inventory Analysis
6. Outlier & Correlation Check
7. Prepare summary CSVs for Power BI
"""

# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the cleaned dataset
file_path = r'C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data/cleaned_data.csv'
df = pd.read_csv(file_path)
print("✅ Data loaded successfully.")

# Step 3: View basic info and shape
print("\nShape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)

# Step 4: Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 5: Basic descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Step 6: Top 5 and bottom 5 rows
print("\nTop 5 rows:")
print(df.head())

print("\nBottom 5 rows:")
print(df.tail())

# Step 7: Profit distribution
plt.figure(figsize=(8,5))
sns.histplot(df['profit'], bins=30, kde=True, color='green')
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Step 8: Sales vs Cost scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='total_cost', y='total_sales', hue='vendor_name')
plt.title('Total Sales vs Total Cost')
plt.tight_layout()
plt.show()

# Step 9: Profit by Vendor
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='vendor_name', y='profit', estimator=sum, ci=None)
plt.title('Total Profit by Vendor')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 10: Sales by Category
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='category', y='total_sales', estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 11: Monthly Sales Trend
# Convert to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
monthly_stats = df.groupby(df['order_date'].dt.to_period('M')).agg({
    'total_sales': 'sum',
    'profit': 'sum'
}).reset_index()
monthly_stats['order_date'] = monthly_stats['order_date'].astype(str)

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_stats, x='order_date', y='total_sales')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 12: Inventory Analysis (Stock vs Sales)
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='inventory_stock', y='total_sales', hue='vendor_name')
plt.title('Inventory Stock vs Total Sales')
plt.tight_layout()
plt.show()

# Step 13: Correlation Matrix
plt.figure(figsize=(10,8))
sns.heatmap(df[['cost_price','selling_price','total_sales','total_cost','profit']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Step 14: Detect Outliers in Profit
plt.figure(figsize=(8,5))
sns.boxplot(data=df, y='profit')
plt.title('Outlier Detection in Profit')
plt.tight_layout()
plt.show()

# Step 15: Prepare summary CSVs for Power BI
summary_vendor = df.groupby('vendor_name').agg({
    'total_sales': 'sum',
    'profit': 'sum',
    'quantity_sold': 'sum'
}).reset_index()
summary_vendor.to_csv(r'C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data/vendor_summary.csv', index=False)

summary_category = df.groupby('category').agg({
    'total_sales': 'sum',
    'profit': 'sum'
}).reset_index()
summary_category.to_csv(r'C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data/category_summary.csv', index=False)

summary_monthly = monthly_stats.copy()
summary_monthly.to_csv(r'C:\Users\sajid\OneDrive\Desktop\flipkart1_vendor\data/monthly_summary.csv', index=False)

print("✅ Full EDA completed. Summaries saved for Power BI.")
