from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from enum import Enum

class Alignments:
    """Enum of Qt alignments which will possibly be used, purpose is to provide some syntactic sugar"""

    Top = Qt.AlignmentFlag.AlignTop
    Bottom = Qt.AlignmentFlag.AlignBottom
    Left = Qt.AlignmentFlag.AlignLeft
    Right = Qt.AlignmentFlag.AlignRight
    TopLeft = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
    Center = Qt.AlignmentFlag.AlignCenter
    VerticalCenter = Qt.AlignmentFlag.AlignVCenter
    HorizontalCenter = Qt.AlignmentFlag.AlignHCenter
    TopCenter = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter
    BottomCenter = Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter
    TopRight = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop
    BottomLeft = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom
    BottomRight = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom
    CenterLeft = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
    CenterRight = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
    Justify = Qt.AlignmentFlag.AlignJustify


class Colors:
    """list of some used colors whose purpose is to remove some boilerplate around RGB values"""

    CoolGrey = QColor(33, 33, 33)
    Cream = QColor(255, 253, 208)
    UbuntuOrange = QColor(233, 84, 32)
    OffWhite = QColor(250, 249, 246)
    Indigo = QColor(75, 0, 130)


class ColorModes(Enum):
    """Either dark or light"""
    DARK = "dark"
    LIGHT = "light"

