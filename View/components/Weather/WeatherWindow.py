from . import *
from MyWeather.View.utils.enumerations import ColorModes
from MyWeather.View.StyleSheets.WeatherTab import Dark, Light
from MyWeather.Init.WeatherInits import ItemsInit, ItemLayout
from .WeatherChooseButton import TextImageButton
from ..Graphs.GraphPicker import GraphPicker, ReturnOption
from ..Graphs.Container import BaseGraphContainer
from .Title import Title
from .OptionsMenu import OptionMenu

class WeatherTab(QFrame):
    """Weather tab class"""
    def __init__(self):
        super().__init__()
        self.setObjectName("weathertab")
        self.color_mode = MODE

        self.selections : list[TextImageButton] = []
        self.selection_layout : QLayout = None      #contains the 3 API choices in a horizontal layout

        self.menu : OptionMenu = None               #the menu instance

        self.view_layout : QLayout = None           #The layout containing the data views

        self.graph : BaseGraphContainer = None      #the currently displayed graph (a singleton in the case of realtime)
        self.tabs : list[GraphPicker] = []          #tabs (graph pickers)

        self.return_option : ReturnOption = None    #the return option among the tabs

        self.title : Title = None
        self.InitLayout() #stretches at index 0, 2 and 4 on init, the item layout is at index 3
        self.SetColorMode(self.color_mode, False)



    @pyqtSlot(ColorModes)
    def SetColorMode(self, mode : ColorModes, change : bool = True):
        """Swaps the background image of the weather tab and updates it's components' color scheme\n
        -If change is passed as True, switches the self.color_mode to the opposite (used when the mode is switched by the app's Sidebar)"""
        self.setStyleSheet(self.GetStyleSheet(mode))

        #set a style sheet to the menu's option popups, if the menu does currently exist
        if self.menu is not None: 
            self.menu.SetColorMode(mode)

        #simillarly do the same for a graph if it's being displayed
        if self.graph is not None:  
            self.graph.SwitchColorMode()

        #finally, do the same for the graph picker widgets if they exist
        if len(self.tabs) != 0:
            for tab in self.tabs:
                tab.SwitchColorMode()

        if change:
            self.color_mode = ColorModes.DARK if self.color_mode != ColorModes.DARK else ColorModes.LIGHT


    def GetStyleSheet(self, mode : ColorModes):
        """Returns the WeatherTabWindow style sheet from the given color mode"""
        return (Dark if mode == ColorModes.DARK else Light).WeatherTabWindow


    def InitLayout(self):
        """Initializes the weather window structure"""

        #set all spacing/margins to 0 for customized stretch adding
        (layout := QVBoxLayout()).setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self._layout_ = layout

        ItemsInit.ParseItems(ItemLayout.layout, self._layout_, self)
        self.setLayout(self._layout_)

    def UpdateFonts(self, font : str):
        for item in self.selections:
            if type(item) == QLabel:
                item.setFont(QFont(font, pointSize=40))

            else:
                item.title.setFont(QFont(font, pointSize=20))
                item.description.setFont(QFont(font, pointSize=15))