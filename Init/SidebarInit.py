import re
from MyWeather.View.components.Sidebar import Sidebar, SidebarButton
from MyWeather.View.utils.enumerations import ColorModes, Colors
from MyWeather.Constdata.SidebarButtons import buttons
from MyWeather.Constdata.Mode import MODE

def GetSidebar() -> Sidebar.Sidebar:
    """Initializes the sidebar at the beginning of the app"""
    DEFAULT_COLOR = Colors.CoolGrey if MODE == ColorModes.DARK\
    else Colors.OffWhite

    sidebar = Sidebar.Sidebar(DEFAULT_COLOR)
    InitSidebarButtons(buttons, MODE, sidebar)

    return sidebar



def InitSidebarButtons(buttons : dict, mode : ColorModes, sidebar : Sidebar.Sidebar) -> None:
        """Initializes the menu's buttons and adds them to it's layout

        Args:
            buttons (dict): the dictionary containing data to be passed to the button constructors
            mode (ColorModes): the current color mode

        Returns:
            None: initialized sidebar vertical layout is a instance attribute
        """

        

        #main for loop through the buttons dictionary provided
        for index, button in enumerate(buttons):
            position = "default" if index not in [0, len(buttons) - 1] else\
            ("top" if index == 0 else "bottom")


            #the first 3 callables take the same argument
            if not re.match(r".* mode", button["text"]):
                new_button = SidebarButton.SidebarButton(
                button['icon'],                                     #button icon
                button['text'],                                     #text under the icon
                mode,                                               #current color mode
                index,                                              #button's index 
                position=position)                                  #button's position in the toolbar

            else:
                new_button = SidebarButton.SidebarButton(
                    button['icon'], 
                    button['text'], 
                    mode,
                    index,
                    position)

                sidebar.mode_trigger = new_button                   #create a trigger variable to be accessed from outside the class
                sidebar.mode_trigger.clicked.connect

            sidebar._layout_.addWidget(new_button)                  #add the button to the sidebar's layout
            sidebar.buttons.append(new_button)                      #append to the buttons list (useful when switching color mode)
            
            


        sidebar.SetLayoutSpacing()                                  #align the layout correctly
        
        sidebar.setLayout(sidebar._layout_)                         #set the layout variable as the current layout