from . import *
from typing import Callable



class SidebarButton(QToolButton):
    """Class used for the sidebar, about 3-4 of them should be used ideally

    Args:
        QPushButton (QPushButton): Inherits from the standard Qt ToolButton class
    """


    color_switch_signal = pyqtSignal(ColorModes)


    def __init__(self, icon_path : str, description : str, on_click : Callable, mode : ColorModes,  position : str = "default"):
        """Sidebar button constructor

        Args:
            icon_path (str): The path to the icon to be used
            description (str): Button description (which tab does it switch to in the main window)
            on_click (Callable): We'll connect the button to a slot with this function
            position (str): Button's position in the toolbar
        """ 
        super().__init__()
        


        self.position = position           


        #set the color and border
        self.SetStyle(self.position, mode)


        #icon and text from params
        self.setIcon(gui.QIcon(icon_path))
        self.setIconSize(QSize(45,45))
        self.setText(description)

        #connect the button to the passed in function
        self.clicked.connect(on_click)

        



    def SetStyle(self, position : str, mode : ColorModes):
        """sets a stylesheet for the button with transparency and some other stuff"""


        sheet = StyleSheets.dark\
        if mode.value == "dark"\
        else StyleSheets.light                             #get the sheet to be set        


        #get the default style sheet according to the button's position in the toolbar
        default = sheet.SidebarButtonDefault if position not in ["top", "bottom"]\
        else (sheet.SidebarButtonTop 
                if position == "top" else sheet.SidebarButtonBottom)

        
        #join the default and hover style sheets together
        style_sheet = f"{default.value}\n\n{sheet.SidebarButtonHover.value}"

        #set it to the button
        self.setStyleSheet(style_sheet)
        
        #text under icon for a more modern look
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        #default font
        self.setFont(gui.QFont(FONTS.sidebar))

        #size policy
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        