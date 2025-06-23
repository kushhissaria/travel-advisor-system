from google.adk.agents import Agent
from google.adk.tools import google_search

# Validation Agent — used as a tool by TravelAgent
validation_agent=Agent(
    name="validation_agent",
    model="gemini-2.0-flash",
    description="Travel safety and accuracy validator for travel suggestions",
    instruction="""
You are a Validation Agent in a multi-agent travel assistant system. Your job is to verify the accuracy, safety, and suitability of travel recommendations provided by the Travel Agent.

🔍 Responsibilities:
1. Use Google Search to fact-check all travel suggestions.
2. Look for current travel advisories, recent news, or safety concerns.
3. Flag any misleading, outdated, or high-risk suggestions.
4. Consider factors like political unrest, climate events, or suitability for solo, female, LGBTQ+ travelers, etc.

⚠️ You do NOT recommend destinations. You only validate or raise concerns.

📦 Output Format:
- ✅ Validation Summary
- ⚠️ Potential Issues (if any)
- 🔍 Sources Checked
- 📣 Follow-Up Questions (if needed)

Tone: Cautious, professional, user-centric.
Make sure what’s passed to the user is **safe, up to date, and accurate**.
""",
    tools=[google_search]
)
#from google.adk.agents import Agent
#from google.adk.tools import google_search  # Optional for real validation
#
#validation_agent = Agent(
#    name="ValidationAgent",
#    model="gemini-2.0-pro",
#    description="Validates the safety and accuracy of travel suggestions",
#    instruction="""
#Your job is to validate travel suggestions.
#Check for safety concerns, outdated information, or impractical recommendations.
#You must NOT create new travel plans — only validate what’s given.
#"""
#)
#
#async def validate_travel_plan(input_text: str):
#    # Optional: you can use google_search here for real-time validation
#
#    # For now, always return a successful validation
#    return f"""
#✅ Validation Summary:
#- No major safety concerns.
#- Jaipur is considered safe for most travelers.
#- Weather in winter is pleasant.
#
#🔍 Sources Checked:
#- gov.in travel advisories
#- Recent news articles
#- Tourism blogs
#"""
#
#validation_agent.run = validate_travel_plan
