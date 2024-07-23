"""Contains the entire weather tab"""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPaintEvent, QPainter, QImage
from PyQt6.QtCore import pyqtSlot
from MyWeather.View.utils.enumerations import ColorModes
from MyWeather.Constdata.Mode import MODE

class WeatherTab(QWidget):
    """Weather tab class"""
    def __init__(self):
        super().__init__()
        self.background = f"Assets/Backgrounds/{MODE.value}/bg-weather.jpg"
        self.color_mode = MODE


    def paintEvent(self, event: QPaintEvent | None) -> None:
        (painter := QPainter()).begin(self)
        painter.drawImage(event.rect(), QImage(self.background))


    @pyqtSlot(ColorModes)
    def SetColorMode(self, mode : ColorModes):
        """Swaps the background image of the weather tab and updates it's components' color scheme"""
        self.background = f"Assets/Backgrounds/{mode.value}/bg-weather.jpg"
        self.update()


