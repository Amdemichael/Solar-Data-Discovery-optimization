import pandas as pd
import plotly.express as px

def load_data(countries):
    df_list = []
    for country in countries:
        path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(path)
        df["Country"] = country
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

def summary_stats(df):
    stats = df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
    return stats.round(2)

def plot_boxplot(df, metric):
    fig = px.box(df, x="Country", y=metric, color="Country", title=f"{metric} Distribution by Country")
    return fig
