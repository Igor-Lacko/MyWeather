"""Contains the third part of the Home tab header, the weather data and location:
    Structure:
        1.CITY, LOCATION, COUNTRY (should take up 40% of the VBOX layout, the others should get 20% each)
        2.WIND DEGREES/SPEED
        3.PRECIPITATION HEIGHT
        4.HUMIDITY PERCENTAGE
"""

from . import *
from PyQt6.QtGui import QFont


class HeaderDataText(QVBoxLayout):
    """Inherits from the VBox layout since the items are stacked vertically"""

    def __init__(self, data : Realtime, mode : ColorModes):
        """Data text constructor

        Args:
            data (Realtime): contains the weather data
            mode (ColorModes): on initialization, for setting a color
        """ 
        
        super().__init__()

        self.setAlignment(Alignments.Right)

        self.addWidget(temperature_widget := QLabel(text=
                        f"{data.temperature.actual_temperature}°C, feels like {data.temperature.feelslike}°C"),  
                        alignment=Alignments.Left,
                        stretch=1)
        
        self.addWidget(wind_widget := QLabel(text=
                        f"Wind: {data.wind.degrees}° {data.wind.direction} at {data.wind.speed} km/h"),  
                        alignment=Alignments.Left,
                        stretch=1)
        
        self.addWidget(precip_widget := QLabel(text=
                        f"Precipitation height: {data.precip_height} mm"),  
                        alignment=Alignments.Left,
                        stretch=1)
        
        self.addWidget(humidity_widget := QLabel(text=
                        f"Humidity: {data.humidity}%"),  
                        alignment=Alignments.Left,
                        stretch=1)
        
        self.widgets = [temperature_widget, wind_widget, precip_widget, humidity_widget]


        for index, widget in enumerate(self.widgets):
            self.setStretch(index, 25)

            widget.setAlignment(Alignments.Left)
            widget.setFont(QFont('Noto Sans Mono', pointSize=15))
            
        
        self.SetColor(mode)
    
        self.setContentsMargins(0,0,20,0)
    
    
    
    def SetColor(self, color_mode : ColorModes):
        """Sets the text color"""
        
        for widget in self.widgets:
            widget.setStyleSheet((StyleSheets.dark.HeaderLead if color_mode == ColorModes.DARK else StyleSheets.light.HeaderLead).value)

