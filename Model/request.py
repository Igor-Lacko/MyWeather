from . import api
from weatherapi.rest import ApiException
from urllib3.exceptions import NewConnectionError, MaxRetryError
from termcolor import colored
from datetime import date, timedelta
from . import parse




#realtime weather request
def RealtimeWeather(city : str) -> parse.obj.Realtime:
    try:
        response = api.realtime_weather(q=city)
    
    except Exception:
        print(colored("\n\n--------------------Error--------------------\n", "red"))
        return None

    else:
        if response is None:
            return None

        return parse.ParseRealtimeWeather(response)



#forecast for city "city" for the next "days" days
def Forecast(city : str, days : int = 3, dt : date = None) -> parse.obj.Timeline:
    try:
        response = api.forecast_weather(q=city, days=days, dt=dt)

    except Exception:
        print(colored("\n\n--------------------Error--------------------\n", "red"))
        return None

    else:
        return parse.ParseTimelineWeather(response)


#historic weather up to 7 days ahead
def HistoricWeather(city : str, days : int = 7):
    try:
        response = api.history_weather(q=city, dt=date.today() - timedelta(days=days), end_dt=date.today() - timedelta(days=1))

    except Exception:
        print(colored("\n\n--------------------Error--------------------\n", "red"))
        return None


    else:
        return parse.ParseTimelineWeather(response)




def CompleteData(city : str, days : int = 3, dt : date = None) -> parse.obj.BulkData:
    try:
        response = api.forecast_weather(q=city, days=days, dt=dt)
    
    except Exception:
        print(colored("\n\n--------------------Error--------------------\n", "red"))
        return None


    else:
        if response is None:
            return None

        return parse.ParseWeatherData(response)








