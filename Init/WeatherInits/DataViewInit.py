"""Contains constructors for the data view layout in the weather tab after the option menu vanishes and a successful response is gotten"""
from . import *
from MyWeather.View.components.DataViews.GraphView.Container import BaseGraphContainer
from MyWeather.Model import obj
from MyWeather.View.utils.enumerations import ColorModes


def GetView(data : obj.Realtime | obj.Day, view : str, api : str, mode : ColorModes) -> QHBoxLayout:
    match api:
        case 'realtime':
            return GetRealtimeView(data, view, mode)

        case _:
            raise NotImplementedError("Not done yet!")



def GetRealtimeView(data : obj.Realtime | obj.Day, view : str, mode : ColorModes) -> QHBoxLayout:
    
    layout = QHBoxLayout()
    match view:
        case "graph":
            layout.setContentsMargins(50,0,50,0)
            graph = BaseGraphContainer(data, mode, 'realtime')
            layout.addWidget(graph)

        case "text":
            raise NotImplementedError("Text view not implemented yet!")

        case _:
            raise ValueError(f"View argument '{view}' not one of graph or text")

    return layout