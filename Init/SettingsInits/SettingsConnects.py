"""Functions that connect settings menus to their respective functionality"""
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QLabel
from MyWeather.View.MainWindow import MainWindow
from MyWeather.Controller.SettingsController.Functions import UpdateSettingsFonts




def SetFont(widget : QWidget, font : str):
    """Helper function to be passed into the functools.partial method"""
    widget.setFont(QFont(font))







def ConnectSettingsMenus(main_window : MainWindow):
    """Connects all menus in the settings to their respective functionalities"""

    for item in main_window.settings.items:

        if type(item) != QLabel:

            match item.description.text():

                case "Default location":
                    item.submitted.connect(lambda location: main_window.home.header.FetchNewData(location))
            
                case "Sidebar":
                    item.menu.currentTextChanged.connect(lambda font: main_window.sidebar.UpdateFonts(font))

                case "Header lead":
                    item.menu.currentTextChanged.connect(lambda font: main_window.home.header.UpdateLeadFont(font))

                case "Header data":
                    item.menu.currentTextChanged.connect(lambda font: main_window.home.header.UpdateDataFont(font))

                case "Weather tab":
                    item.menu.currentTextChanged.connect(lambda font: main_window.weather.UpdateFonts(font))

                case "Graph header":
                    item.menu.currentTextChanged.connect(lambda font: main_window.home.window.graph.header.UpdateFonts(font))
                
                case "Other":
                    item.menu.currentTextChanged.connect(lambda font: UpdateSettingsFonts(main_window.settings, font))



