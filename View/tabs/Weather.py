from PyQt6.QtWidgets import *
from ..components.test import ColoredBar
from ..utils import enumerations


class WeatherTab(QVBoxLayout):
    """contains the weather data tab for the application

    Args:
        QVBoxLayout (QVBoxLayout): Has items aligned vertically
    """

    def __init__(self):
        """home tab constructor"""
        super().__init__()

        self.addWidget(ColoredBar(color=enumerations.Colors.Indigo))
        self.setContentsMargins(0,0,0,0)