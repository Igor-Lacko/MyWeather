"""Includes the main graph widget"""
from . import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot

class WeatherGraph(FigureCanvasQTAgg):
    """Includes the weather graph"""
    def __init__(self):
        

        temperatures = []
        for hour in InitWeatherData.forecast.days[0].hours:
            temperatures.append(hour.temperature_data.actual_temperature)

        

        pyplot.style.use(GRAPH_MODE)
        figure, axes = pyplot.subplots()
        super().__init__(figure)
        figure.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.15)
        axes.set_xlabel('Time', fontsize=14)
        axes.set_title('Temperature', fontsize=20)

        axes.plot(range(24), temperatures)

        pyplot.xticks(range(24))
        pyplot.locator_params('y',10)

        


        

    

