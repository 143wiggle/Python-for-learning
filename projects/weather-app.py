import requests

api_key = "your_api_key"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()

if data["cod"] == "404":
    print("City not found.")
else:
    main_data = data["main"]
    temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
    print(f"The temperature in {city} is {temperature:.2f}°C.")
