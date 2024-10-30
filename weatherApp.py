import os
from dotenv import load_dotenv
import requests

#If you actually want to try it then go to https://api.openweathermap.org/data/2.5/weather.
api_key = ""

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        description = data['weather'][0]['description']
        city_name = data['name']

        print(f"Weather in {city_name}: {description.capitalize()}")
        print(f"Temperature: {temp}°C")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except Exception as e:
        print(f"Error: {e}")
city = input("Enter a city: ")
get_weather(city)