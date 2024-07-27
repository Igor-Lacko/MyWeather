"""Contains the main part of the Home tab (so everything other than the header."""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPaintEvent, QPainter, QImage
from PyQt6.QtCore import pyqtSlot
from MyWeather.View.Styles.Sheets import StyleSheets
from MyWeather.View.utils.enumerations import *
from .Graph.GraphFrame import GraphFrame
from MyWeather.Constdata.Mode import MODE




class HomeWindow(QFrame):
    """The main widget for the Home tab"""
    def __init__(self):
        super().__init__()
        self.setObjectName("homewindow")
        self.setStyleSheet((StyleSheets.dark if MODE == ColorModes.DARK else StyleSheets.light).HomeWindow.value)
        self.InitLayout()


    def InitLayout(self):
        """Initializes the combination of vertical/horizontal layouts due to more complicated logic"""
        
        vertical = QVBoxLayout()
        horizontal = QHBoxLayout() #contains the graph frame

        horizontal.addSpacerItem(QSpacerItem(10,10))
        horizontal.addWidget(graph := GraphFrame())
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
    def SwitchColorMode(self, mode : ColorModes):
        """Swaps the background image according to the mode and updates the graph's and header's color scheme"""
        self.setStyleSheet((StyleSheets.dark if mode == ColorModes.DARK else StyleSheets.light).HomeWindow.value)
        self.graph.SwitchColorMode(mode)


