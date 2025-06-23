from google.adk.agents import Agent  
from google.adk.tools import google_search,agent_tool  
from advisor_agent.sub_agents.travel_agent.agent import travel_agent
from advisor_agent.sub_agents.accommodation_agent.agent import accommodation_agent
root_agent = Agent(
    name="advisor_agent",
    model="gemini-2.0-flash",
    description="Root agent that orchestrates travel planning, validation, and booking",
    instruction="""
You are the Root Agent in a multi-agent travel advisor system.

Your responsibilities:
1. Greet the user and understand their travel preferences (destination, dates, interests, budget).
2. Use the Travel Agent (agent tool) to generate curated travel suggestions.
3. **Ensure that the Travel Agent uses the Validation Agent to check all recommendations before returning results.**
4. Only after successful validation, return results to the user.
5. Use the Accommodation Agent (sub-agent) to help users find and book places to stay.

System structure:
- **Travel Agent** (Agent Tool): Generates high-quality travel plans and uses the Validation Agent internally.
- **Validation Agent**: Ensures travel plans are safe, current, and appropriate.
- **Accommodation Agent** (Sub-Agent): Handles finding and booking stays.

Workflow:
1. Ask user about travel goals.
2. Trigger Travel Agent to plan suggestions.
3. The Travel Agent **must validate** all recommendations via the Validation Agent before sending results.
4. Once validated, present the travel plan to the user.
5. If user wants to proceed, trigger the Accommodation Agent.
6. Maintain smooth, natural flow from start to booking.

Tone:
- Friendly, intelligent, and organized.
- Be the brain coordinating the experience — the user should feel guided and understood at every step.
""",
    sub_agents=[accommodation_agent],
    tools=[
        agent_tool.AgentTool(
            travel_agent
        )
    ]
)
#from google.adk.agents import Agent
#from advisor_agent.sub_agents.travel_planner.agent import travel_agent
#from advisor_agent.sub_agents.accommodation_agent.agent import accommodation_agent
#
## This function decides where to send the input
#async def route_user_query(user_input: str):
#    user_input = user_input.lower()
#    if "hotel" in user_input or "stay" in user_input or "accommodation" in user_input:
#        return await accommodation_agent.run(user_input)
#    else:
#        return await travel_agent.run(user_input)
#
## Create the root agent
#root_agent = Agent(
#    name="advisor_agent",
#    model="gemini-2.0-flash",
#    description="Root agent coordinating travel and accommodation planning.",
#    instruction="""
#You help users plan trips and book stays. If the query is about travel, delegate to the Travel Agent.
#If it’s about places to stay or hotels, delegate to the Accommodation Agent.
#Always return meaningful responses to the user.
#"""
#)
#
## Override the default behavior
#root_agent.run = route_user_query
