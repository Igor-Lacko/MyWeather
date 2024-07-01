"""Contains the header text and buttons to switch days which are shown in the graph"""
from . import *
from PyQt6.QtGui import QIcon, QFont
from MyWeather.View.utils.enumerations import *


class FrameHeader(QHBoxLayout):
    """Graph header class\n
    -initialized as a layout with a dummy widget with a layout instead of just a layout to round out the QFrame borders nicely
    """

    stretch_dict = {
        0   :   10,
        1   :   80,
        2   :   10
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
        header_layout.addLayout(title := TitleMenu(range))
        header_layout.addWidget(right_button := QPushButton())

        self.widgets = [left_button, title, right_button]

        self.SetStretch(header_layout)
        self.InitItems()

        self.addWidget(header_widget)



    def SetStretch(self, layout):
        """Sets the stretch according to the stretch_dict dictionary"""
        for index, stretch in self.stretch_dict.items():
            layout.setStretch(index, stretch)
            if type(self.widgets[index]) != TitleMenu:
                self.widgets[index].setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)



    def InitItems(self):
        """Initializes the button icons (so far only the icons), TODO: color modes"""
        (right_button := self.widgets[0]).setIcon(QIcon(f"Assets/GraphFrameIcons/{MODE.value}/left-arrow.png"))
        (left_button := self.widgets[2]).setIcon(QIcon(f"Assets/GraphFrameIcons/{MODE.value}/right-arrow.png"))



    


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

        self.menu.addItems(["Temp", "Rain", "Wind"])

        for widget in [self.text_widget, self.menu]:
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.InitTextStyle(self.text_widget)

        


    def InitTextStyle(self, text : QLabel):
        """Sets the text style, font and font size"""
        text.setAlignment(Alignments.Center)
        text.setFont(QFont("Ubuntu", pointSize=15))
        text.setStyleSheet("""QLabel{
                            border-right: 2px solid silver;
                            border-left: 2px solid silver;
                            border-bottom: none;
                            border-top: none;
                            }""")