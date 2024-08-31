"""Contains the controller for the header of the home tab"""
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from MyWeather.View.components.Home.Header.Header import Header
from MyWeather.Init import LOCATION
from Constdata.ConditionIcons import Icons
from MyWeather.Model import request as API, obj

class HeaderController(QObject):



    def __init__(self):
        super().__init__()


    def GetHeaderIcon(self, condition : str, is_day : bool) -> str:
        """skims through the dictionary mapping Condition : Icon and returns the icon URL

        Args:
            condition (str): The weather condition
            is_day (bool): To choose the correct icon

        Returns:
            str: The icon URL
        """

        daynight = "day" if is_day else "night"


        for map in Icons:
            if condition in map['conditions']:
                return map[daynight]


        #default icon, because mostly it actually is sunny in the summer :)
        return 'Assets/ConditionIcons/day/sunny.png'


    def UpdateHeader(self, data : obj.Realtime, Header : Header):
        """Called when the worker thread fetches data succesfully. Updates the header with new data

        Args:
            data (obj.Realtime): The provided weather data
        """


        #update the header icon
        Header.subcomponents[0].setPixmap(QPixmap(GetHeaderIcon(data.condition, data.is_day)).scaled(
                100,
                100,        
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
                ))
    

    
        #update each individual part of the header
        for component in Header.subcomponents[1:-1]:
            component.UpdateData(data)


    def FailureHandler(self):
        raise ConnectionRefusedError("Header update not possible")


    def ConnectHeader(self, Header):
        self.header = Header





def GetHeaderIcon(condition : str, is_day : bool) -> str:
        """skims through the dictionary mapping Condition : Icon and returns the icon URL

        Args:
            condition (str): The weather condition
            is_day (bool): To choose the correct icon

        Returns:
            str: The icon URL
        """
        daynight = "day" if is_day else "night"


        for map in Icons:
            if condition.lower() in map['conditions']:          #sometimes the API results differed in lower or upper case
                return map[daynight]

