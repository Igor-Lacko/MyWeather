"""Includes a function that parses the option menu with the API type as an argument and returns a dictionary with options based on that"""
from . import *
from datetime import datetime


def GetOptions(api : str, menu : OptionMenu) -> dict:
    """Returns a dictionary with keys and their options to be sent to the model

    Args:
        api (str): The API/data type
        menu (OptionMenu): The option menu where the needed values were set

    Returns:
        dict: dictionary with keys : values
    """

    match api:
        case 'realtime':    #the simplest option, only needs a location
            options = {
                'api'       :   api,
                'location'  :   None,
            }

            for item in menu.items:
                if item.key == 'location':
                    options['location'] = item.value

            return options

        case 'forecast' | 'history':        #needs a length/date pick in addition
            options = {
                'api'           :   api,
                'location'      :   None,
                'range'         :   None,
                'date'          :   None
            }

            for item in menu.items:
                if item.key == 'location':
                    options['location'] = item.value

                if item.key == 'range':
                    options['range'] = item.value

                if item.key == 'date':
                    options['date'] = item.value if item.value == 'None' else ParseDate(item.value)

            return options

        case _:                             #invalid argument
            raise ValueError("Invalid API argument")



def ParseDate(date : str) -> str:
    """Converts a date from Weekday, DD.MM.YYYY to YYYY-MM-DD

    Args:
        date (str): the old date format

    Returns:
        str: the converted date
    """

    return datetime.strptime(date, '%A, %d.%m.%Y').strftime('%Y-%m-%d')

