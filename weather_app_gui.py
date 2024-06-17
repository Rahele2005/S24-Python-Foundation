import http.client
import json
import tkinter as tk
from tkinter import messagebox

# Replace 'your_actual_api_key' with your actual OpenWeatherMap API key
API_KEY = '9c71450ed4e0b60ad2883951e4723470'
BASE_URL = 'api.openweathermap.org'
ENDPOINT = '/data/2.5/weather'

def get_weather(city_name):
    conn = http.client.HTTPConnection(BASE_URL)
    conn.request("GET", f"{ENDPOINT}?q={city_name}&appid={API_KEY}")
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read().decode('utf-8')
        data = json.loads(data)
        main = data['main']
        weather = data['weather'][0]
        
        temp = main['temp'] - 273.15  # Convert temperature from Kelvin to Celsius
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        result = (
            f"City: {city_name}\n"
            f"Temperature: {temp:.2f}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Weather Description: {description.capitalize()}"
        )
        return result
    else:
        return f"City {city_name} not found. Please check the name and try again."

def show_weather():
    city_name = city_entry.get()
    weather_info = get_weather(city_name)
    messagebox.showinfo("Weather Information", weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the widgets
tk.Label(root, text="Enter city name:").pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=20)

# Run the application
root.mainloop()
