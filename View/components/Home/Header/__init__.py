"""Contains the header for the home tab, with a icon, temperature and some other data with all it's sub-components"""
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtCore import Qt, pyqtSlot
from MyWeather.Model.obj import Realtime
from MyWeather.View.utils.enumerations import *
from MyWeather.View.constdata.mode import DEFAULT
from .LeadText import HeaderLeadText
from .Data import HeaderDataText



class Header(QWidget):
    """Contains the header for the home tab, should roughly look like this

    ------------------------------------------------
    ||ICON|TMP/FEELSLIKE|    CITY, COUNTRY, DATE  ||        ICON: 10% of the layout
    ||ICON|TMP/FEELSLIKE|    -WIND SPEED/DIRECTION||        TMP: 10%, should be a VBOX layout with 50% elements
    ||ICON|CONDITION    |    -PRECIP HEIGHT       ||        LOCATION/WEATHER: 80% of the layout, should also be vbox with 40% city and 20% others
    ||ICON|CONDITION    |    -HUMIDITY PERCENT    ||        OTHER: Should set background
    ------------------------------------------------

    Args:
        QWidget (QWidget): Inherits from QWidget, easier border control
    """
    #constant variable
    stretch_dict = {
        0 : 10,
        1 : 10,
        2 : 80
    }

    def __init__(self, data : Realtime, icon_path : str):
        """Header constructor, sets up the layouts

        Args:
            data (Realtime): Contains the realtime weather data
            icon_path (str): Path to the icon depending on the weather condition
        """
        super().__init__()

        self.setLayout(header_layout := QHBoxLayout())
        header_layout.setContentsMargins(0,0,0,0)                               #initialize the main horizontal layout   
        self.header_layout = header_layout


        self.subcomponents = []                                                 #appended to with every method call


    #------------------------------ADDING WIDGETS-------------------------------------------#

        self.AddIcon(icon_path)                                                         #entry icon

        self.header_layout.addLayout(lead_widget := HeaderLeadText(data, DEFAULT))      #lead text
        self.subcomponents.append(lead_widget)


        self.header_layout.addLayout(data_widget := HeaderDataText(data, DEFAULT))      #main data text
        self.subcomponents.append(data_widget)



    #-----------------------------SET STYLING-----------------------------------------------#
        self.SetStyle(DEFAULT)



    
    
    def SetStyle(self, color_mode : ColorModes):
        """Sets the visual appearance of the header on initialization

        Args:
            color_mode (ColorModes): The color mode on initialization
        """
        self.setAutoFillBackground(True)                                        #turn on the autofill property

        (palette := self.palette()).setColor(QPalette.ColorRole.Window,
        Colors.CoolGrey if color_mode == ColorModes.DARK                        #set a background color
        else Colors.OffWhite)

        self.setPalette(palette)
        self._palette_ = palette


        

        self.setStretch()








    
    def AddIcon(self, path):
        """Adds a icon to the left of the header depending on the weather condition

        Args:
            path (str, optional): path to the icon
        """
        (icon := QLabel()).setPixmap(QPixmap(path).scaled(
            100,
            100,        
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
            ))
        
        icon.setAlignment(Alignments.Center)
        
        self.header_layout.addWidget(icon)
        self.subcomponents.append(icon)


    def setStretch(self):
        """sets stretch at every element according to the stretch_dict dictionary"""
        
        for index, stretch in Header.stretch_dict.items():
            self.header_layout.setStretch(index, stretch)

    
    @pyqtSlot(ColorModes)
    def SwitchColorMode(self, mode : ColorModes):
        """Switches the Home tab's header color mode

        Args:
            mode (ColorModes): the current color mode, switching to the other
        """
        self.SetLightMode() if mode.value == "light"\
        else self.SetDarkMode()




    def SetLightMode(self):
        """Switches the current color mode to light"""
        self._palette_.setColor(QPalette.ColorRole.Window, Colors.OffWhite)
        self.setPalette(self._palette_)

        
        for div in self.subcomponents[1:]:
            div.SetColor(ColorModes.LIGHT)

    def SetDarkMode(self):
        """Switches the current color mode to dark"""
        self._palette_.setColor(QPalette.ColorRole.Window, Colors.CoolGrey)
        self.setPalette(self._palette_)
        
        for div in self.subcomponents[1:]:
            div.SetColor(ColorModes.DARK)

