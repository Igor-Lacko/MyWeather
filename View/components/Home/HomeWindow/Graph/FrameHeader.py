"""Contains the header text and buttons to switch days which are shown in the graph"""
from . import *
from PyQt6.QtGui import QIcon, QFont
from MyWeather.View.utils.enumerations import *


class FrameHeader(QHBoxLayout):
    """Graph header class\n
    -initialized as a layout with a dummy widget with a layout instead of just a layout to round out the QFrame borders nicely
    """
    def __init__(self, range : str):
        """Frame header constructor

        Args:
            range (str): The range of the dates to be displayed on the header, such as "The forecast from DD.MM.YY to DD.MM.YY"
        """
        super().__init__()
        
        (header_widget := QWidget()).setLayout(header_layout := QHBoxLayout())
        header_widget.setObjectName("header_widget")

        header_layout.addWidget(left_button := QPushButton())
        header_layout.addLayout(title := TitleMenu(range))
        header_layout.addWidget(right_button := QPushButton())

        self.left_button = left_button
        self.title = title
        self.right_button = right_button

        self.SetColor(MODE)

        self.addWidget(header_widget)


        header_layout.setStretch(0, 10)
        header_layout.setStretch(1, 80)
        header_layout.setStretch(2, 10)
        header_layout.setContentsMargins(0,0,0,0)
        header_layout.setSpacing(0)



    def SetColor(self, mode : ColorModes):
        """Initializes the button icons (so far only the icons). Called on __init__()

        Args:
            mode (ColorModes): The provided color mode
        """
        self.left_button.setIcon(QIcon(f"Assets/GraphFrameIcons/{mode.value}/left-arrow.png"))
        self.right_button.setIcon(QIcon(f"Assets/GraphFrameIcons/{mode.value}/right-arrow.png"))



    


class TitleMenu(QHBoxLayout):
    """Helper layout that contains the frame header's menu and title"""
    def __init__(self, range):
        super().__init__()
        
        self.addWidget(text := QLabel(text=range))
        self.addWidget(menu := QComboBox())
        self.setStretch(0,90)
        self.setStretch(1,10)

        self.setContentsMargins(0,0,0,0)
        self.setSpacing(0)

        self.text_widget = text
        self.menu = menu

        self.text_widget.setObjectName("title_widget")
        self.menu.addItems(["Temp", "Rain", "Wind"])

        for widget in [self.text_widget, self.menu]:
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.InitTextStyle(self.text_widget)
        self.menu.setFont(QFont(FONTS.graph_header))


        


    def InitTextStyle(self, text : QLabel):
        """Sets the text style, font and font size"""
        text.setAlignment(Alignments.Center)
        text.setFont(QFont(FONTS.graph_header, pointSize=15))

    
    
    def ChangeTitle(self, date_str : str, location : str): 
        self.text_widget.setText(f"Forecast for {date_str}, {location}")

    
        
    def UpdateFonts(self, font : str):
        """Called inside the settings"""

        for widget in [self.text_widget, self.menu]:
            widget.setFont(QFont(font, pointSize=15))