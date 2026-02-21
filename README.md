WEEKLY SALES FORECASTING

Project Overview

This project develops an interpretable weekly sales forecasting model for retail stores using Linear Regression. The system predicts future sales by incorporating historical sales patterns, economic indicators, and environmental factors.

The goal is to provide a transparent, scalable, and practical forecasting framework that helps retail businesses improve inventory planning, staffing decisions, and promotional strategies.

Objectives

* Develop a weekly sales forecasting model using Linear Regression.
* Incorporate external factors such as:

  * Temperature
  * Fuel Price
  * Consumer Price Index (CPI)
  * Unemployment Rate
  * Holiday indicators
* Apply time-series feature engineering using lag and rolling features.
* Implement proper time-based train–test splitting.
* Evaluate model performance using RMSE, MAE, and R² metrics.
* Analyze feature importance through regression coefficients.
* Build an interpretable forecasting pipeline suitable for real-world retail applications.

---
Methodology

Data Preprocessing

* Handling missing values
* Date-time conversion
* Sorting data chronologically
* Feature scaling (if required)

Feature Engineering

* Lag features (previous week sales)
* Rolling mean features (trend awareness)
* Calendar-based features:

  * Week
  * Month
  * Holiday flag
* External economic indicators integration

Model Development

* Linear Regression model training
* Time-based data splitting (no random shuffling)
* Model fitting using historical sales data

Model Evaluation

Performance measured using:

* **RMSE** — Root Mean Squared Error
* **MAE** — Mean Absolute Error
* **R² Score** — Goodness of fit

Interpretability

* Regression coefficients analyzed to understand feature impact
* Positive and negative sales drivers identified


Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit (for visualization/dashboard)


Evaluation Metrics

| RMSE     | Measures prediction error magnitude |
| MAE      | Average absolute prediction error   |
| R² Score | Model explanatory power             |

---
 How to Run the Project

clone Repository

```bash
git clone https://github.com/your-username/weekly-sales-forecasting.git
cd weekly-sales-forecasting
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Train Model

```bash
python src/train_model.py
```

###  Run Dashboard 

```bash
streamlit run dashboard.py
```

Example Use Cases

* Inventory planning
* Supply chain optimization
* Staffing decisions
* Promotional planning
* Demand forecasting

Key Features

✔ Interpretable ML model
✔ Time-series aware feature engineering
✔ Real-world retail factors included
✔ Scalable forecasting pipeline
✔ Business-friendly evaluation metrics

 Future Improvements

* Ridge/Lasso regularized regression
* Walk-forward validation
* Confidence interval prediction
* Multi-store hierarchical forecasting
* Automated retraining pipeline


