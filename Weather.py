"""Command-line Weather App using the OpenWeatherMap API."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Request current weather for a city.

    Returns a dictionary with the weather details on success,
    or None if something went wrong (an error message is printed).
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.RequestException:
        print("Unable to connect to the weather service.")
        return None

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
        }
    elif response.status_code == 400:
        print("Invalid request. Please check the city name.")
    elif response.status_code == 401:
        print("Authentication failed. Please check your API key.")
    elif response.status_code == 404:
        print("City not found. Please check the city name.")
    else:
        print(f"Error: received status code {response.status_code}")

    return None


def display_weather(weather):
    """Print the weather report."""
    print()
    print("=============================")
    print("       WEATHER REPORT")
    print("=============================")
    print(f"City:        {weather['city']}, {weather['country']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Weather:     {weather['weather']}")
    print(f"Humidity:    {weather['humidity']}%")
    print("=============================")


def main():
    print("=============================")
    print("       WEATHER APP")
    print("=============================")
    print()

    if not API_KEY:
        print("API key not found. Add API_KEY=your_key to your .env file.")
        return

    city = input("Enter a city: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    weather = get_weather(city)

    if weather:
        display_weather(weather)


if __name__ == "__main__":
    main()