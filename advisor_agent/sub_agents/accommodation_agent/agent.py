from google.adk.agents import Agent
from advisor_agent.sub_agents.accommodation_agent.api.accommodation_api import search_tool


accommodation_agent = Agent(
    name="AccommodationAgent",
    model="gemini-2.0-flash",
    description="Books accommodations based on destination and user preferences.",
    instruction="""
You are the Accommodation Agent in a multi-agent travel assistant system.

🎯 Your Role:
- Help users find and book accommodations (hotels, hostels, homestays) after they’ve chosen a travel destination.
- Suggest 2-3 options in different budget ranges (e.g., budget, mid-range, luxury).
- Include price range, amenities, distance from center, and pros/cons.

🛠️ How You Work:
- Take input from the Root Agent (destination, travel dates, preferences).
- Use the 3rd-party Accommodation API (SerpAPI) to search for real listings.
- Return a clear list of suggestions with key info.

📦 Response Format:
- 🏨 Hotel Name
- 💸 Price Range
- 🌐 Booking Link
- 📍 Location Overview
- 🛏️ Amenities
- 📣 Why it's a good fit

🎯 Example Inputs:
- “Find me a mid-range hotel in Goa from 12th to 15th July.”
- “Suggest the best-rated homestays in Rishikesh for 2 people.”

⚠️ Do not make up results — always fetch using the search API and return actual listings.

You can call:
    result = search_accommodation(destination="Goa", check_in="2025-07-12", check_out="2025-07-15")
""",
   tools=[search_tool]
)
#from google.adk.agents import Agent
#from advisor_agent.sub_agents.accommodation_agent.api.accommodation_api import search_accommodation
#
#accommodation_agent = Agent(
#    name="AccommodationAgent",
#    model="gemini-2.0-flash",
#    description="Helps users find and book hotels",
#    instruction="""
#You help users find hotels or rentals based on their destination and dates.
#You use external APIs to fetch real-time data and respond in a clean, organized format.
#"""
#)
#
#async def handle_accommodation_query(user_input: str):
#    # ✳️ For now, hardcoded (you can extract these with regex or LLM later)
#    destination = "Jaipur"
#    check_in = "2025-07-01"
#    check_out = "2025-07-05"
#
#    results = search_accommodation(destination, check_in, check_out)
#
#    if not results:
#        return "⚠️ Sorry, I couldn’t find any accommodations for your query."
#
#    response = f"🏨 **Top stays in {destination}**\n\n"
#    for hotel in results:
#        response += f"**{hotel['name']}**\n"
#        response += f"- 📍 Location: {hotel['location']}\n"
#        response += f"- 🔗 [Link]({hotel['link']})\n"
#        response += f"- 📝 Notes: {hotel['notes']}\n\n"
#
#    return response
#
#accommodation_agent.run = handle_accommodation_query