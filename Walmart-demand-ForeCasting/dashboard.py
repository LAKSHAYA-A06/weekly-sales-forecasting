import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Walmart Sales Forecast Dashboard",
    layout="wide"
)

st.title("📊 Walmart Demand Forecasting Dashboard")

# -------------------------------
# LOAD MODEL
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("Walmart-demand-ForeCasting/linear_regression_walmart_lr.joblib")
    return model

model = load_model()

# -------------------------------
# SIDEBAR INPUTS
# -------------------------------
st.sidebar.header("🔧 Manual Prediction")

store = st.sidebar.number_input("Store", min_value=1, step=1)
dept = st.sidebar.number_input("Department", min_value=1, step=1)
temperature = st.sidebar.number_input("Temperature")
fuel_price = st.sidebar.number_input("Fuel Price")
cpi = st.sidebar.number_input("CPI")
unemployment = st.sidebar.number_input("Unemployment")
holiday = st.sidebar.selectbox("Holiday", [0, 1])

# -------------------------------
# MANUAL PREDICTION
# -------------------------------
if st.sidebar.button("Predict Sales"):

    input_data = pd.DataFrame([[store, dept, temperature,
                                fuel_price, cpi,
                                unemployment, holiday]],
                              columns=[
                                  "Store", "Dept", "Temperature",
                                  "Fuel_Price", "CPI",
                                  "Unemployment", "IsHoliday"
                              ])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Predicted Weekly Sales: {prediction:,.2f}")

# -------------------------------
# CSV UPLOAD SECTION
# -------------------------------
st.header("📂 Upload CSV for Bulk Prediction")

uploaded_file = st.file_uploader("Upload Walmart CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    required_columns = [
        "Store", "Dept", "Temperature",
        "Fuel_Price", "CPI",
        "Unemployment", "IsHoliday"
    ]

    if all(col in df.columns for col in required_columns):

        predictions = model.predict(df[required_columns])
        df["Predicted_Sales"] = predictions

        st.subheader("✅ Predictions Added")
        st.dataframe(df.head())

        # -------------------------------
        # ACTUAL VS PREDICTED GRAPH
        # -------------------------------
        if "Weekly_Sales" in df.columns:

            st.subheader("📈 Actual vs Predicted Sales")

            fig, ax = plt.subplots()

            ax.plot(df["Weekly_Sales"].values,
                    label="Actual Sales")

            ax.plot(df["Predicted_Sales"].values,
                    label="Predicted Sales")

            ax.legend()
            ax.set_xlabel("Records")
            ax.set_ylabel("Sales")

            st.pyplot(fig)

        # -------------------------------
        # STORE DROPDOWN FILTER
        # -------------------------------
        st.subheader("🏬 Store-wise Analysis")

        selected_store = st.selectbox(
            "Select Store",
            df["Store"].unique()
        )

        store_df = df[df["Store"] == selected_store]

        st.write(f"Showing data for Store {selected_store}")

        # -------------------------------
        # SALES TREND GRAPH
        # -------------------------------
        st.subheader("📊 Sales Trend")

        fig2, ax2 = plt.subplots()

        if "Weekly_Sales" in store_df.columns:
            ax2.plot(store_df["Weekly_Sales"].values,
                     label="Actual")

        ax2.plot(store_df["Predicted_Sales"].values,
                 label="Predicted")

        ax2.legend()
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Sales")

        st.pyplot(fig2)

        # -------------------------------
        # DOWNLOAD RESULTS
        # -------------------------------
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download Predictions CSV",
            csv,
            "predicted_sales.csv",
            "text/csv"
        )

    else:
        st.error("❌ CSV missing required columns!")
