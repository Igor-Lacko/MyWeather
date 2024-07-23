"""Includes sidebar controllers.\n
-Written functionally instead of OOP because i wrote it too early and refactoring it would be a pain, maybe later"""
import PyQt6.QtWidgets as widgets
from PyQt6.QtGui import QIcon, QPalette 
from PyQt6.QtCore import QSize, QObject
from MyWeather.View.utils.enumerations import Colors, ColorModes
from MyWeather.Constdata.Mode import MODE
from MyWeather.Constdata import SidebarButtons
from MyWeather.View.components.Sidebar.Sidebar import Sidebar




class SidebarController(QObject):
    """Sidebar controller class"""

    
    def ConnectSidebar(self, sidebar : Sidebar):
        self.sidebar = sidebar
        self.sidebar.mode_trigger.clicked.connect(self.switch_sidebar_color)


    def switch_sidebar_color(self):
        """Updates the sidebar's color and his icons"""
        global MODE


        MODE = ColorModes.DARK if MODE == ColorModes.LIGHT else ColorModes.LIGHT
        SidebarButtons.UpdateButtons(MODE)

        for index, button in enumerate(SidebarButtons.buttons):
        
            self.sidebar.buttons[index].setIcon(QIcon(button['icon']))
            self.sidebar.buttons[index].setIconSize(QSize(45, 45))
            self.sidebar.buttons[index].SetStyle(self.sidebar.buttons[index].position,MODE)
            self.sidebar.buttons[index].setText(button['text'])
        

        self.sidebar._palette_.setColor(QPalette.ColorRole.Window,
                                    Colors.CoolGrey
                                    if MODE == ColorModes.DARK
                                    else Colors.OffWhite)

        self.sidebar.setPalette(self.sidebar._palette_)


        self.sidebar.mode_trigger.color_switch_signal.emit(MODE)