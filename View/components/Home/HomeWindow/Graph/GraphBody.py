"""Includes the main graph widget's class"""
from View.components.Home.HomeWindow.Graph import ColorModes
from . import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot


class WeatherGraph(FigureCanvasQTAgg):
    """Includes the weather graph"""
    def __init__(self):
        


        

        pyplot.style.use(GRAPH_MODE)
        
        self.figure, self.axes = pyplot.subplots()
        super().__init__(self.figure)
        
        self.figure.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
        
        self.axes.set_xlabel('Time', fontsize=14, loc='right')
        
        self.axes.spines['top'].set_visible(False)


        self.axes.set_xticks(range(24))

    def switch_color_mode(self, mode : ColorModes):
        self.SetDarkMode() if mode == ColorModes.DARK else self.SetLightMode()

        #winf graph doesn't have an legend, it only has one line so far
        if type(self) != WindGraph:
            self.axes.legend(loc='best',
                            framealpha=1, facecolor='black' if mode == ColorModes.DARK else 'white',
                            labelcolor='white' if mode == ColorModes.DARK else 'black'
                            )


    
    
    def SetDarkMode(self):
        """Dark mode setter"""


        self.figure.set_facecolor('black')
        self.axes.set_facecolor('black')
        
        self.axes.xaxis.label.set_color('white')
        self.axes.yaxis.label.set_color('white')
        
        [label.set_color('white') for label in self.axes.xaxis.get_ticklabels()]
        [label.set_color('white') for label in self.axes.yaxis.get_ticklabels()]
    
    
    
    def SetLightMode(self):
        """Light mode setter"""


        self.figure.set_facecolor('white')
        self.axes.set_facecolor('white')

        self.axes.xaxis.label.set_color('black')
        self.axes.yaxis.label.set_color('black')
        

        [label.set_color('black') for label in self.axes.xaxis.get_ticklabels()]
        [label.set_color('black') for label in self.axes.yaxis.get_ticklabels()]





class TemperatureGraph(WeatherGraph):
    """Contains the graph for actual and feelslike temperature"""
    
    def __init__(self, actual : list[float], feelslike : list[float]):
        """Temperature graph constructor

        Args:
            actual (list[float]): List of the actual temperatures for every hour    
            feelslike (list[float]): List of the temperatures that it feels like at every hour
        """

        super().__init__()
        self.axes.set_title('Temperature')
        self.axes.set_ylabel('°C', rotation=0, loc='top')

        self.axes.plot(actual, label="Actual temperature")
        self.axes.plot(feelslike, label="Feels like")

        self.axes.legend(loc='best', framealpha=1, facecolor='black' if MODE == ColorModes.DARK else 'white')

    
    def switch_color_mode(self, mode: ColorModes):
        """Color mode switcher for graph"""
        super().switch_color_mode(mode)
        self.axes.set_title('Temperature', color='white' if mode == ColorModes.DARK else 'black')
        

class WindGraph(WeatherGraph):
    """Contains the graph with wind speed"""

    def __init__(self, speed : list[float]):
        """Wind graph constructor

        Args:
            speed (list[float]): List of wind speed for a given hour
        """

        super().__init__()

        self.axes.set_title('Wind speed')
        self.axes.set_ylabel('km/h')

        self.axes.plot(speed, label="Wind speed in km/h")


    def switch_color_mode(self, mode: ColorModes):
        """Color mode switcher for graph"""
        super().switch_color_mode(mode)
        self.axes.set_title('Wind speed', color='white' if mode == ColorModes.DARK else 'black')
        


class RainGraph(WeatherGraph):
    """Contains the graph with precipitation height, humidity, and chance of rain"""

    def __init__(self, humidity : list[int], chance_of_rain : list[int]):
        """Rain graph constructor

        Args:
            humidity (list[int]): List of humidity percentages for each hour
            chance_of_rain (list[int]): List of chance of rain as a percentage at a given hour
        """
        super().__init__()

        self.axes.set_title('Rain/humidity')
        self.axes.set_ylabel('%', rotation=0, loc='top')

        self.axes.plot(humidity, label="Humidity percentage")
        self.axes.plot(chance_of_rain, label="Chance of rain in %")

        self.axes.legend(loc='best', framealpha=1, facecolor='black' if MODE == ColorModes.DARK else 'white')

    
    def switch_color_mode(self, mode: ColorModes):
        """Color mode switcher for graph"""
        super().switch_color_mode(mode)
        self.axes.set_title('Rain/humidity', color='white' if mode == ColorModes.DARK else 'black')



        


    

        


        

    

