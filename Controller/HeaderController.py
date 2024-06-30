"""Contains the controller for the header of the home tab"""
from ..View.components.Home.Header import Header
from ..Model.constdata.icons import Icons


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






