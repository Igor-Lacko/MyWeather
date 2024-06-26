#parsing weatherapi JSON files
from . import obj
from datetime import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M"



#---helper functions to parse tiny classes---#

#wind speed and direction in degrees
def ParseWindData(weatherdata): return obj.WindData(weatherdata["wind_kph"], weatherdata["wind_degree"])

#actual and feelslike temperature
def ParseTemperatureData(weatherdata): return obj.TemperatureData(weatherdata["temp_c"], weatherdata["feelslike_c"])


#chance and height in mm of precipitation
def ParseRainData(weatherdata, sample_size):
    return obj.RainData(weatherdata["precip_mm"], weatherdata["chance_of_rain"]) \
    if sample_size == "hour" else obj.RainData(weatherdata["totalprecip_mm"], weatherdata["daily_chance_of_rain"])



#---helper functions to parse data for the Forecast class---#



#parses the min/max/avg stats for daily forecast 
def ParseStats(dailyweatherdata):
    params = {
        "max_temp" : dailyweatherdata["maxtemp_c"],
        "min_temp" : dailyweatherdata["mintemp_c"],
        "avg_temp" : dailyweatherdata["avgtemp_c"],
        "max_wind" : dailyweatherdata["maxwind_kph"],
        "avg_humidity" : dailyweatherdata["avghumidity"]
    }

    return obj.Stats(**params)



#parses hourly weather forecast data
def ParseHourlyWeather(hourlydata):
    params = {
        "time" : datetime.strptime(hourlydata["time"], DATE_FORMAT),
        "humidity" : hourlydata["humidity"],
        "condition" : hourlydata["condition"]["text"],
        "wind_data" : ParseWindData(hourlydata),
        "temperature_data" : ParseTemperatureData(hourlydata),
        "rain_data" : ParseRainData(hourlydata, "hour")
    }

    return obj.Hour(**params)



#parses daily weather data
def ParseDailyWeather(dailydata):
    dailyweatherdata = dailydata["day"]
    params = {
        "date" : datetime.strptime(dailydata["date"], "%Y-%m-%d"),
        "stats" : ParseStats(dailyweatherdata),
        "rain_data" : ParseRainData(dailyweatherdata, "Day"),
        "condition" : dailyweatherdata["condition"]["text"],
        "hours" : [ParseHourlyWeather(hour) for hour in dailydata["hour"]]         
    }

    return obj.Day(**params)



#---Main functions---#



#parses a realtime API response and returns a Realtime class object
def ParseRealtimeWeather(response):
    local_data = response["location"] #contains metadata such as time
    weather_data = response["current"] #contains the actual weather data
    
    #parsing individual arguments
    params = {
        "location" : local_data["name"],
        "date" : datetime.strptime(local_data["localtime"], DATE_FORMAT),
        "temperature" : ParseTemperatureData(weather_data),
        "wind" : ParseWindData(weather_data),
        "precip_height" : weather_data["precip_mm"],
        "humidity" : weather_data["humidity"],
        "condition" : weather_data["condition"]["text"]
    }

    #initialize and return the new object of type Realtime
    return obj.Realtime(**params)




#parses data for the entire forecast
def ParseForecastWeather(response):
    local_data = response["location"]
    weather_data = response["forecast"]

    params = {
        "location" : local_data["name"],
        "days" : [ParseDailyWeather(day) for day in weather_data["forecastday"]]
    }

    return obj.Forecast(**params)