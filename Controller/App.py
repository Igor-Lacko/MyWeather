from PyQt6 import QtWidgets as widgets, QtCore as core
from .CommunicatorObject import WeatherFetcher
from .HeaderController import HeaderController
from .HomeGraphController import GraphController
from .SidebarController import SidebarController
from .WeatherTabController.ControllerClass import WeatherController
from functools import partial

class Application(widgets.QApplication):
    
    def __init__(self, argv: list[str] = []) -> None:
        super().__init__(argv)

        self.worker_thread = core.QThread()
        self.worker_object = WeatherFetcher()

        self.worker_object.moveToThread(self.worker_thread)

        self.header_controller = HeaderController()
        self.graph_controller = GraphController()
        self.sidebar_controller = SidebarController()
        self.weather_controller = WeatherController()

        self.worker_thread.start()



    def ConnectThreadController(self):
        #----------FAILURE CONNECTS FOR HOME TAB----------#
        self.worker_object.failed_home.connect(self.header_controller.FailureHandler)
        self.worker_object.failed_home.connect(self.graph_controller.FailureHandler)

        #----------SUCCESS CONNECTS FOR HOME TAB----------#
        self.worker_object.bulk.connect(lambda data: self.header_controller.UpdateHeader(data.current, self.header_controller.header))
        self.worker_object.bulk.connect(lambda data: self.graph_controller.UpdateGraph(data.forecast))

        #----------FAILURE CONNECT FOR WEATHER TAB----------#
        #self.worker_object.failed_weather.connect(self.weather_controller.ResponseFailed)

        #----------SUCCESS CONNECTS FOR WEATHER TAB----------#
        for signal in [self.worker_object.realtime, self.worker_object.timeline]:
            signal.connect(self.weather_controller.ResponseSuccess)