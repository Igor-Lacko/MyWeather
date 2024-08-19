"""Several functions that remove some boilerplate code around the Weather Tab controller"""
from . import *
from MyWeather.Init.WeatherInits.ItemLayout import api_options
from MyWeather.Init.WeatherInits.ItemsInit import ParseItems
from MyWeather.Model import obj

def GetSelectionLayout(tab : WeatherTab):
    """Returns a initialized layout with the selection buttons"""
    layout = QHBoxLayout()
    ParseItems(api_options['items'], layout, tab)
    tab.selection_layout = layout
    return layout


def ClearEffect(widgets : list[QWidget]):
    """Deletes the widget's effect"""
    for widget in widgets:
        widget.graphicsEffect().deleteLater()
        widget.setGraphicsEffect(None)


def GetTitle(data : obj.Realtime | obj.Timeline, api : str) -> str:
    """Returns a title depending on the data length, location, and type. Examples:
    - Realtime for NYC returns "Current weather in New York City, United States of America"
    - Forecast for Presov from 19.8.2024-21.8.2024 returns "Forecast from 19.8.2024 to 21.8.2024, Presov, Slovakia
    - Historic for Brno from 10.7.2024-17.7.2024 returns Historic data from 10.7.2024 to 17.7.2024, Brno, Czech Republic

    Args:
        data (obj.Realtime | obj.Timeline): The weather data (used for information liek date, location... etc.)
        api (str): API type because case is prettier than isinstance 

    Returns:
        str: The title text
    """

    match api:
        case 'realtime':
            return f"Current weather in {data.location}"

        case 'forecast':
            return f"Forecast from {data.days[0].date_str} to {data.days[-1].date_str}, {data.location}"

        case 'history':
            return f"Historic data from {data.days[0].date_str} to {data.days[-1].date_str}, {data.location}"

        case _:
            raise ValueError("Incorrect API argument")
