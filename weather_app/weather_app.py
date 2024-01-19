import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather Conditions:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print("Weather data not available.")

def main():
    api_key = "52e7991c78ed41509d8ceb9918fa892d"

    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
