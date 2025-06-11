import requests
from core.speaker import speak

def handle(query: str):
    try:
        ip = requests.get('https://api.ipify.org').text
        geo_data = requests.get(f'https://get.geojs.io/v1/ip/geo/{ip}.json').json()
        city = geo_data.get("city", "Unknown city")
        country = geo_data.get("country", "Unknown country")
        speak(f"You are in {city}, {country}.")
    except:
        speak("I couldn't determine your location.")
