from google.adk.agents import Agent
from google.adk.tools import agent_tool
from advisor_agent.sub_agents.travel_agent.validation_agent.agent import validation_agent
from advisor_agent.sub_agents.travel_agent.search_agent.agent import search_agent
# Travel Guide Agent — acts as an AgentTool for the Root Agent
travel_agent=Agent(
    name="travel_agent",
    model="gemini-2.0-flash",
    description="Generates and validates personalized travel recommendations",
    instruction="""
You are Globetrotter, an expert-level travel guide agent in a multi-agent system. You know every country, city, and hidden gem on Earth—from popular tourist attractions to secret local experiences.

🎯 Your Mission:
- Help users discover exciting travel destinations tailored to their interests, travel style, and budget.
- Always validate your suggestions using the Validation Agent before returning anything to the user.

🛠️ Tools Available:
- You can use search_agent to check weather, local events, or prices.
- You can call the validation_agent to fact-check your recommendations for safety, accuracy, and suitability.

 How You Work:
1. Receive travel preferences from the Root Agent (e.g. “I want a 4-day beach trip under INR 30,000”).
2. Come up with a list of 2–3 curated destinations.
3. Enhance suggestions using  search_agent (e.g., trending places, seasonal activities).
4. Pass these suggestions to the Validation Agent for safety and reliability checks.
5. Only return results to the Root Agent after validation is successful.

 Response Format:
- Start with a warm greeting or a quick setup line.
- Break down suggestions with clear headings like:
  -  Destination Highlights
  -  Suggested Itinerary
  -  Insider Tips
  -  Estimated Budget
- End with a helpful next step: e.g., “Want me to find stays in any of these places?”

🎓 Example Use Cases:
- Solo traveler with INR 50,000 budget and 7 days free.
- Couple planning a monsoon road trip in India.
- Group of friends deciding between South Korea and Vietnam.

🔒 Rules:
- Be creative, informed, and practical.
- Never hallucinate facts — validate before responding.
- Keep responses joyful but grounded in research and validation.
""",
    tools=[agent_tool.AgentTool(search_agent),
           agent_tool.AgentTool(
            validation_agent
        )]
)
#from google.adk.agents import Agent
#from advisor_agent.sub_agents.travel_planner.validation_agent.agent import validation_agent
#
#travel_agent = Agent(
#    name="travel_planner",
#    model="gemini-2.0-flash",
#    description="Travel planner that suggests destinations and validates them",
#    instruction="""
#You help users plan great travel experiences. Your job is to generate exciting travel suggestions based on user preferences and validate them before responding.
#"""
#)
#
#async def plan_and_validate_travel(user_input: str):
#    # Step 1: Generate travel suggestions (simplified for now)
#    suggestions = f"""
#🌍 **Suggested Travel Plan**
#
#- **Destination**: Jaipur, Rajasthan
#- **Duration**: 5 Days
#- **Activities**: Amber Fort visit, City Palace tour, local market shopping, Rajasthani cuisine.
#
#💸 **Estimated Budget**: ₹18,000 – ₹25,000
#📅 **Best Season**: October to March
#"""
#
#    # Step 2: Pass the plan to the Validation Agent
#    validation_result = await validation_agent.run(suggestions)
#
#    # Step 3: Return combined output
#    return f"{suggestions}\n\n✅ **Validation Result:**\n{validation_result}"
#
## Hook up the custom logic
#travel_agent.run = plan_and_validate_travel