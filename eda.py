import os
import sys
import pandas as pd
from scipy import stats

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

excel_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".xlsx")]
if not excel_files:
    print("❌ No Excel files found in data folder.")
    sys.exit(1)

DATA_PATH = os.path.join(DATA_DIR, excel_files[0])
REPORT_PATH = os.path.join(OUTPUT_DIR, "EDA_Report.xlsx")

def load_dataset(path):
    try:
        df = pd.read_excel(path)
        print(f"✅ Data loaded: {os.path.basename(path)} (shape: {df.shape})")
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        sys.exit(1)

def analyze_data(df):
    report_sections = {}
    overview = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Memory Usage (MB)": round(df.memory_usage(deep=True).sum()/1024**2, 3)
    }
    report_sections["Dataset Overview"] = pd.DataFrame(list(overview.items()), columns=["Metric", "Value"])
    report_sections["Data Types"] = df.dtypes.reset_index().rename(columns={"index": "Column", 0: "Data Type"})
    report_sections["Missing Values"] = df.isnull().sum().reset_index().rename(columns={"index": "Column", 0: "Missing Count"})
    report_sections["Duplicates"] = pd.DataFrame([{"Duplicate Rows": df.duplicated().sum()}])
    trends = {}
    for col in df.columns:
        top_vals = df[col].value_counts().head(5).to_dict()
        trends[col] = top_vals
    report_sections["Top Values"] = pd.DataFrame(trends).T
    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        report_sections["Numeric Summary"] = df[numeric_cols].describe()
    else:
        report_sections["Numeric Summary"] = pd.DataFrame({"Note": ["No numeric columns found"]})
    outlier_info = {}
    for col in numeric_cols:
        z_scores = stats.zscore(df[col].dropna())
        outliers = (abs(z_scores) > 3).sum()
        outlier_info[col] = {"Outlier Count": int(outliers)}
    report_sections["Outlier Report"] = pd.DataFrame(outlier_info).T if outlier_info else pd.DataFrame({"Note": ["No numeric columns"]})
    return report_sections

def save_report(sections, path):
    with pd.ExcelWriter(path) as writer:
        for name, data in sections.items():
            data.to_excel(writer, sheet_name=name[:31], index=False)
    print(f"📊 Report saved to: {path}")

def main():
    print("="*50)
    print("CodeAlpha Task 2 - Exploratory Data Analysis")
    print("="*50)
    print("\n🔍 Key Questions for EV Dataset:")
    print("1. Which vehicle make is most common?")
    print("2. What is the most popular electric vehicle type?")
    print("3. Which county has the highest EV count?")
    print("4. What is the range distribution for EVs?")
    print("5. Are there any missing or duplicate records?\n")
    df = load_dataset(DATA_PATH)
    results = analyze_data(df)
    save_report(results, REPORT_PATH)
    print("\n✅ EDA Completed Successfully")

if __name__ == "__main__":
    main()
    