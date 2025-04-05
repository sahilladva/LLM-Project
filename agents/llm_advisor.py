import subprocess

class LLMAdvisorAgent:
    def __init__(self, model="llama2"):
        self.model = model

    def query_ollama(self, prompt):
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt.encode('utf-8'),
                capture_output=True,
                timeout=60
            )
            output = result.stdout.decode('utf-8')
            return output.strip()
        except Exception as e:
            return f"Error: {e}"

    def generate_advice(self, recommendation, farm_data):
        prompt = f"""
You are an expert agricultural advisor.
Based on the following data:
- Crop: {recommendation['Crop']}
- Sustainability Score: {recommendation['Sustainability_Score']}
- Market Score: {recommendation['Market_Score']}
- Market Price per ton: {recommendation['Market_Price_per_ton']}
And the farm conditions:
- Soil pH: {farm_data['Soil_pH']}
- Soil Moisture: {farm_data['Soil_Moisture']}
- Temperature: {farm_data['Temperature_C']}°C
- Rainfall: {farm_data['Rainfall_mm']}mm

Please provide a detailed recommendation on why this crop is suitable for sustainable farming and suggest improvements.
"""
        advice = self.query_ollama(prompt)
        return advice

    def ask_custom_question(self, question):
        prompt = f"You are an agricultural expert. Please answer: {question}"
        response = self.query_ollama(prompt)
        return response


if __name__ == "__main__":
    # Dummy test for the LLM Advisor with LLaMA 2
    recommendation = {
        "Crop": "Wheat",
        "Sustainability_Score": 7.5,
        "Market_Score": 70,
        "Market_Price_per_ton": 210,
        "Decision": "Recommended"
    }
    farm_data = {'Soil_pH': 7.0, 'Soil_Moisture': 30, 'Temperature_C': 26, 'Rainfall_mm': 100}
    agent = LLMAdvisorAgent(model="tinyllama")
    print(agent.generate_advice(recommendation, farm_data))

    # Test custom question
    question = "Which crop is good for acidic soil?"
    print("Answer to custom question:")
    print(agent.ask_custom_question(question))
