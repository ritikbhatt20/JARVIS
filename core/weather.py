import json
import requests

def weather_data():
    weather_api_key = "fcd2c236893559071f53147e2c72132f"
    city = "Ghaziabad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        return f"The weather in {city} is {weather_description}. The temperature is {temperature} degrees Celsius with {humidity}% humidity."
    else:
        return "Sorry, I couldn't fetch the weather information at the moment."