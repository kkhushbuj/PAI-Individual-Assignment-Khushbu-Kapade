import streamlit as st
import pandas as pd

from ingestion import ingest_synthetic_data
from analytics import get_filtered_data, summary_stats, plot_trend
from data_cleaner import clean_dataframe
from utils import export_to_csv
from data_generator import COUNTRIES, METRICS

st.set_page_config(page_title="Public Health Insights", layout="wide")

st.title("🩺 Public Health Data Insights Dashboard")




st.sidebar.header("Data Generation")

num_records = st.sidebar.number_input(
    "Number of synthetic records",
    min_value=100,
    max_value=10000,
    step=100,
    value=500
)

if st.sidebar.button("Generate Synthetic Data"):
    count = ingest_synthetic_data(num_records)
    st.sidebar.success(f"{count} records generated and stored.")


st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Country",
    options=["All"] + COUNTRIES
)

metric = st.sidebar.selectbox(
    "Metric",
    options=["All"] + METRICS
)

start_date = st.sidebar.date_input("Start date", value=None)
end_date = st.sidebar.date_input("End date", value=None)


country_filter = None if country == "All" else country
metric_filter = None if metric == "All" else metric

start_date_filter = start_date.strftime("%Y-%m-%d") if start_date else None
end_date_filter = end_date.strftime("%Y-%m-%d") if end_date else None


df = get_filtered_data(
    country=country_filter,
    metric=metric_filter,
    start_date=start_date_filter,
    end_date=end_date_filter
)

df = clean_dataframe(df)


st.subheader("Filtered Data")

if df.empty:
    st.warning("No data available for selected filters.")
else:
    st.dataframe(df, use_container_width=True)

   
    st.subheader("Summary Statistics")
    stats = summary_stats(df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Count", stats["count"])
    col2.metric("Mean", round(stats["mean"], 2))
    col3.metric("Min", stats["min"])
    col4.metric("Max", stats["max"])

   
    st.subheader("Trend Over Time")

    df_plot = df.copy()
    df_plot["date"] = pd.to_datetime(df_plot["date"])
    df_plot = df_plot.sort_values("date")

    st.line_chart(
        data=df_plot,
        x="date",
        y="value",
        use_container_width=True
    )

   
    st.subheader("Export Data")

    export_name = st.text_input(
        "CSV filename",
        value="data/exported_data.csv"
    )

    if st.button("Export CSV"):
        export_to_csv(df, export_name)
        st.success(f"Data exported to {export_name}")
