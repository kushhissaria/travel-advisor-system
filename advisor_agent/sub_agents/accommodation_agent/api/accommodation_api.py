#import os
#from dotenv import load_dotenv
##from serpapi import GoogleSearch
#from serpapi import GoogleSearch
#
#load_dotenv()
#API_KEY = os.getenv("SERPAPI_KEY")
#
#def search_accommodation(destination, check_in, check_out, budget=None):
#    query = f"{destination} hotels from {check_in} to {check_out}"
#    params = {
#        "q": query,
#        "location": destination,
#        "hl": "en",
#        "gl": "in",
#        "api_key": API_KEY
#    }
#
#    search = GoogleSearch(params)
#    results = search.get_dict()
#
#    hotels = []
#    for result in results.get("organic_results", [])[:3]:
#        hotels.append({
#            "name": result.get("title"),
#            "price": "N/A",
#            "link": result.get("link"),
#            "location": destination,
#            "amenities": ["Wi-Fi", "AC", "Breakfast"],  # Placeholder
#            "notes": result.get("snippet", "")
#        })
#
#    return hotels
#import os
#from dotenv import load_dotenv
#from serpapi import GoogleSearch
#from google.adk.tools import tool
#
#load_dotenv()
#API_KEY = os.getenv("SERPAPI_KEY")
#
#
#def _search_accommodation(destination, check_in, check_out, budget=None):
#    query = f"{destination} hotels from {check_in} to {check_out}"
#    params = {
#        "q": query,
#        "location": destination,
#        "hl": "en",
#        "gl": "in",
#        "api_key": API_KEY
#    }
#
#    search = GoogleSearch(params)
#    results = search.get_dict()
#
#    hotels = []
#    for result in results.get("organic_results", [])[:3]:
#        hotels.append({
#            "name": result.get("title"),
#            "price": "N/A",
#            "link": result.get("link"),
#            "location": destination,
#            "amenities": ["Wi-Fi", "AC", "Breakfast"],  # Placeholder
#            "notes": result.get("snippet", "")
#        })
#
#    return hotels
#
#
#@tool(name="search_accommodation", description="Find hotels based on destination and date")
#async def search_tool(input: dict) -> str:
#    """
#    Expects:
#    {
#        "destination": "Goa",
#        "check_in": "2025-07-01",
#        "check_out": "2025-07-05"
#    }
#    """
#    try:
#        destination = input["destination"]
#        check_in = input["check_in"]
#        check_out = input["check_out"]
#
#        hotels = _search_accommodation(destination, check_in, check_out)
#
#        if not hotels:
#            return "⚠️ No hotels found for this query."
#
#        response = f"🏨 **Top Hotel Suggestions in {destination}**\n\n"
#        for hotel in hotels:
#            response += f"**{hotel['name']}**\n"
#            response += f"- 📍 Location: {hotel['location']}\n"
#            response += f"- 🔗 [Link]({hotel['link']})\n"
#            response += f"- 📝 Notes: {hotel['notes']}\n\n"
#
#        return response.strip()
#    except Exception as e:
#        return f"❌ Tool Error: {str(e)}"
from google.adk.tools.base_tool import Tool

async def search_tool(input: dict) -> str:
    destination = input["destination"]
    check_in = input["check_in"]
    check_out = input["check_out"]

    results = _search_accommodation(destination, check_in, check_out)

    return f"Top result: {results[0]['name']}" if results else "No results"

search_tool = Tool(
    name="search_accommodation",
    description="Search for hotels using destination and dates",
    input_type="dict",  # Tells ADK to pass in a dictionary
    function=search_tool
)
