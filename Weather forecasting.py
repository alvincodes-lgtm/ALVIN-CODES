import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city from the OpenWeatherMap API."""
    if not API_KEY:
        print("Error: API_KEY not found. Please set it in your .env file.")
        return None

    # Define query parameters required by OpenWeatherMap API
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Fetch temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Check HTTP Status Codes
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            print("Invalid request. Please check the city name.")
        elif response.status_code == 401:
            print("Authentication failed. Please check your API key.")
        elif response.status_code == 404:
            print("City not found. Please check the city name.")
        else:
            print(f"An error occurred. HTTP Status Code: {response.status_code}")

    except requests.RequestException:
        print("Unable to connect to the weather service.")

    return None


def main():
    print("=============================")
    print("       WEATHER APP           ")
    print("=============================")

    city = input("Enter a city: ").strip()

    # Handle empty input
    if not city:
        print("City name cannot be empty. Please try again.")
        return

    weather = get_weather(city)

    # Display weather report if data was retrieved successfully
    if weather:
        city_name = weather.get("name")
        country = weather.get("sys", {}).get("country", "")
        temp = weather.get("main", {}).get("temp")
        humidity = weather.get("main", {}).get("humidity")
        description = weather.get("weather", [{}])[0].get("description", "").capitalize()

        print("\n=============================")
        print("       WEATHER REPORT        ")
        print("=============================")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")


if __name__ == "__main__":
    main()




    