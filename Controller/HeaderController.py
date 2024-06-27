"""Contains the controller for the header of the home tab"""
from ..View.components.Home.Header import Header
from ..Model.constdata.icons import Icons
from ..Model.request import RealtimeWeather



def GetHeader() -> Header:
    """Gets an API response and initializes the header

    Returns:
        Header: The initialized Header object
    """ 

    if (data := RealtimeWeather("Presov")) is not None:
        return Header(data, GetHeaderIcon(data.condition, data.is_day))
    
    else:
        return None
    


def GetHeaderIcon(condition : str, is_day : bool) -> str:
    """skims through the dictionary mapping Condition : Icon and returns the icon URL`

    Args:
        condition (str): The weather condition
        is_day (bool): To choose the correct icon

    Returns:
        str: The icon URL
    """

    daynight = "day" if is_day else "night"

    for dict in Icons:
        if condition in dict['conditions']:
            return dict[daynight]


    #default icon, because mostly it actually is sunny in the summer :)
    return 'View/Assets/ConditionIcons/day/sunny.png'






