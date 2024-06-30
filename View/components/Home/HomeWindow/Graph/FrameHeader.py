"""Contains the header text and buttons to switch days which are shown in the graph"""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QFont
from MyWeather.View.utils.enumerations import *


class FrameHeader(QHBoxLayout):
    """Graph header class\n
    -initialized as a layout with a dummy widget with a layout instead of just a layout to round out the QFrame borders nicely
    """

    stretch_dict = {
        0   :   1,
        1   :   8,
        2   :   1
    }
    
    def __init__(self, range : str):
        """Frame header constructor

        Args:
            range (str): The range of the dates to be displayed on the header, such as "The forecast from DD.MM.YY to DD.MM.YY"
        """
        super().__init__()
        
        (header_widget := QWidget()).setLayout(header_layout := QHBoxLayout())
        header_widget.setObjectName("header_widget")

        header_layout.addWidget(left_button := QPushButton())
        header_layout.addWidget(title := QLabel(text=range))
        header_layout.addWidget(right_button := QPushButton())

        self.widgets = [left_button, title, right_button]

        self.SetStretch(header_layout)
        self.InitItems()

        self.addWidget(header_widget)



    def SetStretch(self, layout):
        """Sets the stretch according to the stretch_dict dictionary"""
        for index, stretch in self.stretch_dict.items():
            layout.setStretch(index, stretch)
            self.widgets[index].setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        layout.setContentsMargins(0,0,0,0)



    def InitItems(self):
        """Initializes the text and button icons (so far only the icons), TODO: color modes"""
        self.InitTextStyle(self.widgets[1])

        (right_button := self.widgets[0]).setIcon(QIcon("Assets/GraphFrameIcons/dark/left-arrow.png"))
        (left_button := self.widgets[2]).setIcon(QIcon("Assets/GraphFrameIcons/dark/right-arrow.png"))



    def InitTextStyle(self, text : QLabel):
        """Sets the text style, font and font size"""
        text.setAlignment(Alignments.Center)
        text.setFont(QFont("Ubuntu", pointSize=15))

