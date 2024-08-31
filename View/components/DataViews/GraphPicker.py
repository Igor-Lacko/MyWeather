"""Includes the tabs (graph selectors) that appear when a user chooses Forecast or History API"""
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap
from MyWeather.Constdata.ConditionIcons import Icons
from MyWeather.Model import obj
from MyWeather.Init import FONTS
from MyWeather.View.utils.enumerations import Alignments, ColorModes
from MyWeather.View.StyleSheets.GraphPicker import Dark, Light


class GraphPicker(QFrame):
    """The graph selector frame"""

    #custom clicked signal since it's a subclassed QFrame
    clicked = pyqtSignal()

    def __init__(self, data : obj.Day, index : int, color_mode : ColorModes):
        """Graph picker constructor

        Args:
            data (obj.Day): The weather data provided, only used to get a condition and a icon from that
            index (int): Place of the picker in the list of them, used to set a object name for stylesheets
            color_mode (ColorModes): Passed as a parameter and used as an instance attribute since it would be much more tedious to handle from the parent widget
        """
        super().__init__()

        self.setObjectName(f"graphpicker{index}")

        self.color_mode = color_mode

        #states to change stylesheets
        self.pressed = self.hovered = False


        self.date = data.date_str
        self.condition = data.condition

        #initialize a VBox Layout with room for a date and icon
        self._layout_ = QVBoxLayout()
        self._layout_.setContentsMargins(0,0,0,0)
        self._layout_.setSpacing(0)

        #add a icon
        self.icon = QLabel()
        self.icon.setPixmap(self.GetIcon())
        self.icon.setAlignment(Alignments.Center)
        self._layout_.addWidget(self.icon, stretch=50)

        #add a label with the date of the day
        self.text = QLabel(text=self.date)
        self.text.setFont(QFont(FONTS.weather_tab, pointSize=17))
        self.text.setAlignment(Alignments.Center)
        self._layout_.addWidget(self.text, stretch=50)

        self.setLayout(self._layout_)




    def GetIcon(self) -> QPixmap:
        """Returns a icon path to the daily condition

        Returns:
            QPixmap: Initialized and scaled icon
        """
        for icon in Icons:
            if self.condition in icon['conditions']:
                return QPixmap(icon['day']).scaled(
                    50,
                    50,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

        raise FileNotFoundError("Wrong condition")


    def enterEvent(self, event):
        """Sets hover state to True"""
        self.hovered = True
        super().enterEvent(event)


    def LeaveEvent(self, event):
        """Sets hover state to False"""
        self.hovered = False
        super().leaveEvent(event)


    def mousePressEvent(self, event):
        """Checks the event button and sets pressed state to True if needed"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = True

        super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        """Checks the event button, sets pressed to false if needed and if the user is hovering over it (signalling intention to click) emits the clicked signal"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = False

            if self.hovered:
                self.clicked.emit()


    def setStyleSheet(self):
        """Override of setStyleSheet, checks states and sets the sheed based on that"""


