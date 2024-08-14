from . import *
from MyWeather.Constdata.SidebarButtons import buttons
from MyWeather.Constdata.Mode import MODE
from .SidebarButton import SidebarButton





class Sidebar(QWidget):
    """Main Window sidebar type, contains about 3-4 sidebar buttons

    Args:
        QWidget (QWidget): Inherits from the basic QWidget class
    """

    def __init__(self, color : gui.QColor):
        super().__init__()

        #empty buttons list
        self.buttons : list[SidebarButton] = []        

        #set the sidebar color
        self.setAutoFillBackground(True)

        #create a palette
        (palette := self.palette()).setColor(gui.QPalette.ColorRole.Window, color)              
        self.setPalette(palette)
        self._palette_ = palette                                    #set the palette as an instance attribute for later color change and maybe other stuff tbh



        self._layout_ = QVBoxLayout()                               #dummy layout, parent widget updates this when initializing


        (icon := QLabel()).setPixmap(
            gui.QPixmap('Assets/MainIcon.png'))                     #set an centrally-aligned icon
        
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._layout_.addWidget(icon)


        self._layout_.addStretch()


    def SetLayoutSpacing(self):
        """Called inside the InitButtons method, sets the layout spacing and aligns the items correctly"""

        self._layout_.setContentsMargins(0,0,0,200)                 #zero margins
        self._layout_.setSpacing(0)                                 #zero spacing between elements


        for index in range(self._layout_.count()):                  #evenly stretch out all elements    
            self._layout_.setStretch(index, 1)



    def UpdateFonts(self, font):
        """Called inside the settings"""
        for button in self.buttons:
            button.font = font
            button.setFont(gui.QFont(font))
