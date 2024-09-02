"""Includes the graph superclass and all it's subclasses"""
from . import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib import pyplot, use
from MyWeather.View.utils.enumerations import ColorModes #absolute import to avoid enum comparision issues

use("QtAgg")

class AbstractGraph(FigureCanvasQTAgg):
    """Graph superclass, implements common aspects for all graphs"""
    def __init__(self):
        """Graph superclass constructor"""

        #initial color mode and matplotlib's theme
        self.color_mode = MODE
        pyplot.style.use(GRAPH_MODE)

        #initialize the figure/axes
        self.figure, self.axes = pyplot.subplots()
        super().__init__(self.figure)

        #adjust some visual stuff
        self.figure.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)
        self.axes.spines['top'].set_visible(False)

        #set the x-axis label and it's length
        self.axes.set_xlabel("Hours", fontsize=14, loc='right')
        self.axes.set_xticks(range(24))



    def Update(self):
        """Updates the graph based on new data, implemented by the subclasses\n
        - Used only by the Home Window graph (other graphs are constant)"""
        self.figure.clear()
        self.axes = self.figure.add_subplot()

        #restore the original x-label and visual stuff
        self.axes.spines['top'].set_visible(False)
        self.axes.set_xlabel("Hours", fontsize=14, loc='right')
        self.axes.set_xticks(range(24))



    def SetDarkMode(self):
        """Dark mode setter"""
        #background color
        self.figure.set_facecolor('black')
        self.axes.set_facecolor('black')

        #text colors
        self.axes.xaxis.label.set_color('white')
        self.axes.yaxis.label.set_color('white')
        [label.set_color('white') for label in self.axes.xaxis.get_ticklabels()]
        [label.set_color('white') for label in self.axes.yaxis.get_ticklabels()]



    def SetLightMode(self):
        """Light mode setter"""
        #background color
        self.figure.set_facecolor('white')
        self.axes.set_facecolor('white')

        #text colors
        self.axes.xaxis.label.set_color('black')
        self.axes.yaxis.label.set_color('black')
        [label.set_color('black') for label in self.axes.xaxis.get_ticklabels()]
        [label.set_color('black') for label in self.axes.yaxis.get_ticklabels()]



    def SetColorMode(self, mode : ColorModes, change : bool=True):
        """Sets the graph's color scheme. Used on color mode switches or when redrawing the graph itself

        Args:
            mode (ColorModes): The color scheme to be set (dark or light)
            change (bool, optional): If the graph's color_mode attribute should be switched. Defaults to True since color mode switches are probably more frequent
        """
        self.SetDarkMode() if mode == ColorModes.DARK else self.SetLightMode()
        if change:
            self.color_mode = ColorModes.DARK if self.color_mode != ColorModes.DARK else ColorModes.LIGHT




class TemperatureGraph(AbstractGraph):
    """Abstract graph subclass containing temperature data"""

    def __init__(self, actual : list[float], feelslike : list[float]):
        """Temperature graph constructor

        Args:
            actual (list[float]): List of actual temperatures throughout the dat
            feelslike (list[float]): List of feelslike temperatures troughout the day
        """

        super().__init__()

        self.axes.set_title('Temperature')
        self.axes.set_ylabel('°C', rotation=0, loc='top')

        self.axes.plot(actual, label="Actual temperature")
        self.axes.plot(feelslike, label="Feels like")
        self.axes.legend(loc='best', framealpha=1)

        self.SetColorMode(self.color_mode, change=False)



    def SetColorMode(self, mode: ColorModes, change: bool = True):
        """Color mode setter for the temperature graph"""
        super().SetColorMode(mode, change)
        self.axes.set_title('Temperature', color='white' if mode == ColorModes.DARK else 'black')
        self.axes.legend(loc='best',
                            framealpha=1, facecolor='black' if mode == ColorModes.DARK else 'white',
                            labelcolor='white' if mode == ColorModes.DARK else 'black'
                            )


    def Update(self, data : Day):
        """Temperature graph updater, sets the new data to the y-axis

        Args:
            data (obj.Day): The weather data to extract from
        """
        super().Update()
        self.axes.set_title('Temperature')
        self.axes.set_ylabel('°C', rotation=0, loc='top')

        #data plot
        self.axes.plot([hour.temperature_data.actual_temperature for hour in data.hours], label="Actual temperature")
        self.axes.plot([hour.temperature_data.feelslike for hour in data.hours], label="Feels like")

        #reset the visual settings and redraw the figure
        self.SetColorMode(self.color_mode, change=False)
        self.draw()





