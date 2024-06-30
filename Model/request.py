from . import api
from swagger_client.rest import ApiException
from urllib3.exceptions import NewConnectionError, MaxRetryError
from termcolor import colored
from datetime import datetime as date
from . import parse



#realtime weather request
def RealtimeWeather(city : str) -> parse.obj.Realtime:
    try:
        response = api.realtime_weather(q=city)
    
    except ApiException:
        print(colored("\n\n--------------------Error: Invalid argument in API call--------------------\n", "red"))
        return None
    
    except (NewConnectionError, MaxRetryError):
        print(colored("\n\n--------------------Error: Connection unsuccessful----------------------\n", "red"))
        return None
    
    else:
        return parse.ParseRealtimeWeather(response)


#forecast for city "city" for the next "days" days
def Forecast(city : str, days : int = 7 - date.today().weekday(), dt : date = None) -> parse.obj.Forecast:
    try:
        response = api.forecast_weather(q=city, days=days, dt=dt)
    
    except ApiException:
        print(colored("\n\n--------------------Error: Invalid argument in API call--------------------\n", "red"))
        return None
    
    except (NewConnectionError, MaxRetryError):
        print(colored("\n\n--------------------Error: Connection unsuccessful----------------------\n", "red"))
        return None
    
    else:
        return parse.ParseForecastWeather(response)
    




def CompleteData(city : str, days : int = 7 - date.today().weekday(), dt : date = None) -> parse.obj.WeatherData:
    try:
        response = api.forecast_weather(q=city, days=days, dt=dt)
    
    except ApiException:
        print(colored("\n\n--------------------Error: Invalid argument in API call--------------------\n", "red"))
        return None
    
    except (NewConnectionError, MaxRetryError):
        print(colored("\n\n--------------------Error: Connection unsuccessful----------------------\n", "red"))
        return None
    
    else:
        return parse.ParseWeatherData(response)
    





