import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            "temperature": main['temp'],
            "pressure": main['pressure'],
            "humidity": main['humidity'],
            "description": weather['description']
        }
    else:
        return None

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "YOUR_API_KEY"
    weather_data = get_weather(city_name, api_key)
    
    if weather_data:
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Pressure: {weather_data['pressure']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Description: {weather_data['description']}")
    else:
        print("City not found.")