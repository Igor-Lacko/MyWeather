"""Contains the third part of the Home tab header, the weather data and location:
    Structure:
        1.CITY, LOCATION, COUNTRY (should take up 40% of the VBOX layout, the others should get 20% each)
        2.WIND DEGREES/SPEED
        3.PRECIPITATION HEIGHT
        4.HUMIDITY PERCENTAGE
"""

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPalette
from MyWeather.Model.obj import Realtime
from ....utils.enumerations import Alignments, Colors


class HeaderDataText(QVBoxLayout):
    """Inherits from the VBox layout since the items are stacked vertically"""

    def __init__(self, data : Realtime):
        """Data text constructor

        Args:
            location (str, optional): Default location. Defaults to "Presov, Slovakia".
            temperature (str, optional): temperatire at location. Defaults to "20.1°C, feels like 20.1".
            wind (str, optional): wind speed and direction. Defaults to "Wind: 40°Northeast at 16.9km/h".
            precip (str, optional): precipitation height. Defaults to "Precipitation height: 0.0mm".
            humidity (str, optional): humidity percentage. Defaults to "Humidity: 73%".
        """ 
        
        super().__init__()

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
            widget.setStyleSheet("""QLabel{margin-left: 50px;}""")

    
    def SetColor(self, color : str):
        """Sets the text color"""
        
        for widget in self.widgets:
            widget.setStyleSheet(color)

