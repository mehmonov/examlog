import pandas as pd
import matplotlib.pyplot as plt

def generate_graph():
    df = pd.read_csv('data/daily_log.csv', names=['date', 'hours', 'vocab', 'reading', 'writing', 'math', 'tests'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.tail(14)
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['reading'], label='Reading')
    plt.plot(df['date'], df['writing'], label='Writing')
    plt.plot(df['date'], df['math'], label='Math')
    plt.legend()
    plt.title('SAT Progress (Last 14 Days)')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    path = 'data/progress_graph.png'
    plt.savefig(path)
    return path
