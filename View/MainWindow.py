#includes the MyWeather MainWindow class
import PyQt6.QtWidgets as widgets
from PyQt6.QtCore import Qt
from MyWeather.View.utils import enumerations
from MyWeather.Model.constdata.buttons import buttons
from MyWeather.Model.constdata.mode import MODE
from .components.Sidebar import Sidebar
from .tabs import Settings, Home, Weather




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

        (main_layout := widgets.QHBoxLayout()).addWidget(sidebar := Sidebar(enumerations.Colors.CoolGrey))
        main_layout.addLayout(tabs := widgets.QStackedLayout())

        (home := widgets.QWidget()).setLayout(home_tab := Home.HomeTab())
        
        (settings := widgets.QWidget()).setLayout(Settings.SettingsTab())
        (weather := widgets.QWidget()).setLayout(Weather.WeatherTab())

        tabs.addWidget(home)
        tabs.addWidget(weather)
        tabs.addWidget(settings)

        sidebar._layout_= sidebar.InitButtons(buttons, tabs, MODE)
        sidebar.mode_trigger.color_switch_signal.connect(home_tab.header.SwitchColorMode)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        
        main_layout.setStretch(0, 3)
        main_layout.setStretch(1, 97)

        empty.setLayout(main_layout)


        self.main_layout = main_layout

    
        
    
    def Run(self):
        """maximizes and shows the window"""

        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.show()




