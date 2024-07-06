"""Contains the controller for the header of the home tab"""
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from MyWeather.View.components.Home.Header.Header import Header
from MyWeather.Init import LOCATION, FONTS
from ..Model.constdata.icons import Icons
from ..Model import request as API, obj
import geocoder


def GetHeaderIcon(condition : str, is_day : bool) -> str:
    """skims through the dictionary mapping Condition : Icon and returns the icon URL`

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


def UpdateHeader(Header : Header) -> bool:
    """Updates the header on click of it's update button

    Args:
        Header (Header): The header instance to be updated

    Returns:
        bool: Success/Failure variable. TODO: On fail, implement some sort of visual message on the GUI
    """

    #get the location to query
    if LOCATION != "current":
        location = LOCATION
    
    else:
        
        try:
            location = f"{(user_location := geocoder.ip('me').latlng)[0]},{user_location[1]}"
        
        except TypeError:
            location = "Presov"

    #if the API query or the current location query (if current location set as default fails)
    if location is None or (data := API.RealtimeWeather(location)) is None:
        return False
    
    
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

    #return success value
    return True
    


    


    

    






