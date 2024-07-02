"""Contains the main frame for showing the weather graphs on the home screen"""
from . import *
from MyWeather.View.utils.enumerations import *
from MyWeather.Init.MainWindowInits import GraphInit
from .GraphLayout import GraphLayout
from PyQt6.QtCore import pyqtSlot




class GraphFrame(QFrame):
    """Main class for the frame"""

    def __init__(self, sheet):
        super().__init__()


        self.setObjectName("GraphFrame")
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        
        
        (layout := QVBoxLayout()).addLayout(header := GraphInit.GetGraphHeader())
        layout.addLayout(graph := GraphLayout())

        self.graph = graph
        self.header = header
        
        layout.setStretch(0,10)
        layout.setStretch(1,90)

        

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.setStyleSheet(StyleSheets.light.GraphFrame.value)
        self.header.widgets[1].menu.currentIndexChanged.connect(self.graph.SwitchGraph)

    



