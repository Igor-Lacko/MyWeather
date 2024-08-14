"""Module containing the menu that appears after the user makes his API choice"""
from . import *
from PyQt6.QtCore import pyqtProperty
from MyWeather.View.utils.enumerations import ColorModes
from MyWeather.View.StyleSheets.ListView import Dark, Light
from .Option import *

class OptionMenu(QFrame):
    def __init__(self, active : str):
        """Option menu constructor

        Args:
            active (str): The API choice
        """

        super().__init__()
        self.setObjectName("optionmenu")

        self._layout_ = QVBoxLayout()
        self._layout_.setSpacing(0)
        self._layout_.setContentsMargins(0,0,0,0)
        self.setLayout(self._layout_)

        self.active = active
        self.realtime_items = self.forecast_items = self.history_items = []


    def SetColorMode(self, mode : ColorModes):
        """Only used for applying a style sheet to the ListView of the options. The weather tab itself handles widget color changes

        Args:
            mode (ColorModes): The color mode to be set stylesheet to
        """
        for item in self.items:
            if isinstance(item, LineEditOption) or isinstance(item, ComboBoxOption):
                item.completer.popup().setStyleSheet((Dark if mode == ColorModes.DARK else Light).ListViewPopup)

    @pyqtProperty(list)
    def items(self):
        return self.realtime_items if self.active == "realtime" else (self.forecast_items if self.active == "forecast" else self.history_items)