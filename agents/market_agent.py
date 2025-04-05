# agents/market_agent.py
import sqlite3
import pandas as pd
import pandas as pd

def get_market_data():
    df = pd.read_csv("data/MarketData.csv")
    return df


class MarketAgent:
    def __init__(self, db_path="farming.db"):
        self.db_path = db_path

    def fetch_data(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM MarketData", conn)
        conn.close()
        return df

    def analyze_market(self, df):
        # Example: Market_Score = Demand_Index * 0.6 + Economic_Indicator * 0.4
        df['Market_Score'] = df['Demand_Index'] * 0.6 + df['Economic_Indicator'] * 0.4
        return df[['Market_ID', 'Product', 'Market_Price_per_ton', 'Market_Score']]

    def run(self):
        df = self.fetch_data()
        processed_df = self.analyze_market(df)
        return processed_df

if __name__ == "__main__":
    agent = MarketAgent()
    print(agent.run().head())
