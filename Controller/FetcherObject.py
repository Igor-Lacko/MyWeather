"""Contains the WeatherFetcher object which fetches weather data and passes them to a communicator object"""
from MyWeather.Model import obj, request as API
from PyQt6.QtCore import pyqtSignal, QObject
import geocoder
from .CommunicatorObject import DataCommunicator
from MyWeather.Init import LOCATION


class WeatherFetcher(QObject):

    def __init__(self, communicator : DataCommunicator):
        """Weather fetcher constructor"""
        super().__init__()
        self.communicator = communicator
        self.current_location = LOCATION


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
                self.communicator.data = None
                return

        else:
            location = self.current_location

        match opts['api']:
            #get data based on the api
            case 'bulk':
                data = API.CompleteData(location, opts['range'], None)

            case 'realtime':
                data = API.Forecast(location, 1).days[0]

            case 'forecast':
                data = API.Forecast(location, opts['range'], None)

            case 'history':
                data = API.HistoricWeather(location, opts['range'])        #TODO: Add restrictions

        self.communicator.data = data



    #used on the home tab, so only with bulk data
    def UpdateData(self, days : int=3, date=None):
        if self.current_location.lower() == "current":
            location = geocoder.ip('me').latlng

            if location is not None:
                location = f"{location[0]},{location[1]}"

            else:
                self.communicator.data = None
                return

        else:
            location = self.current_location

        if (data := API.CompleteData(location, days=days, dt=date)) is None:
            self.communicator.data = None

        else:
            self.communicator.data = data