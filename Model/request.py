from . import api
from swagger_client.rest import ApiException
from urllib3.exceptions import NewConnectionError, MaxRetryError
from termcolor import colored
from datetime import date, timedelta
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
        if response is None:
            return None
        
        return parse.ParseRealtimeWeather(response)



#forecast for city "city" for the next "days" days
def Forecast(city : str, days : int = 3, dt : date = None) -> parse.obj.Timeline:
    try:
        response = api.forecast_weather(q=city, days=days, dt=dt)
    
    except ApiException:
        print(colored("\n\n--------------------Error: Invalid argument in API call--------------------\n", "red"))
        return None
    
    except (NewConnectionError, MaxRetryError):
        print(colored("\n\n--------------------Error: Connection unsuccessful----------------------\n", "red"))
        return None
    
    else:
        return parse.ParseTimelineWeather(response)


#historic weather up to 7 days ahead
def HistoricWeather(city : str, beginning : date = date.today() - timedelta(days=7)):
    try:
        response = api.history_weather(q=city, dt=beginning)
    
    except ApiException:
        print(colored("\n\n--------------------Error: Invalid argument in API call--------------------\n", "red"))
        return None
    
    except (NewConnectionError, MaxRetryError):
        print(colored("\n\n--------------------Error: Connection unsuccessful----------------------\n", "red"))
        return None
    
    else:
        return parse.ParseTimelineWeather(response)




def CompleteData(city : str, days : int = 3, dt : date = None) -> parse.obj.BulkData:
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








