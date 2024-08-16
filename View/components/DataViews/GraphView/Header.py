"""Module containing the graph header superclass and all subclasses"""
from . import *
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import pyqtSlot
from MyWeather.View.utils.enumerations import ColorModes #absolute import to avoid enum comparision issues


class BaseGraphHeader(QFrame):
    """Graph header superclass, enough only for realtime weather, multiple-day superclass inherits from this"""
    def __init__(self, **data):
        """Graph header constructor, default graph header has these items: \n 
        - a title with a Forecast for {city}, {country}, {date}\n
        - a menu to choose what data will the graph show (temperature, rain, wind, sunset/sunrise) 

        Args:
            data (dict[str,str]): A set of keyword arguments, only one used in subclass is the location and current date
        """
        super().__init__()
        self.setObjectName("header_widget")

        #set the data description based on the api
        self.description = "Data" if data['api'] == "history" else "Forecast"

        #initialize the layout/spacing
        self._layout_ = QHBoxLayout()
        self._layout_.setContentsMargins(0,0,0,0)
        self._layout_.setSpacing(0)
        self.setLayout(self._layout_)

        #initialize the title and menu
        self._layout_.addWidget(self.GetTitle(data['date'], data['location'], False if data['api'] == 'history' else True), stretch=90)
        self._layout_.addWidget(self.GetMenu(), stretch=10)



    def GetTitle(self, date : str, location : str, forecast : bool=True):
        """Returns a QLabel with the graph data's location and date

        Args:
            date (str): Date in the format DD.MM.YYYY
            location (str): Location in the format City/Town, Country
            forecast (bool): Defaults to true (since both Realtime and Forecast APIs use Forecast and only history API uses Data), whether the title shows Forecast for... or Data for...
        """

        #initialize the title
        (title := QLabel(text=f"{'Forecast' if forecast else 'Data'} for {location}, {date}"))\
        .setFont(QFont(FONTS.graph_header, pointSize=15))
        title.setAlignment(Alignments.Center)
        title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #add it to the widget
        self.title = title
        return title


    def GetMenu(self):
        """Returns a QComboBox with the data choices as items"""

        #initialize the menu
        (menu := QComboBox()).addItems(["Temp", "Wind", "Rain", "Water"])
        menu.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        menu.setFont(QFont(FONTS.graph_header, pointSize=14))

        #add it to the widget
        self.menu = menu
        return menu

    @pyqtSlot(str)
    def UpdateFonts(self, font : str):
        """Called inside settings when the Graph Header font is set to a new one

        Args:
            font (str): The new font
        """

        for widget in [self.title. self.menu]:
            widget.setFont(QFont(font, pointSize=15))



class ExtendedGraphHeader(BaseGraphHeader):
    """Graph header subclass which can include multiple days"""

    def __init__(self, **data):
        """Extended graph header constructor

        Args:
            data (dict[str,str]): Used with some new keyword arguments, such as day range or API choice
        """
        super().__init__(**data)

        #add buttons
        self.AddButtons(data['color_mode'])



    def AddButtons(self, mode : ColorModes):
        """Initializes the left/right buttons which aren't included in the base class

        Args:
            mode (ColorModes): The initial color mode (used for settring an icon to the buttons)
        """

        #initialize the buttons and their names
        self.left_button = QPushButton()
        self.right_button = QPushButton()
        self.left_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.right_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.left_button.setObjectName("left_button")
        self.right_button.setObjectName("right_button")

        #set the initial color scheme
        self.SetButtonIcons(mode)

        #insert the buttons into the layout
        self._layout_.insertWidget(0, self.left_button, stretch=10)
        self._layout_.addWidget(self.right_button, stretch=10)

        #align the title and menu so they take up 80% of the layout (so that the stretches add up to 100)
        self._layout_.setStretch(1, 72)             #title
        self._layout_.setStretch(2, 8)              #menu



    def SetButtonIcons(self, mode : ColorModes):
        """Sets an icon to the left and right buttons depending on the mode argument

        Args:
            mode (ColorModes): The color mode scheme of the icons
        """
        self.left_button.setIcon(QIcon(f"Assets/GraphFrameIcons/{mode.value}/left-arrow.png"))
        self.right_button.setIcon(QIcon(f"Assets/GraphFrameIcons/{mode.value}/right-arrow.png"))



    def ChangeTitle(self, date : str, location : str):
        """Updates the graph's title based on the parameters

        Args:
            date (str): _description_
            location (str): _description_
        """

        self.title.setText(f"{self.description} for {location}, {date}")
