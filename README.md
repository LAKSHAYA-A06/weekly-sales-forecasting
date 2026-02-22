# Walmart-demand-ForeCasting


## 📌 **Project Title**

**Walmart Weekly Sales Forecasting Using Exploratory Data Analysis and Linear Regression**

---

## 📝 **Project Overview**

This project aims to **forecast weekly sales** for Walmart stores using historical data and simple, interpretable machine learning techniques.
By leveraging **Exploratory Data Analysis (EDA)** and a **Linear Regression model**, the project identifies trends, seasonality, and key factors influencing store-level sales such as:

* Temperature
* Fuel price
* CPI (inflation index)
* Unemployment
* Holiday events
* Seasonal patterns (month, week, year)
* Past sales (lag and rolling features)

The goal is to develop a prediction pipeline that provides meaningful insights and supports retail decision-making (inventory planning, staffing, budgeting, promotions, etc.).

---

## 📂 **Dataset Description**

The dataset contains the following columns:

| Column           | Description                             |
| ---------------- | --------------------------------------- |
| **Store**        | Store ID (1–45)                         |
| **Date**         | Week-ending date                        |
| **Weekly_Sales** | Sales for the store on that week        |
| **Holiday_Flag** | 1 if the week is a holiday week, else 0 |
| **Temperature**  | Average temperature                     |
| **Fuel_Price**   | Fuel cost                               |
| **CPI**          | Consumer Price Index                    |
| **Unemployment** | Unemployment rate                       |

Total Rows: **6435**
Number of Stores: **45**

---

## 🔍 **Project Workflow**

### **1. Data Cleaning**

* Parsed `Date` column (handling mixed formats)
* Converted numeric columns properly
* Removed rows with unparseable dates
* Sorted by date and store
* Handled missing values and duplicates

### **2. Exploratory Data Analysis**

EDA included:

* Time series plot of weekly sales
* Store-level sales patterns
* Seasonal trend analysis
* Correlation heatmap
* Histogram and distribution checks
* Holiday week vs normal week comparison

Key insights:

* Holiday weeks show noticeable sales spikes
* Strong weekly and monthly seasonality
* Recent past sales strongly influence future sales

---

## 🧩 **Feature Engineering**

To prepare data for modeling, the following features were created:

### **Date-based features**

* `Year`
* `Month`
* `Week`
* `DayOfWeek`
* `IsWeekend`

### **Lag features**

* Sales from previous weeks:

  * `lag_1`, `lag_2`, `lag_4`

### **Rolling statistics**

* Moving averages capturing local trends:

  * `rolling_mean_4`, `rolling_mean_12`

These features help Linear Regression model seasonal behavior and past-sales influence.

---

## 🤖 **Modeling Approach — Linear Regression**

A **Linear Regression model** was chosen for:

* Interpretability
* Simplicity
* Baseline forecasting performance

### **Train/Test Split**

* Time-based split (last 12 weeks used as test set)
* Ensures realistic forecasting scenario

### **Performance Metrics**

* RMSE
* MAE
* R² Score
* Actual vs Predicted Sales Plot

---

## 📈 **Results**

The model successfully learned general sales patterns across stores.
Key observations:

* Recent weeks’ sales (`lag_1`, `lag_2`) were the strongest predictors
* Holiday weeks significantly increased sales
* Rolling averages improved stability
* Model captured trend direction but may under-estimate extreme spikes

This Linear Regression model serves as a strong **baseline** for future improvements.

---

## 🛠️ **How to Run the Project**

### **Step 1 — Install Required Libraries**

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

### **Step 2 — Place Dataset**

Make sure the file is named:

```
Walmart DataSet.csv
```

Place it in the same directory as your script.

### **Step 3 — Run the Script**

Execute the provided Python script:

```bash
python walmart_demand_ForeCasting.py
```
🖥️ Running the Streamlit Dashboard

Follow the steps below to launch the interactive sales forecasting dashboard.

Step 1 — Install Required Libraries

Open terminal inside the project folder and install dependencies:

```bash

pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib

```
Step 2 — Navigate to Project Folder

Open terminal and move into the project directory:
```bash
cd QEEKLY-SALES-FORECASTING

```
Step 3 — Run the Streamlit Application

Start the dashboard using:
```bash
streamlit run dashboard.py
```
If Streamlit command is not recognized, run:
```bash
python -m streamlit run dashboard.py
```
Outputs generated:

* Cleaned dataset
* EDA plots
* Model metrics
* Actual vs predicted plot
* Feature importance table
* Saved model file (`linear_regression_walmart_lr.joblib`)

---

## 🎯 **Conclusion**

This project demonstrates how combining EDA with a simple machine learning model can produce meaningful retail forecasts.
The Linear Regression approach provides:

* Clear insights into which factors affect sales
* A solid, easy-to-understand baseline forecast
* A foundation for more advanced models in the future

Overall, the project highlights the importance of data-driven forecasting for inventory optimization, staffing, budgeting, and retail strategy.

---

## 🚀 **Future Improvements**

* Add advanced models (Random Forest, XGBoost, LightGBM, SARIMAX, Prophet)
* Introduce promotional/event features
* Add store-level demographics or regional data
* Use rolling-window cross validation
* Deploy model via API or dashboard



* Walk-forward validation
* Confidence interval prediction
* Multi-store hierarchical forecasting
* Automated retraining pipeline


