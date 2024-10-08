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

    #custom clicked signal since it's a subclassed QFrame, which will emit it's data
    clicked = pyqtSignal(obj.Day)

    def __init__(self, data : obj.Day, color_mode : ColorModes):
        """Graph picker constructor

        Args:
            data (obj.Day): The weather data provided, only used to get a condition and a icon from that
            color_mode (ColorModes): Passed as a parameter and used as an instance attribute since it would be much more tedious to handle from the parent widget
        """
        super().__init__()

        #keep the data as an instance attribute to later emit it
        self.data = data

        #keep the color scheme as a instance attribute
        self.color_mode = color_mode

        #states to change stylesheets
        self.pressed = self.hovered = self.submitted = self.set = False

        #keep the condition as an instance attribute for the icon
        self.condition = self.data.condition.lower()

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
        self.text = QLabel(text=f"{self.data.location}\n{self.data.date_str}")
        self.text.setFont(QFont(FONTS.weather_tab, pointSize=20))
        self.text.setAlignment(Alignments.Center)
        self.text.setWordWrap(True)
        self._layout_.addWidget(self.text, stretch=50)

        #set object names for the style sheets
        self.setObjectName("main")
        self.icon.setObjectName("icon")
        self.text.setObjectName("text")

        self.setLayout(self._layout_)
        super().setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).Idle)




    def GetIcon(self) -> QPixmap:
        """Returns a icon path to the daily condition

        Returns:
            QPixmap: Initialized and scaled icon
        """
        for icon in Icons:
            if self.condition.lower().strip() in icon['conditions']:
                return QPixmap(icon['day']).scaled(
                    100,
                    100,
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
                self.clicked.emit(self.data)
                self.submitted = True


    def setStyleSheet(self):
        """Override of setStyleSheet, checks states and sets the sheet based on that\n
        - If the submitted state is set to True, the StyleSheet isn't set because the widget's animation is ongoing"""

        if not self.submitted and self.set:
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
    """Custom return option displayed alongside the graph pickers which function as a similar way"""

    clicked = pyqtSignal()

    def __init__(self, color_mode : ColorModes):
        """Return option constructor

        Args:
            color_mode (ColorModes): Passed as a parameter and used as an instance attribute since it would be much more tedious to handle from the parent widget
        """

        super().__init__()

        #instance attributes and states
        self.color_mode = color_mode
        self.pressed = self.hovered = self.submitted = self.set = False

        #initialize layout and set spacing to zero
        (_layout_ := QVBoxLayout()).setContentsMargins(0,0,0,0)
        _layout_.setSpacing(0)

        self._layout_ = _layout_

        #add a icon
        self.icon = QLabel()
        self.icon.setPixmap(self.GetIcon())
        self.icon.setAlignment(Alignments.Center)
        self._layout_.addWidget(self.icon, stretch=50)

        #add text
        self.text = QLabel(text="Return to API selection")
        self.text.setFont(QFont(FONTS.weather_tab, pointSize=20))
        self.text.setAlignment(Alignments.Center)
        self.text.setWordWrap(True)
        self._layout_.addWidget(self.text, stretch=50)

        #set object names for the style sheets
        self.setObjectName("main")
        self.icon.setObjectName("icon")
        self.text.setObjectName("text")

        self.setLayout(self._layout_)
        super().setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).Idle)



    def GetIcon(self) -> QPixmap:
        """Returns a initialized QPixmap icon"""
        return QPixmap(f'Assets/door-{self.color_mode.value}.png').scaled(
            100,
            100,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )


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
                self.submitted = True


    def setStyleSheet(self):
        """Override of setStyleSheet, checks states and sets the sheet based on that\n
        - If the submitted state is set to True, the StyleSheet isn't set because the widget's animation is ongoing"""

        if not self.submitted and self.set:
            #imitation of QPushButton's hover:!pressed state
            if self.hovered and not self.pressed:
                super().setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).Hover)

            else:
                super().setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).Idle)


    def SwitchColorMode(self):
        """Switches the current color mode and sets a style sheet"""
        self.color_mode = ColorModes.DARK if self.color_mode == ColorModes.LIGHT else ColorModes.LIGHT
        self.icon.setPixmap(self.GetIcon())
        self.setStyleSheet()