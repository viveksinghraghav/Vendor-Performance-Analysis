# SpiritVALS (Vendor Analytics for Liquor Sales)

This data analytics project analyzes vendor performance in liquor sales using an end-to-end workflow. Raw CSV files are ingested from Google Drive and transformed into a streamlined SQLite data mart (~10k rows from ~15M). Exploratory data analysis (EDA) and vendor-level analytics are performed in Python to deliver actionable insights for procurement and sales optimization.

---

## 📌 Project Goals

* Transform raw transactional data into an analysis‑ready SQLite database.
* Create a compact **summary table** optimized for fast iteration and visual analysis.
* Perform **EDA** to uncover vendor performance patterns and sales drivers.
* Lay groundwork for an **interactive Power BI dashboard** and a stakeholder‑friendly report.

---

## 🧱 Repository Structure

```
notebooks/
    ├── EDA.ipynb
    ├── notebook.ipynb
    └── vendor_performance_analysis.ipynb
.gitignore
get_vendor_summary.py
ingestion_db.py
LICENSE
README.md
requirements.txt
```

**What’s where**

* `ingestion_db.py` – Extracts raw data and loads it into **SQLite** using SQL DDL/DML.
* `get_vendor_summary.py` – Builds a **10k‑row vendor summary** (from \~15M rows) for analytics.
* `notebooks/` – Jupyter notebooks for EDA, visualizations, and vendor insights.
* `requirements.txt` – Python dependencies.

---

## 🗂️ Data Source

* **Drive link** (raw data): [Google Drive file](https://drive.google.com/file/d/18s64R0xY4KMSeTqpx9609KCVnvRjwKbs/view?usp=sharing)
* **Expected content:** transactional liquor sales with fields such as date, vendor, product/brand, quantity, price, outlet/region, etc. (schema inferred during ingestion).

> ⚠️ The raw file is large; the pipeline creates a compact SQLite layer for faster analysis.

---

## 🔄 Data Pipeline (ETL → Data Mart)

1. **Extract & Load**: Download the file from Drive and run `ingestion_db.py` to create a SQLite DB (`inventory.db`).
2. **Transform**: Use SQL (CTEs/indexes) to normalize types, handle nulls, and add keys.
3. **Summarize**: Run `get_vendor_summary.py` to aggregate \~15M rows into \~10k rows (vendor‑day/month/brand metrics).
4. **Analyze & Visualize**: Open notebooks to perform EDA and vendor performance analysis.

---

## ⚙️ Quickstart

```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Place/download the raw file locally (from the Drive link)
""" 
e.g., data/
    ├── begin_inventory.csv
    ├── end_inventory.csv
    ├── purchase_prices.csv
    ├── purchases.csv
    ├── sales.csv
    └── vendor_invoice.csv
"""

# 4) Build the SQLite database
python ingestion_db.py 

# 5) Create the vendor summary table for analytics
python get_vendor_summary.py 

# 6) Explore notebooks
#    notebooks/EDA.ipynb, notebooks/vendor_performance_analysis.ipynb
```
---

## 🧪 EDA & Analytics (Highlights)

- **Brands with Low Sales but High Margins:** Identified brands that may benefit from targeted promotions or pricing adjustments.
- **Top Vendors & Brands by Sales:** Ranked and visualized the leading vendors and brands based on total sales.
- **Vendor Contribution Analysis:** Top 10 vendors account for a major share of total procurement, as shown by Pareto and donut charts.
- **Bulk Purchasing Impact:** Large orders secure the lowest unit prices, confirming significant cost savings.
- **Unsold Inventory & Turnover:** Highlighted vendors with excess stock and calculated capital locked in unsold

*Notebooks:*

* [EDA.ipynb](./notebooks/EDA.ipynb) – data sanity checks, profiling, core distributions.
* [vendor_performance_analysis.ipynb](./notebooks/vendor_performance_analysis.ipynb) – KPI build‑out, vendor rankings, trend diagnostics.
* [notebook.ipynb](./notebooks/notebook.ipynb) – scratchpad/experiments supporting the final analysis.

---

## 📊 Future Scope

* **Power BI dashboard**: interactive pages for Vendor Overview, Brand Mix, Geography, and Seasonality.
* **Stakeholder report**: concise, narrative‐led write‑up for senior management.
* **Automation**: schedule ingestion & summary table refresh (e.g., cron/GitHub Actions) and CI data tests (e.g., Great Expectations).

---

## 🛠️ Tech Stack

* **Python**: pandas, numpy, matplotlib, seaborn, sqlalchemy
* **Database**: SQLite (SQL DDL/DML, indexes for performance)
* **Environment**: Jupyter notebooks

---

## ✅ Reproducibility & Performance Notes

* The **\~10k‑row summary** enables fast iteration vs. scanning \~15M rows.
* SQLite indices and typed columns materially improve query time.
* Random seeds used in any sampling steps (if applicable) are fixed for reproducibility.

---

## 📄 License

This project is released under the terms of the [**LICENSE**](./LICENSE) file in this repository.

---

## 🙋 Contact

**Author**: Mudassir Ansari  
**Role**: Final‑year Computer Engineering student • Data/ML enthusiast  
**Reach**: Open to feedback, internships, and collaboration.
