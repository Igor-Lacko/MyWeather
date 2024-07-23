"""Includes the main graph widget's class"""
from . import *
from View.components.Home.HomeWindow.Graph import ColorModes
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib import pyplot
from MyWeather.Model import obj


class WeatherGraph(FigureCanvasQTAgg):
    """Includes the weather graph"""
    def __init__(self):

        self.color_mode = MODE                          #tecka vybaveno
        pyplot.style.use(GRAPH_MODE)
        
        self.figure, self.axes = pyplot.subplots()
        super().__init__(self.figure)
        
        self.figure.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
        
        self.axes.set_xlabel('Time', fontsize=14, loc='right')
        
        self.axes.spines['top'].set_visible(False)


        self.axes.set_xticks(range(24))

    def SwitchColorMode(self, mode : ColorModes, change : bool = True):
        self.SetDarkMode() if mode == ColorModes.DARK else self.SetLightMode()

        #winf graph doesn't have an legend, it only has one line so far
        if type(self) != WindGraph:
            self.axes.legend(loc='best',
                            framealpha=1, facecolor='black' if mode == ColorModes.DARK else 'white',
                            labelcolor='white' if mode == ColorModes.DARK else 'black'
                            )
        
        if change:
            self.color_mode = ColorModes.DARK if self.color_mode != ColorModes.DARK else ColorModes.LIGHT

    def Update(self):
        """Implemented by the subclasses, updates the graph based on the data provided and it's type (e.g Temperature/Wind or Rain)"""
        self.figure.clear()
        self.axes = self.figure.add_subplot()
        self.axes.set_xlabel('Time', fontsize=14, loc='right')
        
        self.axes.spines['top'].set_visible(False)


        self.axes.set_xticks(range(24))



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

        self.axes.legend(loc='best', framealpha=1)

        self.SwitchColorMode(MODE, change=False)

    
    def SwitchColorMode(self, mode: ColorModes, change : bool = True):
        """Color mode switcher for graph"""
        super().SwitchColorMode(mode, change)
        self.axes.set_title('Temperature', color='white' if mode == ColorModes.DARK else 'black')


    def Update(self, day : obj.Day):
        """Temperature version override of the Weather Graph's data"""
        super().Update()
        self.axes.set_title('Temperature')
        self.axes.set_ylabel('°C', rotation=0, loc='top')

        self.axes.plot([hour.temperature_data.actual_temperature for hour in day.hours], label="Actual temperature")
        self.axes.plot([hour.temperature_data.feelslike for hour in day.hours], label="Feels like")

        self.SwitchColorMode(self.color_mode, change=False)

        self.draw()












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

        self.SwitchColorMode(MODE, change=False)


    def SwitchColorMode(self, mode: ColorModes, change : bool = True):
        """Color mode switcher for graph"""
        super().SwitchColorMode(mode, change)
        self.axes.set_title('Wind speed', color='white' if mode == ColorModes.DARK else 'black')


    def Update(self, day : obj.Day):
        """Wind data version of override of Weather Graph's Update()"""
        super().Update()
        self.axes.set_title('Wind speed')
        self.axes.set_ylabel('km/h', rotation=0, loc='top')

        self.axes.plot([hour.wind_data.speed for hour in day.hours], label="Wind speed in km/h")
        self.SwitchColorMode(self.color_mode, change=False)

        self.draw()





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

        self.axes.legend(loc='best', framealpha=1)

        self.SwitchColorMode(MODE, change=False)

    
    def SwitchColorMode(self, mode : ColorModes, change : bool = True):
        """Color mode switcher for graph"""
        super().SwitchColorMode(mode, change)
        self.axes.set_title('Rain/humidity', color='white' if mode == ColorModes.DARK else 'black')


    def Update(self, day : obj.Day):
        """Rain and humidity version of the override of WeatherGraph's Update()"""
        super().Update()
        self.axes.set_title('Rain/humidity')
        self.axes.set_ylabel('%', rotation=0, loc='top')

        self.axes.plot([hour.humidity for hour in day.hours], label="Humidity percentage")
        self.axes.plot([hour.rain_data.rain_chance for hour in day.hours], label = "Chance of rain in %")

        self.axes.legend(loc='best', framealpha=1)
        self.SwitchColorMode(self.color_mode, change=False)

        self.draw()





