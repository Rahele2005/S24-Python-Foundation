import http.client
import json

# Replace 'your_actual_api_key' with your actual OpenWeatherMap API key
API_KEY = '9c71450ed4e0b60ad2883951e4723470'
BASE_URL = 'api.openweathermap.org'
ENDPOINT = '/data/2.5/weather'

def get_weather(Stuttgart):
    conn = http.client.HTTPConnection(BASE_URL)
    conn.request("GET", f"{ENDPOINT}?q={Stuttgart}&appid={API_KEY}")
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
        
        print(f"City: {Stuttgart}")
        print(f"Temperature: {temp:.2f}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {description.capitalize()}")
    else:
        print(f"City {Stuttgart} not found. Please check the name and try again.")
    
    conn.close()

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
