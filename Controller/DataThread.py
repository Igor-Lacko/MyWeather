from MyWeather.Model import obj, request as API
from PyQt6.QtCore import QThread, pyqtSignal, QObject
import geocoder
from MyWeather.Init import LOCATION






class WeatherFetcher(QObject):
        
    failed = pyqtSignal()
    ready = pyqtSignal(obj.BulkData)

    def __init__(self):
        super().__init__()
        self.current_location = LOCATION


    def FetchNewData(self, location : str):


        self.current_location = location

        if location.lower() == "current":
            location = geocoder.ip('me').latlng

            if location is not None:
                location = f"{location[0]},{location[1]}"

            else:
                self.failed.emit()
                return
        

        if (data := API.CompleteData(location)) is None:
            self.failed.emit()
            return

        else:
            self.ready.emit(data)


    def UpdateData(self):
        if self.current_location.lower() == "current":
            location = geocoder.ip('me').latlng

            if location is not None:
                location = f"{location[0]},{location[1]}"

            else:
                self.failed.emit()
                return

        else:
            location = self.current_location

        if (data := API.CompleteData(location)) is None:
            self.failed.emit()
            return

        else:
            self.ready.emit(data)





