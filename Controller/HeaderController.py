"""Contains the controller for the header of the home tab"""
from ..View.components.Home.Header import Header
from ..Model.constdata.icons import Icons
from . import InitWeatherData



def GetHeader() -> Header:
    """initializes the header

    Returns:
        Header: The initialized Header object
    """ 

    return Header(current := InitWeatherData.current, 
                    GetHeaderIcon(current.condition, current.is_day))
    


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
    return 'View/Assets/ConditionIcons/day/sunny.png'






