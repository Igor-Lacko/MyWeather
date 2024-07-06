"""Contains the settings tab"""
from MyWeather.Init import FONTS, DEFAULT_MODE
import json

with open("Config/settings.json", "r") as config_obj:
    settings = json.load(config_obj)