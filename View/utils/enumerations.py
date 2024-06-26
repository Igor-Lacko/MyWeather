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
    Justify = Qt.AlignmentFlag.AlignJustify


class Colors:
    """list of some used colors whose purpose is to remove some boilerplate around RGB values"""

    CoolGrey = QColor(33, 33, 33)
    Cream = QColor(255, 253, 208)
    UbuntuOrange = QColor(233, 84, 32)
    OffWhite = QColor(250, 249, 246)
    Indigo = QColor(75, 0, 130)



class DarkStyleSheets(Enum):
    """Style sheets for dark mode components

    Args:
        Enum (Enum): Inherits from the Enum class
    """ 
    SidebarButtonDefault = """QToolButton{
        font-family: times;
        background: transparent;
        border: none;
    }"""

    SidebarButtonTop = """QToolButton{
        font-family: times;
        background: transparent;
        border-top: 3px solid gray;
    }"""

    SidebarButtonBottom = """QToolButton{
        font-family: times;
        background: transparent;
        border-bottom: 3px solid gray;
        border-style: solid;
    }"""

    SidebarButtonHover = """QToolButton:hover:!pressed{
        background-color: #11c0c0c0;
    }"""

    


class LightStyleSheets(Enum):
    """Style sheets for light mode components

    Args:
        Enum (Enum): Inherits from the Enum class
    """ 
    SidebarButtonDefault = """QToolButton{
        font-family: times;
        color: black;
        background: transparent;
        border: none;
    }"""

    SidebarButtonTop = """QToolButton{
        font-family: times;
        color: black;
        background: transparent;
        border-top: 3px solid black;
    }"""

    SidebarButtonBottom = """QToolButton{
        font-family: times;
        color: black;
        background: transparent;
        border-bottom: 3px solid black;
        border-style: solid;
    }"""

    SidebarButtonHover = """QToolButton:hover:!pressed{
        background-color: #11000000;
    }"""

    







class StyleSheets: 
    """Acts as a list of some predefined stylesheet enumerations to be used"""
    dark = DarkStyleSheets
    light = LightStyleSheets


class ColorMode(Enum):
    DARK = "dark"
    LIGHT = "light"

