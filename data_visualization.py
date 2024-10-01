import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_market_data(db_name='market_data.db'):
    conn = sqlite3.connect(db_name)
    data = pd.read_sql('SELECT * FROM market_data', conn)
    conn.close()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=data.index, y=data['close'])
    plt.title('Market Price Over Time')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()


if __name__ == "__main__":
    plot_market_data()