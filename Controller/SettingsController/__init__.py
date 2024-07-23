"""Updates the settings JSON file"""
import json
from MyWeather.View.components.Settings.SettingsItem import *
from MyWeather.View.components.Settings.SettingsWindow import SettingsTab

with open("Settings.json", "r") as config_obj:
    settings = json.load(config_obj)