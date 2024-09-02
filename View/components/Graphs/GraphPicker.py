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

    def __init__(self, data : obj.Day, color_mode : ColorModes):
        """Graph picker constructor

        Args:
            data (obj.Day): The weather data provided, only used to get a condition and a icon from that
            color_mode (ColorModes): Passed as a parameter and used as an instance attribute since it would be much more tedious to handle from the parent widget
        """
        super().__init__()

        #keep the color scheme as a instance attribute
        self.color_mode = color_mode

        #states to change stylesheets
        self.pressed = self.hovered = False

        #keep the condition as an instance attribute for the icon
        self.condition = data.condition.lower()

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
        self.text = QLabel(text=f"{data.location}\n{data.date_str}")
        self.text.setFont(QFont(FONTS.weather_tab, pointSize=31))
        self.text.setAlignment(Alignments.Center)
        self.text.setWordWrap(True)
        self._layout_.addWidget(self.text, stretch=50)

        #set object names for the style sheets
        self.setObjectName("main")
        self.icon.setObjectName("icon")
        self.text.setObjectName("text")

        self.setLayout(self._layout_)
        self.setStyleSheet()



    def GetIcon(self) -> QPixmap:
        """Returns a icon path to the daily condition

        Returns:
            QPixmap: Initialized and scaled icon
        """
        for icon in Icons:
            if self.condition in icon['conditions']:
                return QPixmap(icon['day']).scaled(
                    200,
                    200,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

        raise FileNotFoundError(f"Wrong condition '{self.condition}'")


    def enterEvent(self, event):
        """Sets hover state to True"""
        self.hovered = True
        self.setStyleSheet()
        super().enterEvent(event)


    def leaveEvent(self, event):
        """Sets hover state to False"""
        self.hovered = False
        self.setStyleSheet()
        super().leaveEvent(event)


    def mousePressEvent(self, event):
        """Checks the event button and sets pressed state to True if needed"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = True
            self.setStyleSheet()

        super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        """Checks the event button, sets pressed to false if needed and if the user is hovering over it (signalling intention to click) emits the clicked signal"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.pressed = False
            self.setStyleSheet()

            if self.hovered:
                self.clicked.emit()


    def setStyleSheet(self):
        """Override of setStyleSheet, checks states and sets the sheet based on that"""

        #imitation of QPushButton's hover:!pressed state
        if self.hovered and not self.pressed:
            super().setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).Hover)

        else:
            super().setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).Idle)


    def SwitchColorMode(self):
        """Switches the current color mode and sets a style sheet"""
        self.color_mode = ColorModes.DARK if self.color_mode == ColorModes.LIGHT else ColorModes.LIGHT
        self.setStyleSheet()



class ReturnOption(QFrame):
    """Custom return option displayed alongside the graph pickers"""

    def __init__(self):
        """Return option constructor"""
        super().__init__()
        self.setObjectName("graph_picker_return")

        #initialize layout and set spacing to zero
        (_layout_ := QVBoxLayout()).setContentsMargins(0,0,0,0)
        _layout_.setSpacing(0)

        #add a image
        _layout_.addWidget(image := QLabel(), stretch=85)
        image.setObjectName("graph_picker_return_image")


        #add a button
        _layout_.addWidget(button := QPushButton(text="Return to API selection"), stretch=15)
        button.setFont(QFont(FONTS.weather_tab, pointSize=20))
        button.setObjectName("graph_picker_return_button")

        #add access to the button as a instance variable (to be later connected with signals/slots)
        self.button = button 

        #set fixed height since the widgets completely ignore stretch for whatever reason
        button.setFixedHeight(50)

        #set the layout
        self.setLayout(_layout_)
        self._layout_ = _layout_