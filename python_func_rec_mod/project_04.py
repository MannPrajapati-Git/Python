# project : fake weather generator

import random

def fake_weather_multi():
    weather_options = ["sunny", "cloudy", "rainy", "stormy", "foggy", "windy", "humid"]
    cities = ["Delhi", "Ahmedabad", "Bangalore", "Chennai", "Kolkata", "Jaipur"]

    print(" Today’s Random Weather Forecast:\n")
    for city in cities:
        forecast = random.choice(weather_options)
        print(f" {city}: {forecast.capitalize()}")

fake_weather_multi()
