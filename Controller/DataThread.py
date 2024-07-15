from ..Model import obj, request as API
from PyQt6.QtCore import QThread, pyqtSignal, QObject
import geocoder
from MyWeather.Init import LOCATION






class WeatherFetcher(QObject):
        
    failed = pyqtSignal()
    ready = pyqtSignal(obj.Realtime)

    def __init__(self):
        super().__init__()
        self.location_param = None


    def FetchLocationData(self, location : str):
        
        if location.lower() == "current":
            self.location_param = geocoder.ip('me').latlng

            if self.location_param is not None:
                self.location_param = f"{self.location_param[0]},{self.location_param[1]}"

            else:
                return None
            
        if (data := API.RealtimeWeather(location)) is None:
            return None
        
        else:
            return data




