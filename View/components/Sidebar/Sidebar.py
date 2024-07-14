from . import *
from functools import partial
from .SidebarButton import SidebarButton
import re





class Sidebar(QWidget):
    """Main Window sidebar type, contains about 3-4 sidebar buttons

    Args:
        QWidget (QWidget): Inherits from the basic QWidget class
    """

    def __init__(self, color : gui.QColor):
        super().__init__()

        #empty buttons list
        self.buttons = []        

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

        
        

        
        

        
        
        

    
    def InitButtons(self, buttons : dict, tabs : QLayout, mode : ColorModes, slots : dict[str, callable]) -> None:
        """Initializes the menu's buttons and adds them to it's layout

        Args:
            buttons (dict): the dictionary containing data to be passed to the button constructors
            tabs (QLayout): the window layout which the buttons will connect to
            mode (ColorModes): the current color mode
            slots (dict[str, callable]): dictionary with the functions to be passed to button constructors

        Returns:
            None: initialized sidebar vertical layout is a instance attribute
        """

        

        #main for loop through the buttons dictionary provided
        for index, button in enumerate(buttons):
            position = "default" if index not in [0, len(buttons) - 1] else\
            ("top" if index == 0 else "bottom")

            #the first 3 callables take the same argument
            if not re.match(r".* mode", button["text"]):
                new_button = SidebarButton(
                button['icon'],                                     #button icon
                button['text'],                                     #text under the icon
                partial(slots['default'], tabs, index),             #partial function so it doesn't get called immediately
                mode,                                               #current color mode
                position)                                           #button's position in the toolbar

            else:
                new_button = SidebarButton(
                    button['icon'], 
                    button['text'], 
                    partial(slots['trigger'], self),
                    mode,
                    position)

                self.mode_trigger = new_button                      #create a trigger variable to be accessed from outside the class
                

            self._layout_.addWidget(new_button)                     #add the button to the sidebar's layout
            self.buttons.append(new_button)                         #append to the buttons list (useful when switching color mode)
            
            


        self.SetLayoutSpacing()                                     #align the layout correctly
        
        self.setLayout(self._layout_)                               #set the layout variable as the current layout

        
        


    def SetLayoutSpacing(self):
        """Called inside the InitButtons method, sets the layout spacing and aligns the items correctly"""

        self._layout_.setContentsMargins(0,0,0,200)                 #zero margins
        self._layout_.setSpacing(0)                                 #zero spacing between elements


        for index in range(self._layout_.count()):                  #evenly stretch out all elements    
            self._layout_.setStretch(index, 1)



    def UpdateFonts(self, font):
        """Called inside the settings"""
        for button in self.buttons:
            button.setFont(gui.QFont(font))
