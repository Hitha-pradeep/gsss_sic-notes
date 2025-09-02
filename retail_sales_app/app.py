from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# ---------- Home Page ----------
@app.route('/')
def index():
    return render_template('index.html')

# ---------- Handle File Upload ----------
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return "No file selected"
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Process file
    df = pd.read_csv(filepath)

    # Cleaning
    df["Sales"] = df["Sales"].fillna(0)
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.set_index("Date").sort_index()
    df["Weekday"] = df.index.day_name()
    df["Month"] = df.index.month

    # Derived columns
    df["CumulativeSales"] = df.groupby("StoreID")["Sales"].cumsum()
    df["SalesCategory"] = df["Sales"].apply(
        lambda s: "High" if s >= 5000 else "Medium" if s >= 3000 else "Low"
    )

    # Summaries
    store_totals = df.groupby("StoreID")["Sales"].sum().reset_index().rename(columns={"Sales": "TotalSales"})
    weekday_avg = df.groupby("Weekday")["Sales"].mean().reset_index().rename(columns={"Sales": "AvgSalesPerDay"})
    top3_stores = store_totals.sort_values("TotalSales", ascending=False).head(3)

    # Save results
    cleaned_path = os.path.join(PROCESSED_FOLDER, "cleaned_retail_sales.csv")
    store_summary_path = os.path.join(PROCESSED_FOLDER, "store_sales_summary.csv")
    weekday_summary_path = os.path.join(PROCESSED_FOLDER, "weekday_sales_summary.csv")

    df.reset_index().to_csv(cleaned_path, index=False)
    store_totals.to_csv(store_summary_path, index=False)
    weekday_avg.to_csv(weekday_summary_path, index=False)

    # Render dashboard with data
    return render_template(
        'dashboard.html',
        tables={
            "store_totals": store_totals.to_dict(orient="records"),
            "weekday_avg": weekday_avg.to_dict(orient="records"),
            "top3": top3_stores.to_dict(orient="records")
        }
    )

# ---------- Download Processed Files ----------
@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(PROCESSED_FOLDER, filename)
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
