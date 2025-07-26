# data.py
import requests

API_URL = "https://www.apicountries.com/countries"

def fetch_country_names() -> list[str]:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return sorted([entry["name"] for entry in data])
