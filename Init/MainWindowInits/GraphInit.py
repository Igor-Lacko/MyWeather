"""Initializes the graph with InitWeatherData"""
from ...View.components.Home.HomeWindow.Graph.FrameHeader import FrameHeader
from . import InitWeatherData

def GetGraphHeader() -> FrameHeader:
    """Initializes the frame header with the on-init weather data"""
    return FrameHeader(f"Forecast for {InitWeatherData.forecast.days[0].date_str}")