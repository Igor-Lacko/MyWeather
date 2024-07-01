"""Contains the main frame for showing the weather graphs on the home screen"""
from . import *
from MyWeather.View.utils.enumerations import *
from MyWeather.Init.MainWindowInits import GraphInit
from .GraphBody import WeatherGraph
from PyQt6.QtCore import pyqtSlot




class GraphFrame(QFrame):
    """Main class for the frame"""

    def __init__(self, sheet):
        super().__init__()


        self.setObjectName("GraphFrame")
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        
        
        (layout := QVBoxLayout()).addLayout(header := GraphInit.GetGraphHeader())
        (graph_layout := QHBoxLayout()).addWidget(graph := WeatherGraph())
        layout.addLayout(graph_layout)

        self.graph = graph
        self.header = header
        
        layout.setStretch(0,10)
        layout.setStretch(1,90)

        graph_layout.setContentsMargins(0,0,0,0)
        graph_layout.setSpacing(0)

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.setStyleSheet(sheet.value)

    



