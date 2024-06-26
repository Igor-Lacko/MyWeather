from ..utils.enumerations import Colors
from PyQt6.QtWidgets import *
from PyQt6 import QtGui as gui
from PyQt6.QtCore import Qt

class ColoredBar(QWidget):
    """Basic colored widget, primarily used for testing

    Args:
        QWidget (QWidget): Inherits from the basic qwidget class
    """
    def __init__(self, text="text", color=Colors.CoolGrey):
        super().__init__()
        self.setAutoFillBackground(True)


        palette = self.palette()
        palette.setColor(gui.QPalette.ColorRole.Window, color)


        self.setPalette(palette)

        (label := QLabel(text=str(text))).setAlignment(Qt.AlignmentFlag.AlignCenter)
        (layout := QHBoxLayout()).addWidget(label)

        self.setLayout(layout)