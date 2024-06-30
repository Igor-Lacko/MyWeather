from PyQt6.QtWidgets import *
from MyWeather.Controller import HeaderController
from ..components.Home.Header import Header
from ..components.Home.HomeWindow import HomeWindow

class HomeTab(QVBoxLayout):
    """contains the home tab for the application

    Args:
        QVBoxLayout (QVBoxLayout): Has items aligned vertically
    """

    def __init__(self):
        """home tab constructor"""
        super().__init__()

        self.addWidget(header := HeaderController.GetHeader())
        self.header : Header = header

        self.addWidget(main := HomeWindow())
        self.window : HomeWindow = main
        
        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)
        self.setStretch(0, 10)
        self.setStretch(1, 90)
