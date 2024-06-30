"""Includes the main graph widget"""
from PyQt6.QtWidgets import *
from MyWeather.View.utils.enumerations import *

class WeatherGraph(QVBoxLayout):
    """Includes the weather graph"""
    def __init__(self):
        super().__init__()
        
        self.addWidget(fr := QWidget())

        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)