🛒 Flipkart Vendor Analytics Project

This project analyzes Flipkart vendor performance using cleaned e-commerce product data. It includes data cleaning, database integration, exploratory data analysis (EDA) in Python, and interactive dashboarding using Power BI.

---
 Project Goals

- Understand **monthly trends** in sales and profit.
- Evaluate **vendor performance** across key metrics.
- Analyze **category-wise** sales and profitability.
- Explore **inventory vs sales** patterns.
- Build a **Power BI dashboard** for insights.

---
Tech Stack

| Tool         | Purpose                              |
| ------------ | ------------------------------------- |
| Python       | Data cleaning and EDA                 |
| Pandas       | Data manipulation                     |
| Seaborn, Matplotlib | Visualization in EDA           |
| MySQL        | Store cleaned data                    |
| Power BI     | Final dashboard and insights          |
| Git & GitHub | Version control and collaboration     |

---
Project Structure

flipkart-vendor-analytics/
├── data/
│   ├── raw\_flipkart\_data.csv
│   └── cleaned\_data.csv
├── scripts/
│   ├── clean\_and\_prepare.py
│   ├── load\_to\_mysql.py
│   ├── export\_to\_excel.py
│   └── dashboard\_query.py
├── eda/
│   └── vendor\_eda\_analysis.py
├── powerbi/
│   └── dashboard.pbix
├── README.md
└── requirements.txt

 EDA Highlights

- Total Profit by Brand
- Monthly Sales & Profit Trend
- Vendor-wise Comparison
- Inventory vs Sales Distribution
- Category Performance

---
 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/flipkart-vendor-analytics.git
   cd flipkart-vendor-analytics

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run scripts in order:

   * `clean_and_prepare.py` – clean raw data
   * `load_to_mysql.py` – push cleaned data to MySQL
   * `vendor_eda_analysis.py` – perform EDA
   * `export_to_excel.py` – prepare summary CSVs
   * Import CSVs to Power BI

---

## 🧠 Future Scope

* Integrate live Flipkart scraping (via Selenium or API)
* Add predictive insights using ML models
* Embed Gemini/ChatGPT for AI-powered vendor suggestions


---

Let me know if you'd like me to generate the `requirements.txt` file or customize the README with your name or GitHub handle.
```
