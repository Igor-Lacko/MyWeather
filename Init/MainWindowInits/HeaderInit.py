"""Initializes the Home tab header"""
from MyWeather.View.components.Home.Header import Header
from MyWeather.Controller.HeaderController import GetHeaderIcon
from . import InitWeatherData


def GetHeader() -> Header:
    """initializes the header

    Returns:
        Header: The initialized Header object
    """ 

    return Header(current := InitWeatherData.current, 
                    GetHeaderIcon(current.condition, current.is_day))