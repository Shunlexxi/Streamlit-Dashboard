import pandas as pd
import streamlit as st
import numpy as np

# Page title
st.set_page_config(page_title="Line Chart Dashboard", layout="wide")

st.title("📊 Sales Dashboard")

# Sample Data
dates = pd.date_range(start="2025-01-01", periods=30)
sales = np.random.randint(100, 500, size=30)

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales
})

# Sidebar filters
st.sidebar.header("Filters")

# Chart
st.subheader("Daily Sales Trend")
st.line_chart(df.set_index("Date"))

# SHow data table
with st.expander("View Raw Data"):
    st.dataframe(df)
