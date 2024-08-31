"""Contains constructors for the data view layout in the weather tab after the option menu vanishes and a successful response is gotten"""
from . import *
from MyWeather.View.components.DataViews.GraphView.Container import BaseGraphContainer
from MyWeather.View.components.DataViews.GraphPicker import GraphPicker
from MyWeather.Model import obj
from MyWeather.View.components.Weather.WeatherWindow import WeatherTab
from MyWeather.Controller.WeatherTabController.Animations import SetWidgetInvisible


def GetView(data : obj.Realtime | obj.Day, view : str, api : str, tab : WeatherTab) -> QHBoxLayout:
    """Returns a view layout based on the api and view type"""
    match api:
        case 'realtime':
            return GetRealtimeView(data, view, tab)

        case 'forecast':
            return GetForecastView(data, view, tab)

        case _:
            raise NotImplementedError("Not done yet!")



def GetSingleGraph(data : obj.Day, api : str, tab : WeatherTab) -> QHBoxLayout:
    """Gets a single graph view

    Args:
        data (obj.Day): The data to initialize the graph with
        api (str): The API type to pass to the header
        tab (WeatherTab): The tab instance to add the graph to

    Returns:
        QHBoxLayout: Initialized layout containing the graph and some spacer items
    """

    (layout := QHBoxLayout()).setContentsMargins(500,0,500,0)
    layout.addWidget(graph := BaseGraphContainer(data, tab.color_mode, api))

    SetWidgetInvisible(graph)                           #hide the graph until it's animation starts (handled by the controller)

    tab.graph = graph 
    tab.view_layout = layout

    return layout



def GetRealtimeView(data : obj.Realtime | obj.Day, view : str, tab : WeatherTab) -> QHBoxLayout:
    match view:
        case "graph":
            return GetSingleGraph(data, 'realtime', tab)

        case "text":
            raise NotImplementedError("Text view not implemented yet!")

        case _:
            raise ValueError(f"View argument '{view}' not one of graph or text")



def GetForecastView(data : obj.Timeline, view : str, tab : WeatherTab) -> QHBoxLayout:
    if len(data.days) == 1:
        match view:
            case "graph":
                return GetSingleGraph(data, 'forecast', tab)

            case "text":
                raise NotImplementedError("Text view not implemented yet!")

            case _:
                raise ValueError(f"View argument '{view}' not one of graph or text")

    (layout := QHBoxLayout()).setContentsMargins(0,0,0,0)
    layout.setSpacing(0)

    layout.addStretch(20)

    for day in data.days:
        layout.addWidget(picker := GraphPicker(day, tab.color_mode), stretch=40)
        layout.addStretch(20)

        tab.tabs.append(picker)

    tab.view_layout = layout
    return layout
