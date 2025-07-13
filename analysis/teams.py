import pandas as pd

def top_winning_teams(matches, top_n=10):
    return matches["winner"].value_counts().head(top_n)