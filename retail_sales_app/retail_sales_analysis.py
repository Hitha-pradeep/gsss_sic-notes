import pandas as pd

# ------------------- Step 1 – Load Data -------------------
# Make sure retail_sales.csv is in the same folder as this script
df = pd.read_csv("retail_sales.csv")

print("First 5 rows of dataset:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nShape (rows, columns):", df.shape)

# ------------------- Step 2 – Data Cleaning -------------------
# Check missing values
print("\nMissing values before cleaning:\n", df.isna().sum())

# Fill missing Sales with 0
df["Sales"] = df["Sales"].fillna(0)

# Drop duplicates if any
df = df.drop_duplicates()

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("\nMissing values after cleaning:\n", df.isna().sum())

# ------------------- Step 3 – Time-Series Manipulation -------------------
# Set Date as index
df = df.set_index("Date").sort_index()

# Create Weekday and Month columns
df["Weekday"] = df.index.day_name()
df["Month"] = df.index.month

# ------------------- Step 4 – Filtering & Conditional Operations -------------------
# Filter StoreID = 101
store_101 = df[df["StoreID"] == 101]
print("\nSales for StoreID 101:\n", store_101.head())

# Sales > 5000
sales_gt_5000 = df[df["Sales"] > 5000]
print("\nDays with Sales > 5000:\n", sales_gt_5000.head())

# Weekends with Sales > 4000
weekends_high = df[df.index.dayofweek.isin([5, 6]) & (df["Sales"] > 4000)]
print("\nWeekends with Sales > 4000:\n", weekends_high.head())

# ------------------- Step 5 – Grouping & Aggregations -------------------
# Group by StoreID → Total sales
store_totals = df.groupby("StoreID", as_index=False)["Sales"].sum().rename(columns={"Sales": "TotalSales"})
print("\nTotal sales by Store:\n", store_totals)

# Group by Month → Average daily sales
month_avg = df.groupby("Month", as_index=False)["Sales"].mean().rename(columns={"Sales": "AvgDailySales"})
print("\nAverage daily sales by Month:\n", month_avg)

# Group by Weekday → Average sales
weekday_avg = df.groupby("Weekday", as_index=False)["Sales"].mean().rename(columns={"Sales": "AvgSalesPerDay"})
print("\nAverage sales by Weekday:\n", weekday_avg)

# Top 3 stores by sales
top3_stores = store_totals.sort_values("TotalSales", ascending=False).head(3)
print("\nTop 3 Stores by Total Sales:\n", top3_stores)

# ------------------- Step 6 – Derived Columns -------------------
# Cumulative sales per store
df["CumulativeSales"] = df.groupby("StoreID")["Sales"].cumsum()

# Sales category
def categorize_sales(s):
    if s >= 5000:
        return "High"
    elif 3000 <= s <= 4999:
        return "Medium"
    else:
        return "Low"

df["SalesCategory"] = df["Sales"].apply(categorize_sales)

print("\nData with Derived Columns:\n", df.head())

# ------------------- Step 7 – Export Results -------------------
df.reset_index().to_csv("cleaned_retail_sales.csv", index=False)
store_totals.to_csv("store_sales_summary.csv", index=False)
weekday_avg.to_csv("weekday_sales_summary.csv", index=False)

print("\n✅ Exported cleaned_retail_sales.csv, store_sales_summary.csv, weekday_sales_summary.csv")
