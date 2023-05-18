import requests
import json
from pathlib import Path
import config

def get_weather_report(city):
    units = "metric"
    API_key = "38cc1e849ce5be7f2ab4370be368d8ce"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}appid={config.API_key}&q={city}&units={units}"

    response = requests.get(url).json()

    # Creating a JSON file with weather data
    data = json.dumps(response)
    Path("response.json").write_text(data)

    # Reading the JSON file
    final_data = Path("response.json").read_text()
    weather_info = json.loads(final_data)

    # Extracting required parameters from the JSON file
    weather_description = weather_info["weather"][0]["description"]
    temperature = int(weather_info["main"]["temp"])
    feels_like = weather_info["main"]["feels_like"]

    weather_data = {
        "current_temperature": f"Current Temperature: {temperature}°C",
        "feels_like_temperature": f"Feels like: {feels_like}°C",
        "weather_description": f"Description of weather: {weather_description}"
    }

    return weather_data
