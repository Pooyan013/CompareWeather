Weather Comparison App
Overview
The Weather Comparison App is a Django-based web application that allows users to compare the weather conditions of two cities. The application uses the OpenWeatherMap API to fetch real-time weather data and displays the results in a user-friendly format.

This app demonstrates the integration of external APIs with Django, and it provides a simple yet effective interface for users to compare weather conditions.

Features
City Weather Comparison: Users can input the names of two cities and compare their weather conditions.
Real-time Weather Data: The app fetches real-time weather data including temperature, pressure, humidity, and wind speed.
Weather Details: For each city, the app displays the current weather condition and description.
Technologies Used
Django: A high-level Python web framework used for the backend.
Geopy: A Python library for geocoding addresses, used to get latitude and longitude for cities.
Requests: A simple HTTP library for Python, used to make API requests to OpenWeatherMap.
OpenWeatherMap API: A service that provides weather data based on latitude and longitude.
Setup
Prerequisites
Python 3.x
Django
Geopy
Requests
An OpenWeatherMap API key (you can get one for free at OpenWeatherMap)
