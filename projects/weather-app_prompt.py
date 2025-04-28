import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def display_weather(city, api_key):
    data = get_weather(city, api_key)

    if data["cod"] == "404":
        print("City not found.")
    else:
        main_data = data["main"]
        temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
        print(f"The temperature in {city} is {temperature:.2f}°C.")

api_key = "your_api_key"
city = input("Enter city name: ")
display_weather(city, api_key)
