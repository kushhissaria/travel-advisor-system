import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
API_KEY = os.getenv("SERPAPI_KEY")

def search_accommodation(destination, check_in, check_out, budget=None):
    query = f"{destination} hotels from {check_in} to {check_out}"
    params = {
        "q": query,
        "location": destination,
        "hl": "en",
        "gl": "in",
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    hotels = []
    for result in results.get("organic_results", [])[:3]:
        hotels.append({
            "name": result.get("title"),
            "price": "N/A",
            "link": result.get("link"),
            "location": destination,
            "amenities": ["Wi-Fi", "AC", "Breakfast"],  # Placeholder
            "notes": result.get("snippet", "")
        })

    return hotels
