"""Contains a custom QLabel class used as a title with overriden move event to emit the new position"""
from . import *
from PyQt6.QtCore import QPoint, pyqtSignal
from MyWeather.View.utils.enumerations import Alignments




class Title(QLabel):
    moved = pyqtSignal(QPoint)
    def __init__(self, pointsize : int, font : QFont, text : str, width : int):
        """This class exists for a custom QEvent but why not pass some things by default to the constructor?"""
        super().__init__()
        self.setText(text)
        self.setFont(QFont(font, pointSize=pointsize))
        self.setAlignment(Alignments.Center)
        self.setFixedWidth(width)     #so that the text is always centered during the animation




