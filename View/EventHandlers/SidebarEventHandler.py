#includes event handler functions for mouse events
import PyQt6.QtWidgets as widgets
from PyQt6.QtGui import QIcon, QPalette 
from PyQt6.QtCore import QSize
from MyWeather.View.utils.enumerations import Colors, ColorModes
from MyWeather.Model.constdata.mode import MODE
from ...Model.constdata import buttons
from ..components import Sidebar





def switch_tab(layout : widgets.QStackedLayout, index : int):
    """Switches the current tab in the main stacked layout

    Args:
        layout (widgets.QStackedLayout): The layout passed in as an argument
        index (int): The index to switch to
    """

    layout.setCurrentIndex(index)



def switch_sidebar_color(sidebar : Sidebar.Sidebar):
    """So far only updates the sidebar's color and his icons"""
    global MODE



    MODE = ColorModes.DARK if MODE == ColorModes.LIGHT else ColorModes.LIGHT
    buttons.UpdateButtons(MODE)

    for index, button in enumerate(buttons.buttons):
        
        sidebar.buttons[index].setIcon(QIcon(button['icon']))
        sidebar.buttons[index].setIconSize(QSize(45, 45))
        sidebar.buttons[index].SetStyle(sidebar.buttons[index].position,MODE)
        

    sidebar._palette_.setColor(QPalette.ColorRole.Window,
                                Colors.CoolGrey
                                if MODE == ColorModes.DARK
                                else Colors.OffWhite)

    sidebar.setPalette(sidebar._palette_)

    print(sidebar.mode_trigger.color_switch_signal.__repr__())

    sidebar.mode_trigger.color_switch_signal.emit(MODE)
    

    







