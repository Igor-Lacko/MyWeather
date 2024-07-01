"""Contains the main part of the Home tab (so everything other than the header."""
from PyQt6.QtGui import QPaintEvent, QPainter, QImage
from PyQt6.QtWidgets import *
from MyWeather.View.utils.enumerations import *
from .Graph.GraphFrame import GraphFrame
from MyWeather.Init import DEFAULT_MODE
from PyQt6.QtCore import pyqtSlot




class HomeWindow(QWidget):
    """The main widget for the Home tab"""
    
    
    def __init__(self):
        super().__init__()


        self.background = f"Assets/Backgrounds/{DEFAULT_MODE.value}/home-background.jpg"

        self.InitLayout()
                
        

    def paintEvent(self, event: QPaintEvent | None) -> None:
        (painter := QPainter()).begin(self)
        print(self.background)
        painter.drawImage(event.rect(), QImage(self.background))

    def InitLayout(self):
        """Initializes the combination of vertical/horizontal layouts due to more complicated logic"""
        
        vertical = QVBoxLayout()
        horizontal = QHBoxLayout() #contains the graph frame

        horizontal.addSpacerItem(QSpacerItem(10,10))
        horizontal.addWidget(graph := GraphFrame(StyleSheets.dark.GraphFrame if DEFAULT_MODE == ColorModes.DARK else StyleSheets.light.GraphFrame))
        horizontal.addSpacerItem(QSpacerItem(10,10))

        horizontal.setStretch(0,1)
        horizontal.setStretch(1,2)
        horizontal.setStretch(2,1)

        vertical.addWidget(QWidget())
        vertical.addLayout(horizontal)

        vertical.setStretch(0,1)
        vertical.setStretch(1,2)

        self.setLayout(vertical)
        self.graph = graph

    
    @pyqtSlot(ColorModes)
    def switch_color_mode(self, mode : ColorModes):
        """Swaps the background image according to the mode"""
        self.background = f"Assets/Backgrounds/{mode.value}/home-background.jpg"
        self.update()

        