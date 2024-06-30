"""Contain scripts that run on the app start-up\n
    -For example, the base module initialies InitWeatherData, which is the WeatherData displayed on Home Screen
"""
from MyWeather.Model.request import CompleteData

InitWeatherData = CompleteData("Presov")        #presov default frfr