"""Controller for the Weather section of the app. Handles updates based on the user's choice, subsequent choices, restarts, and communication with other elements.
Should by far be the largest controller module."""
from PyQt6.QtWidgets import *
from MyWeather.View.components.Weather.WeatherWindow import WeatherTab
from View.components.Weather.OptionsMenu import OptionMenu