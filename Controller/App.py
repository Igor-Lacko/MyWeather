from PyQt6 import QtWidgets as widgets, QtCore as core
from .CommunicatorObject import DataCommunicator
from .FetcherObject import WeatherFetcher
from .HeaderController import HeaderController
from .HomeGraphController import GraphController
from .SidebarController import SidebarController
from .WeatherTabController.ControllerClass import WeatherController
from functools import partial

class Application(widgets.QApplication):
    
    def __init__(self, argv: list[str] = []) -> None:
        super().__init__(argv)

        #initialize objects in other threads
        self.communicator_thread = core.QThread()
        self.communicator_object = DataCommunicator()

        self.worker_thread = core.QThread()
        self.worker_object = WeatherFetcher(self.communicator_object)

        self.worker_object.moveToThread(self.worker_thread)

        self.header_controller = HeaderController()
        self.graph_controller = GraphController()
        self.sidebar_controller = SidebarController()
        self.weather_controller = WeatherController()

        self.worker_thread.start()
        self.communicator_thread.start()



    def ConnectThreadController(self):
        #----------CONNECT THE FETCHER/INTERMEDIATE OBJECTS TOGETHER----------#
        self.communicator_object.update.connect(self.worker_object.UpdateData)
        self.communicator_object.fetch.connect(self.worker_object.FetchNewData)


        #----------FAILURE CONNECTS FOR HOME TAB----------#
        self.communicator_object.failed_home.connect(self.header_controller.FailureHandler)
        self.communicator_object.failed_home.connect(self.graph_controller.FailureHandler)

        #----------SUCCESS CONNECTS FOR HOME TAB----------#
        self.communicator_object.bulk.connect(lambda data: self.header_controller.UpdateHeader(data.current, self.header_controller.header))
        self.communicator_object.bulk.connect(lambda data: self.graph_controller.UpdateGraph(data.forecast))

        #----------FAILURE CONNECT FOR WEATHER TAB----------#
        self.communicator_object.failed_weather.connect(self.weather_controller.ResponseFail)

        #----------SUCCESS CONNECTS FOR WEATHER TAB----------#
        for signal in [self.communicator_object.realtime_graph, self.communicator_object.realtime_text, self.communicator_object.timeline]:
            signal.connect(self.weather_controller.ResponseSuccess)