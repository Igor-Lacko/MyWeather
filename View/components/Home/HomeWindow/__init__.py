"""Contains the main part of the Home tab (so everything other than the header."""
from PyQt6.QtGui import QPaintEvent, QPainter, QImage
from PyQt6.QtWidgets import *
from MyWeather.View.utils.enumerations import *
from .Graph.GraphFrame import GraphFrame
from MyWeather.View.constdata.mode import DEFAULT




class HomeWindow(QWidget):
    """The main widget for the Home tab"""
    
    
    def __init__(self):
        super().__init__()

        self.color = Colors.CoolGrey if DEFAULT == ColorModes.DARK else Colors.OffWhite

        self.InitLayout()
                
        

    def paintEvent(self, event: QPaintEvent | None) -> None:
        (painter := QPainter()).begin(self)
        painter.drawImage(event.rect(), QImage('Assets/Backgrounds/home-background.jpg'))

    def InitLayout(self):
        """Initializes the combination of vertical/horizontal layouts due to more complicated logic"""
        
        vertical = QVBoxLayout()
        horizontal = QHBoxLayout() #contains the graph frame

        horizontal.addSpacerItem(QSpacerItem(10,10))
        horizontal.addWidget(GraphFrame(StyleSheets.dark.GraphFrame if DEFAULT == ColorModes.DARK else StyleSheets.light.GraphFrame))
        horizontal.addSpacerItem(QSpacerItem(10,10))

        horizontal.setStretch(0,1)
        horizontal.setStretch(1,2)
        horizontal.setStretch(2,1)

        vertical.addWidget(QWidget())
        vertical.addLayout(horizontal)

        vertical.setStretch(0,1)
        vertical.setStretch(1,1)

        self.setLayout(vertical)


        