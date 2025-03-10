
# 🛒 Sales Performance Dashboard

## 📌 Project Overview
The **Sales Performance Dashboard** analyzes retail sales data to provide insights into revenue trends, customer segmentation, and product performance.  
This project covers:
- **ETL Pipeline**: Load data into PostgreSQL
- **Data Analysis**: SQL queries in Jupyter Notebook
- **Visualization**: Tableau (CSV import method)

---

## ⚙️ Installation Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/amanattar/Sales_Performance_Dashboard
cd Sales_Performance_Dashboard
```

### **2️⃣ Create a Virtual Environment**
Use **pip** to create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🗂 **Project Structure**
```
Sales_Performance_Dashboard/
│── Data/                         # Raw data files
│   ├── Sample - Superstore.csv    # Sales dataset
│── .gitignore                     # Files to ignore in GitHub
│── Data_Analysis.ipynb            # Jupyter Notebook for analysis
│── load_data.py                    # Script to load data into PostgreSQL
│── README.md                       # Project documentation
│── requirement.txt                  # Python dependencies
```

---

## **📊 Data Analysis & Processing**
1️⃣ **Load CSV into PostgreSQL**
```bash
python load_data.py
```
2️⃣ **Run SQL Queries in Jupyter Notebook**
```bash
jupyter notebook Data_Analysis.ipynb
```
3️⃣ **Export Processed Data to CSV**
```python
import pandas as pd
df.to_csv("output.csv", index=False)
```
4️⃣ **Import CSV into Tableau Public for Visualization**

- Open Sales_Dashboard.twb in Tableau Public
- Click Refresh Data if needed
- Interact with the dashboard
---

## **📊 Tableau Dashboard**
The **Tableau dashboard file (`Sales_Dashboard.twb`)** includes:
- **Revenue Trends** 📈
- **Customer Retention** 🏆
- **Top-Selling Products** 🛍️
- **Regional Sales Performance** 🌍
- **Discount vs Profitability Analysis** 💰

💡 **[View the Tableau Dashboard on Tableau Public](https://public.tableau.com/views/SalesDataAnalysis_17416292294640/SalesPerformanceDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**


## 🚀 Future Enhancements
- **Automate PostgreSQL to Tableau data pipeline**
- **Deploy a Flask API for real-time dashboard updates**
- **Implement Machine Learning for Sales Forecasting**

---

## ⭐ Contributing
If you want to contribute:
1. Fork this repo  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit changes (`git commit -m "Added feature"`)  
4. Push the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📜 License
MIT License

---

## 📬 Contact
👤 **Amanul Rahiman Attar**  
📧 Email: attar.aman29@gmail.com  
🔗 LinkedIn: [Amanul Rahiman Attar](https://www.linkedin.com/in/amanattar)  

