"""Includes the layout containing the three graphs"""
from . import *
from PyQt6.QtCore import pyqtSlot
from .GraphBody import TemperatureGraph, WindGraph, RainGraph
from MyWeather.Model.obj import Day

class GraphLayout(QStackedLayout):
    """Includes the three graphs for Temperature/Wind/Rain"""
    

    def __init__(self, dailydata : Day, location : str):
        """Graph layout constructor for one of the days in the forecast

        Args:
            dailydata (Day): Data for the day provided
            location (str): The location where the data actually is from
        """
        
        super().__init__()
        
        self.date = dailydata.date_str
        self.location = location
        self.index = 0                                  #initial index

        #temperature graph data
        actual = [hour.temperature_data.actual_temperature for hour in dailydata.hours]
        feelslike = [hour.temperature_data.feelslike for hour in dailydata.hours]

        #wind graph data
        wind_speed = [hour.wind_data.speed for hour in dailydata.hours]

        #rain graph data
        chance_of_rain = [hour.rain_data.rain_chance for hour in dailydata.hours]
        humidity = [hour.humidity for hour in dailydata.hours]


        #initialize the graphs list
        self.graphs = [TemperatureGraph(actual, feelslike), RainGraph(chance_of_rain, humidity), WindGraph(wind_speed)]


        for graph in self.graphs:               #add them to the actual graph layout
            self.addWidget(graph)



    @pyqtSlot(int)
    def SwitchGraph(self, new : int):
        """Switches the displayed graph

        Args:
            new (int): Index of the graph to be set 
        """

        self.setCurrentIndex(new)

    
    def SwitchColorMode(self, mode : ColorModes):
        """Passes the color mode switch to all of it's graphs

        Args:
            mode (ColorModes): The Color Mode to be switched on to
        """

        for graph in self.graphs:
            graph.SwitchColorMode(mode)