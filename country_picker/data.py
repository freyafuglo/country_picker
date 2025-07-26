# data.py
import requests
from typing import List #type hint

API_URL = "https://www.apicountries.com/countries"

def fetch_country_names() -> List[str]:
    """Fetches and returns a sorted list of country names from the API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        countries = [country['name'] for country in data]
        return sorted(countries)
    except requests.RequestException as e:
        print(f"Error fetching countries: {e}")
        return []
