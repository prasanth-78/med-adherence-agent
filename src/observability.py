# src/observability.py
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def compute_adherence_metrics(adherence_events):
    """adherence_events: list of dicts with keys 'med', 'ts', 'status' ('on_time', 'late', 'missed')"""
    df = pd.DataFrame(adherence_events)
    if df.empty:
        return {"on_time_rate": None, "total": 0}
    df['ts'] = pd.to_datetime(df['ts'])
    total = len(df)
    on_time = (df['status'] == 'on_time').sum()
    return {"on_time_rate": float(on_time) / total, "total": int(total)}

def plot_weekly_adherence(adherence_events):
    df = pd.DataFrame(adherence_events)
    if df.empty:
        print("No adherence events yet.")
        return
    df['ts'] = pd.to_datetime(df['ts'])
    df['day'] = df['ts'].dt.date
    counts = df.groupby(['day', 'status']).size().unstack(fill_value=0)
    counts.plot(kind='bar', stacked=True)
    plt.title("Daily adherence events (status stacked)")
    plt.tight_layout()
    plt.show()
