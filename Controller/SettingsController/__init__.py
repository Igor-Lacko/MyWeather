"""Updates the settings JSON file"""
import json
from MyWeather.View.components.Settings.SettingsItem import *

with open("Config/settings.json", "r") as config_obj:
    settings = json.load(config_obj)