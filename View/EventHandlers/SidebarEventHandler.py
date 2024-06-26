#includes event handler functions for mouse events
import PyQt6.QtWidgets as widgets
from PyQt6.QtGui import QIcon, QPalette 
from PyQt6.QtCore import QSize
from ..utils.enumerations import Colors, ColorMode
from ..constdata import buttons as buttons
from ..components import Sidebar
from ..constdata.mode import MODE




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



    MODE = ColorMode.DARK if MODE == ColorMode.LIGHT else ColorMode.LIGHT
    buttons.UpdateButtons(MODE)

    for index, button in enumerate(buttons.buttons):
        
        sidebar.buttons[index].setIcon(QIcon(button['icon']))
        sidebar.buttons[index].setIconSize(QSize(45, 45))
        sidebar.buttons[index].SetStyle(sidebar.buttons[index].position,MODE)
        

    sidebar._palette_.setColor(QPalette.ColorRole.Window,
                                Colors.CoolGrey
                                if MODE == ColorMode.DARK
                                else Colors.OffWhite)

    sidebar.setPalette(sidebar._palette_)

    sidebar.buttons[3].color_switch_signal.emit(MODE)
    

    







