#parser for the forecast API call return
from datetime import datetime
from dataclasses import dataclass, field
from statistics import mean

@dataclass
class WindData:
    points = {
        "East" : [0,360],
        "Northeast" : 45,
        "North" : 90,
        "Northwest" : 135,
        "West" : 180,
        "Southwest" : 225,
        "South" : 270,
        "Southeast" : 315
    }

    speed : float
    degrees : float            #instance variables
    direction : str = field(init=False)#calculated from degrees

    
    def GetDirection(self):
        min_distance = 360 #set intial distance to the biggest possible
        direction = "East"
        
        for point in self.points.keys():
            #first calculate the distance of the degrees from each direction point
            if point == "East" : #only one which has two possible coordinates
                current_distance = abs(self.points[point][0] - self.degrees) if self.degrees < 180 else abs(self.points[point][0] - self.degrees)
            else:
                current_distance = abs(self.points[point] - self.degrees)
            #check if a new minimum was found
            if current_distance < min_distance:
                min_distance = current_distance
                direction = point
        
        #return the closest point to the given degrees
        return direction
    
    #automatically initialize the direction to point to the correct world side
    def __post_init__(self):
        self.direction = self.GetDirection()



#represents the precipitation data
@dataclass
class RainData:
    precip_height : float
    rain_chance : float



#represents the temperature data
@dataclass
class TemperatureData:
    actual_temperature : float
    feelslike : float


#weather data for a given hour
@dataclass
class Hour:
    time : datetime
    humidity : float
    condition : str
    wind_data : WindData
    temperature_data : TemperatureData
    rain_data : RainData
    is_day : bool = field(init=False)
    time_str : str = field(init=False)
    location : str = field(init=False)

    #initialize the is_day variable, (night from 22 to 6)
    def __post_init__(self): 
        self.is_day = self.time.hour >= 22 or self.time.hour <= 6
        self.date_str = f"{self.time.day}.{self.time.month}.{self.time.year}"
        self.time_str = f"{self.date_str}, {self.time.hour}:{self.time.minute:02d}"



#class which bundles up all min/max/avg stats
@dataclass
class Stats:
    max_temp : float
    min_temp : float             
    avg_temp : float
    max_wind : float
    avg_humidity : float



#weather data for an entire day
@dataclass
class Day:
    date : datetime
    stats : Stats               #all MAX/MIN/AVG stats
    rain_data : RainData        #daily rain chance and total precipitation height in mm
    condition : str             #condition as text (such as for example "sunny", "raining", etc.)
    hours : list[Hour]          #individual hours
    date_str : str = field(init=False)
    location : str = field(init=False)

    def __post_init__(self):
        self.date_str = f"{self.date.day}.{self.date.month}.{self.date.year}"



#contains all data when realtime weather is requested
@dataclass
class Realtime:
    location : str
    date : datetime
    temperature : TemperatureData
    wind : WindData
    precip_height : float
    humidity : int
    condition : str
    is_day : bool = field(init=False)
    time_str : str = field(init=False)
    
    #initialize the is_day variable
    def __post_init__(self):
        self.is_day = 6 <= self.date.hour < 22 
        self.time_str = f"{self.date.day}.{self.date.month}.{self.date.year}, {self.date.hour}:{self.date.minute:02d}"



#contains all data for the entire history/forecast
@dataclass
class Timeline:
    location : str
    days : list[Day]
    stats : Stats = field(init=False)
    length : int = field(init=False)

    #initialize the history/forecast's statistics and the location variable for days/hours
    def __post_init__(self):
        stat_params = {
            "max_temp" : max(day.stats.max_temp for day in self.days),
            "min_temp" : min(day.stats.min_temp for day in self.days),
            "avg_temp" : mean(day.stats.avg_temp for day in self.days),
            "max_wind" : max(day.stats.max_wind for day in self.days),
            "avg_humidity" : mean(day.stats.avg_humidity for day in self.days)
        }
        self.stats = Stats(**stat_params)
        self.length = len(self.days)

        #add locations to the days/hours
        for day in self.days:
            day.location = self.location

            for hour in day.hours:
                hour.location = self.location




#contains both Timeline and Realtime objects, derived from the Timeline response
@dataclass
class BulkData:
    current : Realtime
    forecast : Timeline


