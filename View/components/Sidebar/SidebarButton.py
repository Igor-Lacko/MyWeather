from . import *
from View.StyleSheets.Sidebar import Dark, Light



class SidebarButton(QToolButton):
    """Class used for the sidebar, about 3-4 of them should be used ideally

    Args:
        QPushButton (QPushButton): Inherits from the standard Qt ToolButton class
    """


    color_switch_signal = pyqtSignal(ColorModes)
    tab_switch_signal = pyqtSignal(int)


    def __init__(self, icon_path : str, description : str, mode : ColorModes, index : int, position : str = "default"):
        """Sidebar button constructor

        Args:
            icon_path (str): The path to the icon to be used
            mode (ColorModes): Current color mode
            description (str): Button description (which tab does it switch to in the main window)
            index (int): Button's index in the sidebar
            position (str): Button's position in the toolbar
        """ 
        super().__init__()

        self.position = position
        self.index = index
        self.font = FONTS.sidebar

        if not re.match(r".* mode", description):
            self.clicked.connect(lambda: self.tab_switch_signal.emit(self.index))

        #set the color and border
        self.SetStyle(self.position, mode)


        #icon and text from params
        self.setIcon(gui.QIcon(icon_path))
        self.setIconSize(QSize(45,45))
        self.setText(description)





    def SetStyle(self, position : str, mode : ColorModes):
        """sets a stylesheet for the button with transparency and some other stuff"""


        sheet = Dark if mode.value == "dark" else Light                             #get the sheet module to be set        


        #get the default style sheet according to the button's position in the toolbar
        default = sheet.SidebarButtonDefault if position not in ["top", "bottom"]\
        else (sheet.SidebarButtonTop
                if position == "top" else sheet.SidebarButtonBottom)

        #join the default and hover style sheets together
        style_sheet = f"{default}\n\n{sheet.SidebarButtonHover}"

        #set it to the button
        self.setStyleSheet(style_sheet)

        #text under icon for a more modern look
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        #default font
        self.setFont(gui.QFont(self.font))

        #size policy
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

