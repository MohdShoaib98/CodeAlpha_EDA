# CodeAlpha Internship, Task 2: Exploratory Data Analysis (EDA)

## Project Overview
This repository contains my submission for Task 2, Exploratory Data Analysis (EDA), for the CodeAlpha Data Analytics Internship. The aim of this task is to carry out a thorough EDA on a dataset. I will ask meaningful questions, identify trends and anomalies, test hypotheses, and find data quality issues.

For this project, I used the Electric Vehicle Population Data, which I converted to Excel format. This dataset has a variety of categorical and numerical fields, making it suitable for uncovering insights.

---
## Objectives
This project meets the Task 2 requirements:

1. Ask meaningful questions before analysis:
   - Which vehicle make is most common?
   - What is the most popular electric vehicle type?
   - Which county has the highest EV count?
   - What is the distribution of electric range?
   - Are there missing or duplicate records?

2. Explore the data structure, including variables, data types, and dimensions.
3. Identify trends, patterns, and anomalies, such as top values, frequency counts, and unusual data points.
4. Test hypotheses and validate assumptions using summary statistics and outlier detection.
5. Detect potential data issues, like missing values, duplicates, and inconsistent entries.

---
## Dataset
- **Name**: Electric Vehicle Population Data
- **Format**: Excel (`.xlsx`)
- **Rows**: ~60,000
- **Columns**: Make, Model, Model Year, Electric Range, Electric Vehicle Type, County, etc.
- **Source**: [WA State Open Data Portal](https://data.wa.gov/)

---

## Tech Stack
- **Python** for data processing
- **pandas** for data manipulation and summary statistics
- **scipy** for statistical analysis and outlier detection
- **openpyxl** for reading and writing Excel files

---
## Project Structure

CodeAlpha_EDA/
│
├── data/
│ └── ev_population.xlsx 
│
├── output/
│ └── EDA_Report.xlsx 
│
├── eda.py # Main Python script
├── requirements.txt 
└── README.md 

1️⃣ Install dependencies
       - pip install -r requirements.txt

2️⃣ Place dataset
     - Ensure ev_population.xlsx is inside the data folder.

3️⃣ Run the EDA script
     - python eda.py

📊 Output Details
     - The script generates output/EDA_Report.xlsx, which contains the following sheets:
1. Dataset Overview, including rows, columns, and memory usage.
2. Data Types, showing each column’s data type.
3. Missing Values, detailing the missing data count for each column.
4. Duplicates, listing the number of duplicate rows.
5. Top Values, featuring the five most common values for each column.
6. Numeric Summary, providing the minimum, maximum, mean, median, and quartiles for numeric columns.
7. Outlier Report, indicating the number of detected outliers for each numeric column.


🏆 Insights Example
    - From the EV dataset:
. Tesla is the most common EV make.
. King County has the largest number of EV registrations.
. The majority of EVs are Battery Electric Vehicles.
. The median electric range is about 120 miles, with some outliers exceeding 400 miles.
