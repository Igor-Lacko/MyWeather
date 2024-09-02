from PyQt6.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from MyWeather.Model import obj
from MyWeather.View.components.Graphs.Container import ExtendedGraphContainer
from MyWeather.View.components.Graphs.StackedGraphLayout import StackedGraphLayout

class GraphController(QObject):
    """Updates the graph"""

    def __init__(self):
        super().__init__()




    def ConnectGraph(self, graph : ExtendedGraphContainer):
        """Connect the controller to the graph"""
        self.graph = graph



    def UpdateGraph(self, data : obj.Timeline):
        """Updates the graph with data provided by the worker thread"""
        self.graph.data = data
        self.graph.index = 0  
        self.graph.header.ChangeTitle(data.days[0].date_str, data.location)  #title for the first day
        self.graph.graphs.setCurrentIndex(0)                                             #switch the day to the first of the data recieved

        for index, day in enumerate(data.days):
            self.graph.layouts[index].date = day.date_str           #set new date
            self.graph.layouts[index].location = data.location      #set new location

            for graph in self.graph.layouts[index].graphs:
                graph.Update(day)



    def FailureHandler(self):
        print("Fail :((")
