from PyQt6 import QtWidgets as widgets, QtCore as core
from .DataThread import WeatherFetcher
from .HeaderController import HeaderController
from .GraphController import GraphController

class Application(widgets.QApplication):
    
    def __init__(self, argv: list[str] = []) -> None:
        super().__init__(argv)

        self.worker_thread = core.QThread()
        self.worker_object = WeatherFetcher()

        self.worker_object.moveToThread(self.worker_thread)

        self.header_controller = HeaderController()
        self.graph_controller = GraphController()

        self.worker_thread.start()



    def ConnectThreadController(self):
        
        #----------FAILURE CONNECTS----------#
        self.worker_object.failed.connect(self.header_controller.FailureHandler)
        self.worker_object.failed.connect(self.graph_controller.FailureHandler)



        #----------SUCCESS CONNECTS----------#
        self.worker_object.ready.connect(lambda data: self.header_controller.UpdateHeader(data.current, self.header_controller.header))
        self.worker_object.ready.connect(lambda data: self.graph_controller.UpdateGraph(data.forecast))