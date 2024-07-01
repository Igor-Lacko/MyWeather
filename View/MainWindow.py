#includes the MyWeather MainWindow class
from . import *
from PyQt6.QtCore import Qt
from MyWeather.View.utils import enumerations                           #absolute imports to avoid enum issues
from .constdata.mode import MODE
from .constdata import buttons, slots
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

        DEFAULT_COLOR = enumerations.Colors.CoolGrey if MODE == enumerations.ColorModes.DARK\
        else enumerations.Colors.OffWhite

        #dummy widget to set layout
        self.setCentralWidget(empty := widgets.QWidget())

        (main_layout := widgets.QHBoxLayout()).addWidget(sidebar := Sidebar(DEFAULT_COLOR))
        main_layout.addLayout(tabs := widgets.QStackedLayout())

        (home := widgets.QWidget()).setLayout(home_tab := Home.HomeTab())
        
        (settings := widgets.QWidget()).setLayout(Settings.SettingsTab())
        (weather := widgets.QWidget()).setLayout(Weather.WeatherTab())

        tabs.addWidget(home)
        tabs.addWidget(weather)
        tabs.addWidget(settings)

        sidebar._layout_= sidebar.InitButtons(buttons.buttons, tabs, MODE, slots.slots)
        sidebar.mode_trigger.color_switch_signal.connect(home_tab.header.SwitchColorMode)
        sidebar.mode_trigger.color_switch_signal.connect(home_tab.window.switch_color_mode)
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




