from matplotlib import pyplot
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget
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
        self.graph.graphs.setCurrentIndex(0)                                     #switch the day to the first of the data recieved

        #if the data is shorter than the current one, remove excessive graphs from the layout
        if (current_len := len(self.graph.layouts)) < (new_len := len(data.days)):
            for index in range(new_len - (new_len - current_len), new_len - current_len + 1):
                #free the resources taken up by the excessive graphs, then remove them
                for graph in self.graph.layouts[index].graphs:
                    pyplot.close(graph.figure)
                    self.graph.layouts[index].removeWidget(graph)
                    del(graph)

                #remove the graph from the frame and delete the widget containing it
                self.graph.graphs.removeWidget(self.graph.dummy_widgets[index])
                self.graph.dummy_widgets[index].deleteLater()
                self.graph.layouts.remove(self.graph.layouts[index])
                self.graph.dummy_widgets.remove(self.graph.dummy_widgets[index])


        for index, day in enumerate(data.days):
            #if the index exceeds the current length, add a new graph widget
            if index >= len(self.graph.layouts):
                (dummy := QWidget()).setLayout(graph := StackedGraphLayout(day, data.location, graph.color_mode))
                self.graph.graphs.addWidget(dummy)
                self.graph.layouts.append(graph)
                self.graph.dummy_widgets.append(dummy)

            

            self.graph.layouts[index].date = day.date_str           #set new date
            self.graph.layouts[index].location = data.location      #set new location

            for graph in self.graph.layouts[index].graphs:
                graph.Update(day)



    def FailureHandler(self):
        print("Fail :((")
