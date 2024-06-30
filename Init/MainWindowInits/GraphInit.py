"""Initializes the graph with InitWeatherData"""
from ...View.components.Home.HomeWindow.Graph import FrameHeader
from . import InitWeatherData

def GetGraphHeader() -> FrameHeader.FrameHeader:
    """Initializes the frame header with the on-init weather data"""
    if len(InitWeatherData.forecast.days) != 1:
        date_beginning = InitWeatherData.forecast.days[0].date_str
        date_end = InitWeatherData.forecast.days[-1].date_str
        return FrameHeader.FrameHeader(f"The forecast from {date_beginning} to {date_end}")
    

    day = InitWeatherData.forecast.days[0]
    return FrameHeader.FrameHeader(f"The forecast for {day.date.day}.{day.date.month}.{day.date.year}")