"""Initializes the graph with InitWeatherData"""
from ...View.components.DataViews.GraphView.Container import ExtendedGraphContainer
from . import InitWeatherData
from MyWeather.Constdata.Mode import MODE

def InitGraph() -> ExtendedGraphContainer:
    """Initial home window graph constructor

    Returns:
        ExtendedGraphContainer: ExtendedGraphContainer object with InitWeatherData
    """


    return ExtendedGraphContainer(InitWeatherData.forecast, MODE, 'forecast')
