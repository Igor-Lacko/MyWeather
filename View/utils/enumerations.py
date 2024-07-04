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
        background: transparent;
        border: none;
    }"""

    SidebarButtonTop = """QToolButton{
        background: transparent;
        border-top: 3px solid gray;
    }"""

    SidebarButtonBottom = """QToolButton{
        background: transparent;
        border-bottom: 3px solid gray;
        border-style: solid;
    }"""

    SidebarButtonHover = """QToolButton:hover:!pressed{
        background-color: #11c0c0c0;
    }"""


    HeaderData = """QLabel{
        color: silver;
        border: none;
    }"""

    HeaderLead = """QLabel{
        color: silver;
        border: none;
    }"""

    GraphFrame = """

    
        QFrame#GraphFrame{
            border: 5px solid silver;
            border-radius: 15px;
            background-color: rgb(33,33,33)
        }
    
        QPushButton{
            background: transparent;
            border: none;
        }

        QPushButton:hover:!pressed{
            background-color: #11c0c0c0;
        }

        QWidget#header_widget{
            border-bottom: 2px solid silver;
        }

        QLabel#title_widget{
            color: silver;
            border-left: 2px solid silver;
            border-right: 2px solid silver;
            border-bottom: none;
            border-top: none;
            background: transparent;
        }

    


        QComboBox{
            border-top: none;
            border-bottom: none;
            border-left: none;
            border-right: 2px solid silver;
            background: transparent;
            color: silver;
            selection-background-color: #11c0c0c0;
        }

        QComboBox:hover:!pressed{
            border-top: none;
            border-bottom: none;
            border-left: none;
            border-right: 2px solid silver;
            color: silver;
            background-color: #11c0c0c0;
        }
        
        QComboBox QAbstractItemView{
            background-color: rgb(33,33,33);
            color: silver;
        }

        


    """

    UpdateButton = """QPushButton{
        border: 1px solid white;
        background: transparent;
    }
    
    QPushButton:hover{
        background-color: #11c0c0c0;
    }
    """









class LightStyleSheets(Enum):
    """Style sheets for light mode components

    Args:
        Enum (Enum): Inherits from the Enum class
    """ 
    SidebarButtonDefault = """QToolButton{
        color: black;
        background: transparent;
        border: none;
    }"""

    SidebarButtonTop = """QToolButton{
        color: black;
        background: transparent;
        border-top: 3px solid black;
    }"""

    SidebarButtonBottom = """QToolButton{
        color: black;
        background: transparent;
        border-bottom: 3px solid black;
        border-style: solid;
    }"""

    SidebarButtonHover = """QToolButton:hover:!pressed{
        background-color: #11000000;
    }"""


    HeaderLead = """QLabel{
        color: black;
        border: none;
    }"""

    HeaderData = """QLabel{
        border: none;
        color: black;
    }"""

    UpdateButton = """QPushButton{
        border: 1px solid black;
        background: transparent;
    }
    
    QPushButton:hover{
        background-color: #11000000;
    }
    """


    HomeWindow = """QWidget{
        border-image: url('Assets/Backgrounds/light/home-background.jpg') 0 0 0 0 stretch stretch;
    }"""

    GraphFrame = """

    QFrame#GraphFrame{
            border: 7px solid black;
            border-radius: 15px;
            background-color: rgb(250,249,246)
        }
    
        QPushButton{
            background: transparent;
            border: none;
        }

        QPushButton:hover:!pressed{
            background-color: #11000000;
        }

        QWidget#header_widget{
            border-bottom: 2px solid black;
        }

        QLabel#title_widget{
            color: black;
            border-left: 2px solid black;
            border-right: 2px solid black;
            border-bottom: none;
            border-top: none;
            background: transparent;
        }

    


        QComboBox{
            border-top: none;
            border-bottom: none;
            border-right: 2px solid black;
            background: transparent;
            color: black; 
            selection-background-color: #11000000;
            padding: 1px 0px 1px 3px;
        }

        QComboBox:hover:!pressed{
            border-top: none;
            border-bottom: none;
            border-left: none;
            border-right: 2px solid black;
            color: black;
            background-color: #11000000;
        }

        QComboBox QAbstractItemView{
            background-color: rgb(250,249,246);
            color: black;
        }

        FigureCanvasQTAgg{
            border-bottom: 2px black solid;
        }


    """

    

    







class StyleSheets: 
    """Acts as a list of some predefined stylesheet enumerations to be used"""
    dark = DarkStyleSheets
    light = LightStyleSheets


class ColorModes(Enum):
    """Either dark or light"""
    DARK = "dark"
    LIGHT = "light"

