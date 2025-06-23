from google.adk.agents import Agent
from google.adk.tools import google_search

search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",  
    description="Handles real-time web searches",
    instruction="""
You are a web search assistant. Given a user query, use Google Search to retrieve relevant and up-to-date information. Your responses should be summarized and readable.
""",
    tools=[google_search]
)