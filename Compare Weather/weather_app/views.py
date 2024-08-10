from django.shortcuts import render
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz

def index(request):
    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1 = fetch_weather_and_forecast(city1) if city2 else None
        weather_data2 = fetch_weather_and_forecast(city2) if city2 else None

        context = {
            'weather_data1': weather_data1,
            'weather_data2': weather_data2,
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')


def fetch_weather_and_forecast(city):
    geolocator = Nominatim(user_agent="geopyExercises")
    location = geolocator.geocode(city)
    lat = location.latitude
    long = location.longitude

    api_key = '4b28f169f63a5d76d0ee43f10c933fe4'
    api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}'

    jsondata = requests.get(api).json()

    weather_data = {
        "name":str(city).upper(),
        "condition": jsondata["weather"][0]["main"],
        "description": jsondata["weather"][0]["description"],
        "temperature": int(jsondata["main"]['temp'] - 273.15),
        "pressure": jsondata["main"]["pressure"],
        "humidity": jsondata["main"]["humidity"],
        "wind_speed": jsondata["wind"]["speed"],
    }

    with open("temp.txt", "w") as f:
        f.write(str(jsondata))  

    return weather_data
