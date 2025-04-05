import sqlite3
import pandas as pd
import os

def initialize_database():
    # Connect or create SQLite database
    conn = sqlite3.connect("farming.db")

    # Ensure data folder exists
    data_path = os.path.join(os.getcwd(), "data")

    # Load FarmData.csv into FarmData table
    farm_data_csv = os.path.join(data_path, "FarmData.csv")
    if os.path.exists(farm_data_csv):
        farm_df = pd.read_csv(farm_data_csv)
        farm_df.to_sql("FarmData", conn, if_exists="replace", index=False)
        print("FarmData table created.")
    else:
        print("FarmData.csv not found!")

    # Load MarketData.csv into MarketData table
    market_data_csv = os.path.join(data_path, "MarketData.csv")
    if os.path.exists(market_data_csv):
        market_df = pd.read_csv(market_data_csv)
        market_df.to_sql("MarketData", conn, if_exists="replace", index=False)
        print("MarketData table created.")
    else:
        print("MarketData.csv not found!")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
