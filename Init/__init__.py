"""Contain scripts that run on the app start-up\n
    -The base module also initializes settings for the app
"""
from MyWeather.Model.request import CompleteData
from MyWeather.View.utils.enumerations import ColorModes
import json
from dataclasses import dataclass
import geocoder


#helper class for dot access to fonts later on
@dataclass
class Fonts:
    sidebar : str
    header_lead : str
    header_data : str
    graph_header : str




with open("Config/settings.json", "r") as file:
    settings = json.load(file)




#----------DEFAULT SETTINGS----------#
DEFAULT_MODE = ColorModes(settings["theme"])
GRAPH_MODE = settings["graph"]
LOCATION = settings["location"]
CITY = LOCATION if LOCATION != "current" else\
f"{(user_location := geocoder.ip('me').latlng)[0]},{user_location[1]}"
FONTS = Fonts(**settings["fonts"])





#----------INITIAL WEATHER DATA----------#
InitWeatherData = CompleteData(CITY)
