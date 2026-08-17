import os

from dotenv import load_dotenv


load_dotenv()

weather_api_key = os.getenv("OPENWEATHER_API_KEY")
geoapify_key = os.getenv("GEOAPIFY_API_KEY")

if not weather_api_key:
    raise ValueError("OPENWEATHER_API_KEY is missing from the .env file.")

if not geoapify_key:
    raise ValueError("GEOAPIFY_API_KEY is missing from the .env file.")