from MyWeather.Model import obj, request as API
from PyQt6.QtCore import QThread, pyqtSignal, QObject
import geocoder
from MyWeather.Init import LOCATION






class DataCommunicator(QObject):

    #define signals for all APIs
    failed_home = pyqtSignal()
    failed_weather = pyqtSignal()
    bulk = pyqtSignal(obj.BulkData)
    timeline = pyqtSignal(obj.Timeline)         #mutual for history/forecast since it's the same class
    realtime = pyqtSignal(obj.Realtime)

    def __init__(self):
        super().__init__()
        self.current_location = LOCATION
        self.data : obj.BulkData | obj.Realtime | obj.Timeline = None


    def FetchNewData(self, opts):
        """Fetches new data based on the api argument

        Args:
            location (str): The location the data will be describing. Mandatory for all APIs
            api (str, optional): _description_. Defaults to 'bulk'.
            days (int, optional): Number of days the data will show, mandatory for Bulk/Forecast/History. Defaults to 3.
            date (_type_, optional): Date restriction, optional for Bulk/Forecast/History. Defaults to None.
        """
        self.current_location = opts['location']

        if opts['location'].lower() == "current":
            location = geocoder.ip('me').latlng

            if location is not None:
                location = f"{location[0]},{location[1]}"

            else:
                self.failed_home.emit()
                return

        else:
            location = self.current_location

        try:
            match opts['api']:
                #get data based on the api
                case 'bulk':
                    data = API.CompleteData(location, opts['days'], opts['date'])

                case 'realtime':
                    data = API.RealtimeWeather(location)

                case 'forecast':
                    data = API.Forecast(location, opts['days'], opts['date'])

                case 'history':
                    data = API.HistoricWeather(location)        #TODO: Add restrictions

            if data is None:
                if opts['api'] == 'bulk': #the failure is from home tab
                    self.failed_home.emit()

                else:
                    self.failed_weather.emit()

                return

        except Exception:
            if opts['api'] == 'bulk': #the failure is from home tab
                self.failed_home.emit()

            else:
                self.failed_weather.emit()

            return

        #emit a success signal based on the api
        self.EmitSuccess(data, opts['api'])


    #used on the home tab, so only with bulk data
    def UpdateData(self, days : int=3, date=None):
        if self.current_location.lower() == "current":
            location = geocoder.ip('me').latlng

            if location is not None:
                location = f"{location[0]},{location[1]}"

            else:
                self.failed_home.emit()
                return

        else:
            location = self.current_location

        if (data := API.CompleteData(location, days=days, dt=date)) is None:
            print("nn")
            self.failed_home.emit()
            return

        else:
            self.bulk.emit(data)


    def EmitSuccess(self, data : obj.Realtime | obj.Timeline | obj.BulkData, api : str):
        """Emits one of the defined signals based on the provided type

        Args:
            data (obj.Realtime | obj.Timeline | obj.BulkData): The provided weather data
            api (str): API/data type as a string, for easier conditionals with case
        """

        match api:
            case 'realtime':
                self.realtime.emit(data)

            case 'forecast' | 'history':
                self.timeline.emit(data)

            case 'bulk':
                self.bulk.emit(data)
