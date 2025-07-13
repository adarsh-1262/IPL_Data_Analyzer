import pandas as pd

def load_data():
    deliveries = pd.read_csv("data/deliveries.csv")
    matches = pd.read_csv("data/matches.csv")
    return deliveries, matches

def export_to_csv(data, filename):
    data.to_csv(filename, index=True)
    print(f"✅ Exported to {filename} successfully.")
