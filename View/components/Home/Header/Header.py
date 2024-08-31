from . import *
from PyQt6.QtGui import QPixmap, QPalette, QIcon
from PyQt6.QtCore import Qt, pyqtSlot, pyqtSignal
from MyWeather.Controller import HeaderController
from .LeadText import HeaderLeadText
from .Data import HeaderDataText
from functools import partial
from MyWeather.Init import LOCATION



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
        0 : 20,
        1 : 20,
        2 : 158,
        3 : 2
    }

    update_data = pyqtSignal()
    fetch_new_data = pyqtSignal(dict)

    def __init__(self, data : Realtime, icon_path : str):
        """Header constructor, sets up the layouts

        Args:
            data (Realtime): Contains the realtime weather data
            icon_path (str): Path to the icon depending on the weather condition
        """
        super().__init__()

        self.setLayout(header_layout := QHBoxLayout())
        header_layout.setContentsMargins(0,0,0,0)                                           #initialize the main horizontal layout   
        self.header_layout = header_layout


        self.subcomponents = []                                                             #appended to with every method call


    #------------------------------ADDING WIDGETS-------------------------------------------#

        self.AddIcon(icon_path)                                                             #entry icon

        self.header_layout.addLayout(lead_widget := HeaderLeadText(data, MODE))             #lead text
        self.subcomponents.append(lead_widget)


        self.header_layout.addLayout(data_widget := HeaderDataText(data, MODE))             #main data text
        self.subcomponents.append(data_widget)

        self.header_layout.addWidget(self.GetUpdateButton(), alignment=Alignments.TopRight) #data update button



    #-----------------------------SET STYLING-----------------------------------------------#
        self.SetStyle(MODE)



    
    
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

    
    def GetUpdateButton(self) -> QPushButton:
        """Initializes the update button in the upper right corner (so far does nothing, TODO: actually update the Header content)

        Returns:
            QPushButton: The initialized update button
        """

        (update_button := QPushButton()).setIcon(QIcon(f"Assets/UpdateIcon{MODE.value.title()}.png"))
        update_button.setStyleSheet((Dark if MODE == ColorModes.DARK else Light).UpdateButton)
        
        update_button.clicked.connect(self.UpdateSameLocation)
        self.subcomponents.append(update_button)
        
        return update_button

    
    @pyqtSlot(ColorModes)
    def SwitchColorMode(self, mode : ColorModes):
        """Switches the Home tab's header color mode

        Args:
            mode (ColorModes): the current color mode, switching to the other
        """
        self.SetLightMode() if mode.value == "light"\
        else self.SetDarkMode()




    def SetLightMode(self):
        """Header light mode setter"""
        self._palette_.setColor(QPalette.ColorRole.Window, Colors.OffWhite)
        self.setPalette(self._palette_)

        
        for div in self.subcomponents[1:-1]:
            div.SetColor(ColorModes.LIGHT)

        self.subcomponents[-1].setStyleSheet(Light.UpdateButton)
        self.subcomponents[-1].setIcon(QIcon('Assets/UpdateIconLight.png'))

    
    
    def SetDarkMode(self):
        """Header dark mode setter"""
        self._palette_.setColor(QPalette.ColorRole.Window, Colors.CoolGrey)
        self.setPalette(self._palette_)
        
        for div in self.subcomponents[1:-1]:
            div.SetColor(ColorModes.DARK)

        self.subcomponents[-1].setStyleSheet(Dark.UpdateButton)
        self.subcomponents[-1].setIcon(QIcon('Assets/UpdateIconDark.png'))

    
    def UpdateLeadFont(self, font : str):
        """Called inside the settings"""


        for widget in self.subcomponents[1].widgets:
            widget.setFont(QFont(font, pointSize=20))


    
    def UpdateDataFont(self, font : str):
        """Called inside the settings"""

        for widget in self.subcomponents[2].widgets:
            widget.setFont(QFont(font, pointSize=15))


    @pyqtSlot()
    def UpdateSameLocation(self):
        """Emits the update_data signal which communicates with the worker thread to fetch new data for the same location"""       
        self.update_data.emit()


    @pyqtSlot(str)
    def FetchNewData(self, location : str):
        """Emits the fetch_new_data signal which communicates with the worker thread to fetch data for a new location

        Args:
            location (str): The new location. If == "current" (case insensitive) calls the user latitude and longitude using the geocoder library
        """
        self.fetch_new_data.emit({
            'api'           :       'bulk',
            'location'      :       location,
            'range'         :       3,
            'date'          :       None
            })






