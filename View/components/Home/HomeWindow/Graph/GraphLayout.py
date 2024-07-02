"""Includes the layout containing the three graphs"""
from . import *
from PyQt6.QtCore import pyqtSlot
from .GraphBody import TemperatureGraph, WindGraph, RainGraph

class GraphLayout(QStackedLayout):
    """Includes the three graphs for Temperature/Wind/Rain"""
    
    graph_dict = {
        "Temperature"   :   0,
        "Rain"  :   1,
        "Wind"  :   2
    }

    def __init__(self):
        super().__init__()
        
        self.index = 0                                  #initial index

        #temperature graph data
        actual = [hour.temperature_data.actual_temperature for hour in InitWeatherData.forecast.days[0].hours]
        feelslike = [hour.temperature_data.feelslike for hour in InitWeatherData.forecast.days[0].hours]

        #wind graph data
        wind_speed = [hour.wind_data.speed for hour in InitWeatherData.forecast.days[0].hours]

        #rain graph data
        chance_of_rain = [hour.rain_data.rain_chance for hour in InitWeatherData.forecast.days[0].hours]
        humidity = [hour.humidity for hour in InitWeatherData.forecast.days[0].hours]


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