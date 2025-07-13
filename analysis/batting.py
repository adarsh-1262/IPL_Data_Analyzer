import pandas as pd

def top_run_scorers(deliveries, top_n=10):
    return deliveries.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(top_n)

def top_six_hitters(deliveries, top_n=10):
    sixes = deliveries[deliveries["batsman_runs"] == 6]
    return sixes["batter"].value_counts().head(top_n)