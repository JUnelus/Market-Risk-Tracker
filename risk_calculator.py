import pandas as pd
import numpy as np
from scipy.stats import norm
import sqlite3

class RiskCalculator:
    def __init__(self, confidence_level=0.95):
        self.confidence_level = confidence_level

    def get_market_data(self, db_name='market_data.db'):
        conn = sqlite3.connect(db_name)
        data = pd.read_sql('SELECT * FROM market_data', conn)
        conn.close()
        return data

    def calculate_var(self, data):
        returns = np.log(data['close'] / data['close'].shift(1)).dropna()
        var = norm.ppf(1 - self.confidence_level) * returns.std()
        return var

    def calculate_es(self, data):
        returns = np.log(data['close'] / data['close'].shift(1)).dropna()
        var = self.calculate_var(data)
        es = returns[returns < var].mean()
        return es

if __name__ == "__main__":
    calculator = RiskCalculator()
    data = calculator.get_market_data()
    var = calculator.calculate_var(data)
    es = calculator.calculate_es(data)
    print(f"Value-at-Risk: {var}")
    print(f"Expected Shortfall: {es}")