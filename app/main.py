import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, summary_stats, plot_boxplot


st.set_page_config(page_title="Solar Challenge Dashboard", layout="wide")

st.title("☀️ Solar Potential Explorer")
st.markdown("Compare solar potential metrics across Benin, Sierraleone, and Togo.")

# Sidebar
st.sidebar.header("Select Country")
selected_countries = st.sidebar.multiselect(
    "Choose countries to compare:",
    ["Benin", "Sierraleone", "Togo"],
    default=["Benin", "Sierraleone", "Togo"]
)

# Main Section
if selected_countries:
    data = load_data(selected_countries)
    
    st.subheader("📊 Summary Statistics")
    st.dataframe(summary_stats(data))

    st.subheader("📦 Boxplot Comparison")
    metric = st.selectbox("Select metric to compare:", ["GHI", "DNI", "DHI"])
    fig = plot_boxplot(data, metric)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please select at least one country from the sidebar.")
