#includes the MyWeather MainWindow class
from Constdata import SidebarButtons
from . import *
from PyQt6.QtCore import Qt
from MyWeather.View.utils import enumerations                           #absolute imports to avoid enum issues
from MyWeather.Constdata.Mode import MODE
from MyWeather.Init import SidebarInit
from .components.Home import HomeTab
from .components.Settings.SettingsWindow import SettingsTab
from .components.Weather.WeatherWindow import WeatherTab



class MainWindow(widgets.QMainWindow):
    """Main window class for the View part

    Args:
        widgets (QMainWindow): Inherits from the Qt default MainWindow class
    """


    def __init__(self):
        """Main Window constructor"""

        super().__init__()
        self.setWindowTitle("MyWeather")


        #dummy widget to set layout
        self.setCentralWidget(empty := widgets.QWidget())

        (main_layout := widgets.QHBoxLayout()).addWidget(sidebar := SidebarInit.GetSidebar())
        main_layout.addLayout(tabs := widgets.QStackedLayout())

        (home := widgets.QWidget()).setLayout(home_tab := HomeTab())

        tabs.addWidget(home)
        tabs.addWidget(weather := WeatherTab())
        tabs.addWidget(settings := SettingsTab())


        
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        
        main_layout.setStretch(0, 3)
        main_layout.setStretch(1, 97)

        empty.setLayout(main_layout)


        self.main_layout = main_layout
        self.sidebar = sidebar
        self.settings = settings
        self.home = home_tab
        self.weather = weather
        self.tabs = tabs

    
        
    
    def Run(self):
        """maximizes and shows the window"""
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.show()




