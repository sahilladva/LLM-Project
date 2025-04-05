from agents.farm_data_agent import FarmDataAgent
from agents.market_agent import MarketAgent
from agents.recommendation_agent import RecommendationAgent
from agents.llm_advisor import LLMAdvisorAgent

def main():
    # Run the Farm Data Agent
    farm_agent = FarmDataAgent(db_path="farming.db")
    farm_data = farm_agent.run()
    print("✅ Farm Data Processed:")
    print(farm_data.head())

    # Run the Market Agent
    market_agent = MarketAgent(db_path="farming.db")
    market_data = market_agent.run()
    print("\n✅ Market Data Processed:")
    print(market_data.head())

    # Generate a preliminary recommendation
    rec_agent = RecommendationAgent(farm_data, market_data)
    recommendation = rec_agent.generate_recommendation()
    print("\n🧠 Preliminary Recommendation:")
    print(recommendation)

    # Use LLM Advisor (LLaMA model via Ollama)
    llm_agent = LLMAdvisorAgent(model="tinyllama")

    # Use the first row of farm_data for detailed context
    first_farm_data = farm_data.iloc[0].to_dict()
    detailed_advice = llm_agent.generate_advice(recommendation, first_farm_data)
    print("\n📋 Detailed Advice from LLM:")
    print(detailed_advice)

    # 🌾 Ask multiple farming questions
    while True:
        user_question = input("\n💬 Ask your farming question (or type 'exit' to quit): ")
        if user_question.strip().lower() == "exit":
            print("👋 Exiting the LLM advisor. Have a great day farming! 🌱")
            break
        custom_response = llm_agent.ask_custom_question(user_question)
        print("\n🤖 LLM's Answer:")
        print(custom_response)

if __name__ == "__main__":
    main()
