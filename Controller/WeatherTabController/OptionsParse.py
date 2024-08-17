"""Includes a function that parses the option menu with the API type as an argument and returns a dictionary with options based on that"""
from . import *


def GetOptions(api : str, menu : OptionMenu) -> dict:
    """Returns a dictionary with keys and their options to be sent to the model

    Args:
        api (str): The API/data type
        menu (OptionMenu): The option menu where the needed values were set

    Returns:
        dict: dictionary with keys : values
    """

    match api:
        case 'realtime':    #the simplest option, only needs a location and viewType
            options = {
                'api'       :   'realtime',
                'location'  :   None,
                'view'      :   None
            }

            for item in menu.items:
                if item.key == 'location':
                    options['location'] = item.value

                if item.key == 'view':
                    options['view'] = item.value

            return options

        case _:
            print('fr fr')

