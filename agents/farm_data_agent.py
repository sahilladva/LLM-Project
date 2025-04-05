# agents/farm_data_agent.py
import sqlite3
import pandas as pd

import pandas as pd

def get_farm_data():
    df = pd.read_csv("data/FarmData.csv")
    return df


class FarmDataAgent:
    def __init__(self, db_path="farming.db"):
        self.db_path = db_path

    def fetch_data(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM FarmData", conn)
        conn.close()
        return df

    def compute_sustainability(self, df):
        # Example: Sustainability_Score = Crop_Yield_ton * 0.5 - Fertilizer_Usage_kg * 0.1 - Pesticide_Usage_kg * 0.2
        df['Sustainability_Score'] = df['Crop_Yield_ton'] * 0.5 - df['Fertilizer_Usage_kg'] * 0.1 - df['Pesticide_Usage_kg'] * 0.2
        return df[['Farm_ID', 'Crop_Type', 'Soil_pH', 'Soil_Moisture', 'Temperature_C', 'Rainfall_mm', 'Sustainability_Score']]

    def run(self):
        df = self.fetch_data()
        processed_df = self.compute_sustainability(df)
        return processed_df

if __name__ == "__main__":
    agent = FarmDataAgent()
    print(agent.run().head())
