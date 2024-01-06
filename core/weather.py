import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()   #load env variables

def weather_data():
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    city = "Ghaziabad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        return f"The weather in {city} is {weather_description}. The temperature is {temperature} degrees Celsius with {humidity}% humidity."
    else:
        return "Sorry, I couldn't fetch the weather information at the moment."