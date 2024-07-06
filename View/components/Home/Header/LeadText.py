"""Contains the second header part of the Home tab, with the leading vertically divided text:
    Structure:  
                1. WEATHER CONDITION
                2. TEMPERATURE/FEELSLIKE TEMPERATURE
"""

from . import *
from PyQt6.QtGui import QFont


class HeaderLeadText(QVBoxLayout):
    """Inherits from QVBoxLayout since it's divided into 2 vertical halves"""

    def __init__(self, data : Realtime, mode : ColorModes, font : str = "Ubuntu"):
        """Lead text constructor

        Args:
            data (Realtime): contains the weather data API response to be used
            font (str): font to be used, default is ubuntu
            mode (ColorModes): color mode on initialization
        """

        super().__init__()

        self.addWidget(location_widget := QLabel(text=data.location),  
                        alignment=Alignments.Left,
                        stretch=1)
        
        self.addWidget(time_widget := QLabel(text=data.time_str),  
                        alignment=Alignments.Left,
                        stretch=1)


        self.addWidget(condition_widget := QLabel(text=data.condition),
                        alignment=Alignments.Left,
                        stretch=1)

        location_widget.setFont(QFont(font, pointSize=20))
        time_widget.setFont(QFont(font, pointSize=20))
        condition_widget.setFont(QFont(font, pointSize=30))

        self.widgets = [location_widget, time_widget, condition_widget]                             #to allow access to individual sections

        self.SetColor(mode)

        


    def SetColor(self, color_mode : ColorModes):
        """Sets the text background color"""

        for widget in self.widgets:
            widget.setStyleSheet((StyleSheets.dark.HeaderLead if color_mode == ColorModes.DARK else StyleSheets.light.HeaderLead).value)



    def UpdateData(self, data : Realtime):
        """Updates the weather data with a new set, triggered by the controller

        Args:
            data (Realtime): Realtime weather data
        """

        self.widgets[0].setText(data.location)
        self.widgets[1].setText(data.time_str)
        self.widgets[2].setText(data.condition)

        print(data.time_str)

