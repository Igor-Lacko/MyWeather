from enum import Enum

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
        border: none;
        background: transparent;
    }
    
    QPushButton:hover:!pressed{
        background-color: #11c0c0c0;
    }
    """

    SettingsMain = """QWidget{
        background-color: rgb(33,33,33)
    }"""

    SettingsItem = """QFrame#theme, QFrame#bottom{
        border: 3px solid silver;
        background-color: rgb(33,33,33);
    }

    QFrame#location{
        border-top: none;
        border-left: 3px solid silver;
        border-right: 3px solid silver; 
        border-bottom: 3px solid silver;
    }

    QFrame{
        border-right: 3px solid silver;
        border-left: 3px solid silver;
        border-top: 3px solid silver;
        border-bottom: none;
    }
    
    QLabel{
        border-right: 2px solid silver;
        border-left: none;
        border-top: none;
        border-bottom: none;
        color: silver;
    }

    QLabel#general, QLabel#font{
        border: none;
        color: silver;
    }

    QComboBox{
        border-left: 2px solid silver;
        border-right: none;
        border-top: none;
        border-bottom: none;
        color: silver;
        background-color: transparent;
        subcontrol-origin: left;
        selection-background-color: #11c0c0c0;
        selection-color: silver;
    }

    QComboBox:hover:!pressed{
            border-top: none;
            border-bottom: none;
            border-left: 2px solid silver;
            border-right: none;
            color: silver;
            background-color: #11c0c0c0;
        }
    
    QComboBox QAbstractItemView{
        background: rgb(33,33,33);
        color: silver;
        border: 2px solid white;
        selection-background-color: #11c0c0c0;
        selection-color: silver;
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
        border: none;
        background: transparent;
    }
    
    QPushButton:hover:!pressed{
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

    SettingsMain = """QWidget{
        background-color: rgb(250, 249, 246);
    }"""

    SettingsItem = """QFrame#theme, QFrame#bottom{
        border: 3px solid black;
        background-color: rgb(250,249,246);
    }

    QFrame#location{
        border-top: none;
        border-left: 3px solid black;
        border-right: 3px solid black;
        border-bottom: 3px solid black;
    }

    QFrame{
        border-left: 3px solid black;;
        border-right: 3px solid black;
        border-top: 3px solid black;
        border-bottom: none;
    }
    
    QLabel{
        border-right: 2px solid black;
        border-left: none;
        border-top: none;
        border-bottom: none;
        color: black;
    }

    QLabel#general, QLabel#font{
        color: black;
        border: none;
    }


    QComboBox{
        border-left: 2px solid black;
        border-right: none;
        border-top: none;
        border-bottom: none;
        color: black;
        background-color: transparent;
        subcontrol-origin: left;
        selection-background-color: #11000000;
        selection-color: black;
    }

    QComboBox:hover:!pressed{
            border-top: none;
            border-bottom: none;
            border-left: 2px solid black;
            border-right: none;
            color: black;
            background-color: #11000000;
        }
    
    QComboBox QAbstractItemView{
        background: rgb(250,249,246);
        color: black;
        border: 2px solid black;
        selection-background-color: #11000000;
        selection-color: black;
    }



    
    """



class StyleSheets: 
    """Acts as a list of some predefined stylesheet enumerations to be used"""
    dark = DarkStyleSheets
    light = LightStyleSheets

