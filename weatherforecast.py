import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}  # You can change the units as needed

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to retrieve weather data.")

def weather_forecast():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
    location = input("Enter city name or zip code: ")

    weather_data = get_weather(api_key, location)

    display_weather(weather_data)

if __name__ == "__main__":
    weather_forecast()
