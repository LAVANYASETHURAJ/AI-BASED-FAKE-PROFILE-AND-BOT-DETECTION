import pandas as pd

def detect_bot_posting_behavior(data):
    data['time_gap_std'] = data['post_times'].apply(lambda times: pd.Series(times).diff().std())
    data['is_bot'] = data['time_gap_std'] < 0.5
    return data[['username', 'is_bot']]
