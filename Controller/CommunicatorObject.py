from MyWeather.Model import obj, request as API
from PyQt6.QtCore import QThread, pyqtSignal, QObject, QTimer, QEventLoop
import geocoder
from MyWeather.Init import LOCATION
from enum import Enum


class State(Enum):
    """Helper enum when checking for success"""
    Idle = 0
    Failed = 1
    Success = 2


class DataCommunicator(QObject):

    #define signals for all APIs
    failed_home = pyqtSignal()
    failed_weather = pyqtSignal()
    bulk = pyqtSignal(obj.BulkData)
    timeline = pyqtSignal(obj.Timeline)         #mutual for history/forecast since it's the same class
    realtime_graph = pyqtSignal(obj.Day)
    realtime_text = pyqtSignal(obj.Realtime)
    fetch = pyqtSignal(dict)
    update = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.state : State = State.Idle
        self.data : obj.BulkData | obj.Realtime | obj.Timeline = None
        self.api : str = None




    def CheckSuccess(self):
        """Called after fetch/update, implements a custom "timeout" with QTimer"""
        if self.data is None:
            self.state = State.Failed
            return

        self.state = State.Success


    def AwaitResponse(self):
        """Called after fetch/update, implements a custom "timeout" with QTimer"""
        for _ in range(5):
            loop = QEventLoop()         #use a QEventLoop to block the for loop for a second
            QTimer.singleShot(1000, loop.quit)
            loop.exec()

            self.CheckSuccess()
            #check if the request was successful
            if self.state == State.Success:
                self.SignalSuccess()
                return

        self.SignalFail()


    def SignalFail(self):
        """Emits one of the fail signals depending on self.api (since Home tab uses bulk api and Weather tab uses the other types)"""
        print('EPIC FAIL')
        if self.api == 'bulk':
            self.failed_home.emit()

        else:
            self.failed_weather.emit()

        #reset
        self.api = None
        self.state = State.Idle


    def SignalSuccess(self):
        """Emits one of the defined signals based on the provided type

        Args:
            data (obj.Realtime | obj.Timeline | obj.BulkData): The provided weather data
        """

        match self.api:
            case 'realtime':
                if isinstance(self.data, obj.Realtime):
                    self.realtime_text.emit(self.data)

                else:
                    self.realtime_graph.emit(self.data)

            case 'forecast' | 'history':
                self.timeline.emit(self.data)

            case 'bulk':
                self.bulk.emit(self.data)

        #reset
        self.api = None
        self.state = State.Idle


    #Signal emitter methods
    def UpdateData(self):
        self.data = None
        self.api = 'bulk'
        self.update.emit()
        self.AwaitResponse()

    def FetchNewData(self, opts):
        self.data = None
        self.api = opts['api']
        self.fetch.emit(opts)
        self.AwaitResponse()
