"""Several functions that remove some boilerplate code around the Weather Tab controller"""
from . import *
from MyWeather.Init.WeatherInits.ItemLayout import api_options
from MyWeather.Init.WeatherInits.ItemsInit import ParseItems

def GetSelectionLayout(tab : WeatherTab):
    """Returns a initialized layout with the selection buttons"""
    layout = QHBoxLayout()
    ParseItems(api_options['items'], layout, tab)
    tab.selection_layout = layout
    return layout