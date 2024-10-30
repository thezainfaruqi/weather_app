Weather App 🌦️

Overview:
A simple Python-based command-line Weather App that fetches real-time weather data for any city using the OpenWeatherMap API. It displays the temperature, weather conditions, and a brief description of the current weather. This project is a beginner-friendly way to explore APIs, HTTP requests, and environment variable management in Python.

Features:
🌍 Search for the current weather by city name.
🌡️ Displays temperature in Celsius.
Shows weather conditions (e.g., clear sky, rain).
Secure API key management with .env.

Technologies Used:
Python 🐍
Requests library for making HTTP requests.
OpenWeatherMap API for weather data.
python-dotenv for managing environment variables.

Issue Encountered: API Key Error 🛑
While working on this project, I ran into an issue where the OpenWeatherMap API kept returning a 401 Unauthorized error. This was due to the API key not loading properly from the .env file.
