from PyQt6 import QtWidgets as widgets, QtCore as core


class Application(widgets.QApplication):
    
    def __init__(self, argv: list[str] = []) -> None:
        super().__init__(argv)
        self.worker = core.QThread()