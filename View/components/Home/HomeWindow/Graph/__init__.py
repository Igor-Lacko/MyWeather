"""Contains the main frame for showing the weather graphs on the home screen"""
from PyQt6.QtWidgets import *
from MyWeather.View.utils.enumerations import *
from MyWeather.Init.MainWindowInits import GraphInit
from .GraphBody import WeatherGraph




class GraphFrame(QFrame):
    """Main class for the frame"""

    def __init__(self, sheet):
        super().__init__()


        self.setObjectName("GraphFrame")
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        
        
        (layout := QVBoxLayout()).addLayout(GraphInit.GetGraphHeader())
        layout.addLayout(WeatherGraph())
        
        layout.setStretch(0,10)
        layout.setStretch(1,90)

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.setStyleSheet(sheet.value)



