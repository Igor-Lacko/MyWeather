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


def GetTitle(data : obj.Realtime | obj.Timeline, api : str, date_str : str | None = None) -> str:
    """Returns a title depending on the data length, location, and type. Examples:
    - Realtime for NYC returns "Current weather in New York City, United States of America"
    - Forecast for Presov from 19.8.2024-21.8.2024 returns "Forecast from 19.8.2024 to 21.8.2024, Presov, Slovakia
    - Historic for Brno from 10.7.2024-17.7.2024 returns Historic data from 10.7.2024 to 17.7.2024, Brno, Czech Republic

    Args:
        data (obj.Realtime | obj.Timeline): The weather data (used for information liek date, location... etc.)
        api (str): API type because case is prettier than isinstance
        date_str (str): If only a single day is to be displayed

    Returns:
        str: The title text
    """

    match api:
        case 'realtime':
            return f"Current weather in {data.location}"

        case 'forecast':
            if date_str is None:
                return f"Forecast from {data.days[0].date_str} to {data.days[-1].date_str}, {data.location}"\
                if not len(data.days) == 1 else\
                f"Forecast for {data.location} on {data.days[0].date_str}"

            return f"Forecast for {data.location} on {date_str}"

        case 'history':
            if date_str is None:
                return f"Historic data from {data.days[0].date_str} to {data.days[-1].date_str}, {data.location}"\
                if not len(data.days) == 1 else\
                f"Historic data for {data.location} on {data.days[0].date_str}"

            return f"Historic data for {data.location} on {date_str}"

        case _:
            raise ValueError("Incorrect API argument")


def PrintLayout(layout : QLayout):
    """Just a informative function i used sometimes during the weather section development mostly to check widgets/their stretches in different stages"""
    for index in range(layout.count()):
        print(layout.itemAt(index), layout.stretch(index))


def ClearLayout(layout : QLayout):
    """Removes all items from a layout"""
    while layout.count():
            #remove the item
            item = layout.takeAt(0)

            #check if it's a spacer item (which doesn't have deleteLater built in)
            if type(item) != QSpacerItem:
                item.widget().deleteLater()

            else:
                del(item)