"""Module containing the stacked layout which contains multiple graph objects"""
from . import *
from PyQt6.QtCore import pyqtSlot
from .Body import *


class StackedGraphLayout(QStackedLayout):
    """Graph stacked layout class, switched between with the parent widget's menu's combobox"""

    def __init__(self, data : Day, location : str):
        """Graph layout constructor, used for one day

        Args:
            data (Day): The weather data used to plot on the graphs
            location (str): The location where the data is for
        """
        super().__init__()

        self.location = location
        self.index = 0      #stacked layout index

        #initialize the individual graphs
        self.temperature_graph = TemperatureGraph([hour.temperature_data.actual_temperature for hour in data.hours],
        [hour.temperature_data.feelslike for hour in data.hours])
        self.wind_graph = WindSpeedGraph([hour.wind_data.speed for hour in data.hours])
        self.rain_graph = RainGraph([hour.humidity for hour in data.hours], 
        [hour.rain_data.rain_chance for hour in data.hours])
        self.precip_graph = PrecipitationGraph([hour.rain_data.precip_height for hour in data.hours])

        self.graphs = [self.temperature_graph, self.wind_graph, self.rain_graph, self.precip_graph]

        #add them to the layout
        for graph in self.graphs:
            self.addWidget(graph)



    @pyqtSlot(int)
    def SwitchGraph(self, new : int):
        """Switches the displayed graph, the signal is sent by the graph header's combo box"""
        self.setCurrentIndex(new)



    def SwitchColorMode(self, mode : ColorModes):
        """Switches the color mode for all graphs, signal sent by the light/dark mode button on the sidebar

        Args:
            mode (ColorModes): The color mode to be set to
        """
        for graph in self.graphs:
            graph.SetColorMode(mode)