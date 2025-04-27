# Get temperature from user and display a message accordingly
temperature = float(input("Enter the temperature in °C: "))

if temperature > 35:
    print("It's really hot outside!")
elif temperature > 20:
    print("Nice and warm.")
else:
    print("It's a bit chilly.")
