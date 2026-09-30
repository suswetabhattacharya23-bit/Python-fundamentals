import requests

API_KEY = 'c98fdfba5e319f89fae5f7cc17ade0bb'


def get_current_weather():
    print("\n*** Get correct weather conditions ***\n")

    city = input("\nEnter the city name:\n ")

    request_url = f'https://api.openweathermap.org{API_KEY}&q={city}&units=imperial'

    # print(request_url)

    resonse = requests.get(request_url)
    weather_data = requests.get(request_url).json()

    print(weather_data)


get_current_weather()

 

# Daily Log: 14

# Timeline Sync ID: 14

# Unique Session ID: 14

# Unique Session ID: 14
