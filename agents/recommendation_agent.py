# agents/recommendation_agent.py
import pandas as pd
def recommend_crops(farm_data, market_data):
    # simple dummy logic for now
    return "Wheat"


class RecommendationAgent:
    def __init__(self, farm_data, market_data):
        self.farm_data = farm_data
        self.market_data = market_data

    def generate_recommendation(self):
        # For simplicity, use the first row from farm data
        farm_row = self.farm_data.iloc[0]
        crop_type = farm_row['Crop_Type']
        # Find matching market data (case-insensitive)
        market_info = self.market_data[self.market_data['Product'].str.lower() == crop_type.lower()]
        if not market_info.empty:
            market_row = market_info.iloc[0]
            recommendation = {
                "Crop": crop_type,
                "Sustainability_Score": farm_row['Sustainability_Score'],
                "Market_Score": market_row['Market_Score'],
                "Market_Price_per_ton": market_row['Market_Price_per_ton'],
                "Decision": "Recommended" if (farm_row['Sustainability_Score'] > 5 and market_row['Market_Score'] > 50) else "Not Recommended"
            }
        else:
            recommendation = {
                "Crop": crop_type,
                "Sustainability_Score": farm_row['Sustainability_Score'],
                "Market_Score": None,
                "Market_Price_per_ton": None,
                "Decision": "Insufficient market data"
            }
        return recommendation

if __name__ == "__main__":
    # Dummy data test
    import pandas as pd
    farm_data = pd.DataFrame([{
        'Farm_ID': 'F001',
        'Crop_Type': 'Wheat',
        'Soil_pH': 7.0,
        'Soil_Moisture': 30,
        'Temperature_C': 26,
        'Rainfall_mm': 100,
        'Sustainability_Score': 7.5
    }])
    market_data = pd.DataFrame([{
        'Market_ID': 'M001',
        'Product': 'Wheat',
        'Market_Price_per_ton': 210,
        'Market_Score': 70
    }])
    agent = RecommendationAgent(farm_data, market_data)
    print(agent.generate_recommendation())
