"""Functions that connect settings menus to their respective functionality"""
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QLabel
from MyWeather.View.components.Settings.SettingsWindow import SettingsTab
from MyWeather.View.components.Sidebar.Sidebar import Sidebar
from MyWeather.View.components.Home.Header.Header import Header
from MyWeather.View.components.Home.HomeWindow.Graph.FrameHeader import FrameHeader
from MyWeather.Controller.SettingsController.Functions import UpdateSettingsFonts




def SetFont(widget : QWidget, font : str):
    """Helper function to be passed into the functools.partial method"""
    widget.setFont(QFont(font))







def ConnectFontSlots(Settings : SettingsTab, Sidebar : Sidebar, Header : Header, Graph : FrameHeader):
    """Connects all menus in the settings to their respective functionalities"""

    for item in Settings.items:

        if type(item) != QLabel:

            match item.description.text():

                case "Default location":
                    item.submitted.connect(lambda location: Header.update(location))
            
                case "Sidebar":
                    item.menu.currentTextChanged.connect(lambda font: Sidebar.UpdateFonts(font))

                case "Header lead":
                    item.menu.currentTextChanged.connect(lambda font: Header.UpdateLeadFont(font))

                case "Header data":
                    item.menu.currentTextChanged.connect(lambda font: Header.UpdateDataFont(font))

                case "Graph header":
                    item.menu.currentTextChanged.connect(lambda font: Graph.widgets[1].UpdateFonts(font))
                
                case "Other":
                    item.menu.currentTextChanged.connect(lambda font: UpdateSettingsFonts(Settings, font))



