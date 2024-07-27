from . import *
from MyWeather.View.utils.enumerations import ColorModes
from MyWeather.View.Styles.Sheets import StyleSheets
from MyWeather.Init.WeatherInits import ItemsInit, ItemLayout
from .WeatherChooseButton import TextImageButton

class WeatherTab(QFrame):
    """Weather tab class"""
    def __init__(self):
        super().__init__()
        self.setObjectName("weathertab")
        self.color_mode = MODE

        self.selections : list[TextImageButton] = []
        self.selection_layout : QLayout = None      #contains the 3 API choices in a horizontal layout

        self.menu_layout : QLayout = None           #contains the menu that appears after the user makes a choice 

        self.title = None
        self.InitLayout() #stretches at index 0, 2 and 4 on init, the item layout is at index 3
        self.SetColorMode(self.color_mode)



    @pyqtSlot(ColorModes)
    def SetColorMode(self, mode : ColorModes, change : bool = False):
        """Swaps the background image of the weather tab and updates it's components' color scheme\n
        -If change is passed as True, switches the self.color_mode to the opposite (used when the mode is switched by the app's Sidebar)"""
        self.setStyleSheet(self.GetStyleSheet(mode))

        if change:
            self.color_mode = ColorModes.DARK if self.color_mode != ColorModes.DARK else ColorModes.LIGHT


    def GetStyleSheet(self, mode : ColorModes):
        """Returns the WeatherTabWindow style sheet from the given color mode"""
        return (StyleSheets.dark if mode == ColorModes.DARK else StyleSheets.light).WeatherTabWindow.value


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