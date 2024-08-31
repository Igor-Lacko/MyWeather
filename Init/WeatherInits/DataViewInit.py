"""Contains constructors for the data view layout in the weather tab after the option menu vanishes and a successful response is gotten"""
from . import *
from MyWeather.View.components.DataViews.GraphView.Container import BaseGraphContainer
from MyWeather.Model import obj
from MyWeather.View.utils.enumerations import ColorModes
from MyWeather.View.components.Weather.WeatherWindow import WeatherTab
from MyWeather.Controller.WeatherTabController.Animations import SetWidgetInvisible


def GetView(data : obj.Realtime | obj.Day, view : str, api : str, tab : WeatherTab) -> QHBoxLayout:
    match api:
        case 'realtime':
            return GetRealtimeView(data, view, tab)

        case _:
            raise NotImplementedError("Not done yet!")



def GetRealtimeView(data : obj.Realtime | obj.Day, view : str, tab : WeatherTab) -> QHBoxLayout:
    
    layout = QHBoxLayout()
    match view:
        case "graph":
            layout.setContentsMargins(500,0,500,0)
            graph = BaseGraphContainer(data, tab.color_mode, 'realtime')
            layout.addWidget(graph)

            SetWidgetInvisible(graph)               #hide the graph until it's animation starts (handled by the controller)

            tab.graph = graph
            tab.view_layout = layout

        case "text":
            raise NotImplementedError("Text view not implemented yet!")

        case _:
            raise ValueError(f"View argument '{view}' not one of graph or text")

    return layout