class WindSpeedGraph(AbstractGraph):
    """AbstractGraph subclass containing wind speed"""

    def __init__(self, speed : list[float]):
        """Wind graph constructor

        Args:
            speed (list[float]): List of wind speeds for each hour for the given day
        """

        super().__init__()

        #set titles and plot data
        self.axes.set_title('Wind speed')
        self.axes.set_ylabel('km/h', rotation=0, loc='top', fontsize=14)
        self.axes.plot(speed, label="Wind speed in km/h")

        #initial color scheme
        self.SetColorMode(self.color_mode, change=False)



    def SetColorMode(self, mode: ColorModes, change: bool = True):
        """Color mode setter for wind graph, almost the same + title as the base class"""
        super().SetColorMode(mode, change)
        self.axes.set_title('Wind speed', color='white' if mode == ColorModes.DARK else 'black')



    def Update(self, data : Day):
        """Updates the wind speed graph based on the provided data

        Args:
            data (Day): Daily wind speed data
        """

        super().Update()

        #update the titles and plot new data
        self.axes.set_title('Wind speed')
        self.axes.set_ylabel('km/h', rotation=0, loc='top', fontsize=14)
        self.axes.plot([hour.wind_data.speed for hour in data.hours], label="Wind speed in km/h")

        #redraw the graph
        self.SetColorMode(self.color_mode, change=False)
        self.draw()



class RainGraph(AbstractGraph):
    """AbstractGraph subclass containing humidity and chance of rain"""

    def __init__(self, humidity : list[int], chance_of_rain : list[int]):
        """Water data graph constructor

        Args:
            humidity (list[int]): List of humidity percentages for a given day
            chance_of_rain (list[int]): List of rain chances for a given day
        """

        super().__init__()

        #titles and plotting
        self.axes.set_title("Rain/humidity")
        self.axes.set_ylabel('%', rotation=0, loc='top')
        self.axes.plot(humidity, label="Humidity percentage")
        self.axes.plot(chance_of_rain, label="Chance of rain in %")

        #set legend/visual settings
        self.axes.legend(loc='best', framealpha=1)
        self.SetColorMode(self.color_mode, change=False)



    def SetColorMode(self, mode: ColorModes, change: bool = True):
        """Color scheme setter for the rain graph"""
        super().SetColorMode(mode, change)
        self.axes.legend(loc='best',
                            framealpha=1, facecolor='black' if mode == ColorModes.DARK else 'white',
                            labelcolor='white' if mode == ColorModes.DARK else 'black'
                            )
        self.axes.set_title('Rain/humidity', color='white' if mode == ColorModes.DARK else 'black')



    def Update(self, data : Day):
        """Updater for the RainGraph version"""
        super().Update()

        #titles and plot
        self.axes.set_title('Rain/humidity')
        self.axes.set_ylabel('%', rotation=0, loc='top')
        self.axes.plot([hour.humidity for hour in data.hours], label="Humidity percentage")
        self.axes.plot([hour.rain_data.rain_chance for hour in data.hours], label = "Chance of rain in %")

        #redraw the graph
        self.axes.legend(loc='best', framealpha=1)
        self.SetColorMode(self.color_mode, change=False)
        self.draw()



class PrecipitationGraph(AbstractGraph):
    """Abstract graph subclass containing data for the precipitation height"""

    def __init__(self, heights : list[float]):
        """Precipitation graph constructor

        Args:
            height (list[float]): List of the water heights for each hour for a given day
        """

        super().__init__()

        #titles and plot
        self.axes.set_title("Precipitation height")
        self.axes.set_ylabel("mm", rotation=0, loc='top', fontsize=14)
        self.axes.plot(heights, label="Precipitation in mm")

        #set visual settings
        self.SetColorMode(self.color_mode, change=False)



    def SetColorMode(self, mode: ColorModes, change: bool = True):
        """Color scheme setter for the precipitation graph"""
        super().SetColorMode(mode, change)
        self.axes.set_title('Precipitation height', color='white' if mode == ColorModes.DARK else 'black')



    def Update(self, data : Day):
        """Precipitation graph updater"""
        super().Update()

        #titles and plot
        self.axes.set_title("Precipitation height")
        self.axes.set_ylabel("mm", rotation=0, loc='top', fontsize=14)
        self.axes.plot([hour.rain_data.precip_height for hour in data.hours])

        #redraw the graph
        self.SetColorMode(self.color_mode, change=False)
        self.draw()