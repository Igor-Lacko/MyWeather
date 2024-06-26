"""Contains the second header part of the Home tab, with the leading vertically divided text:
    Structure:  
                1. WEATHER CONDITION
                2. TEMPERATURE/FEELSLIKE TEMPERATURE
"""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPalette
from MyWeather.Model.obj import Realtime
from ....utils.enumerations import Alignments, Colors

class HeaderLeadText(QVBoxLayout):
    """Inherits from QVBoxLayout since it's divided into 2 vertical halves"""

    def __init__(self, data : Realtime, font : str = "Ubuntu"):
        """Lead text constructor

        Args:
            data (Realtime): contains the weather data API response to be used
        """

        super().__init__()

        self.addWidget(location_widget := QLabel(text=data.location),  
                        alignment=Alignments.Left,
                        stretch=1)
        
        self.addWidget(time_widget := QLabel(text=str(data.date)),  
                        alignment=Alignments.Left,
                        stretch=1)


        self.addWidget(condition_widget := QLabel(text=data.condition),
                        alignment=Alignments.Left,
                        stretch=1)

        location_widget.setFont(QFont(font, pointSize=20))
        time_widget.setFont(QFont(font, pointSize=20))
        condition_widget.setFont(QFont(font, pointSize=30))

        self.widgets = [location_widget, time_widget, condition_widget]                             #to allow access to individual sections

        


    def SetColor(self, color : str):
        """Sets the text background color"""

        for widget in self.widgets:
            widget.setStyleSheet(color)
