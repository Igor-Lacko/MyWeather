from PyQt6.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from MyWeather.Model import obj
from MyWeather.View.components.Home.HomeWindow.Graph.GraphFrame import GraphFrame
from MyWeather.View.components.Home.HomeWindow.Graph.GraphLayout import GraphLayout

class GraphController(QObject):
    """Updates the graph"""

    def __init__(self):
        super().__init__()




    def ConnectGraph(self, graph : GraphFrame):
        """Connect the controller to the graph"""
        self.graph = graph



    def UpdateGraph(self, data : obj.Forecast):
        """Updates the graph with data provided by the worker thread"""            
        self.graph.header.widgets[1].ChangeTitle(data.days[0].date_str, data.location)  #title for the first day
        self.graph.graph.setCurrentIndex(0)                                             #switch the day to the first of the data recieved

        for index, day in enumerate(data.days):
            self.graph.daylist[index].date = day.date_str           #set new date
            self.graph.daylist[index].location = data.location      #set new location

            self.UpdateGraphData(day, self.graph.daylist[index])    #update variables for the GraphLayout which contains the entire day

            for graph in self.graph.daylist[index].graphs:
                graph.Update(day)



    def FailureHandler(self):
        print("Fail :((")


    def UpdateGraphData(self, dailydata : obj.Day, graph : GraphLayout):
        """Updates the graph's variables containing actual weather data"""
        
        #temperature graph data
        graph.actual = [hour.temperature_data.actual_temperature for hour in dailydata.hours]
        graph.feelslike = [hour.temperature_data.feelslike for hour in dailydata.hours]

        #wind graph data
        graph.wind_speed = [hour.wind_data.speed for hour in dailydata.hours]

        #rain graph data
        graph.chance_of_rain = [hour.rain_data.rain_chance for hour in dailydata.hours]
        graph.humidity = [hour.humidity for hour in dailydata.hours]