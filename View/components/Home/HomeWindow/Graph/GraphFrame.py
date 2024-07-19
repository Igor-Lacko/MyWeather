"""Contains the main frame for showing the weather graph on the home screen"""
from . import *
from MyWeather.View.Styles.Sheets import StyleSheets
from MyWeather.Init.HomeTabInits import GraphInit
from .GraphLayout import GraphLayout
from PyQt6.QtCore import pyqtSlot
from functools import partial




class GraphFrame(QFrame):
    """Main class for the frame"""


    def __init__(self):
        super().__init__()


        self.setObjectName("GraphFrame")
        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        
        
        (layout := QVBoxLayout()).addLayout(header := GraphInit.GetGraphHeader())
        layout.addLayout(graph := QStackedLayout())

        self.graph = graph
        self.header = header
        self.index = 0                              #initial index
        self.daylist : list[GraphLayout] = []       #for day checking
        self.dummy_widgets : list[QWidget] = []     #dummy widgets which store the graph layouts
        
        layout.setStretch(0,10)
        layout.setStretch(1,90)

        

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.setStyleSheet(self.GetSheet(MODE))

        #connect slots
        self.header.widgets[0].clicked.connect(self.SwitchDayBackward)
        self.header.widgets[2].clicked.connect(self.SwitchDayForward)

        self.InitGraphs()



    def InitGraphs(self):
        """Initializes the 'graph' layout with all days from the forecast"""
        for day in InitWeatherData.forecast.days:
            self.graph.addWidget(dummy := QWidget())
            
            dummy.setLayout(daylist_item := GraphLayout(day, InitWeatherData.forecast.location))                         #NEVERIM ZE TOTO FUNGOVALO WTFFFFFFFFFF
            self.daylist.append(daylist_item)
            self.dummy_widgets.append(dummy)
            
            self.header.widgets[1].menu.currentIndexChanged.connect(daylist_item.SwitchGraph)
            


    def DeleteLayout(self, layout : QLayout):
        """Deletes the layout passed in as an argument"""

        while layout.count():
            if (item := layout.takeAt(0)).widget() is not None:
                item.widget().deleteLater()

            elif item.layout() is not None:     #recursive call if the item at zero is an layout
                self.DeleteLayout(item.layout())

        layout.deleteLater()

        

    
    @pyqtSlot()
    def SwitchDayForward(self):
        """Switches the displayed day to tommorow from the actually displayed\n
        -if at the end of the forecast data starts from it's beginning"""
        
        self.index = self.index + 1 if self.index < (len(self.daylist) - 1) else 0
        self.graph.setCurrentIndex(self.index)
        self.header.widgets[1].ChangeTitle(self.daylist[self.index].date, self.daylist[self.index].location)



    
    @pyqtSlot()
    def SwitchDayBackward(self):
        """Switches the dispayed day to yesterday from the actualkly displayed\n
        -if at the beginning of the forecast data starts drom it's end"""
        
        self.index = self.index - 1 if self.index > 0 else (len(self.daylist) - 1)
        self.graph.setCurrentIndex(self.index)
        self.header.widgets[1].ChangeTitle(self.daylist[self.index].date, self.daylist[self.index].location)

    
    def GetSheet(self, mode : ColorModes):
        """Helper function because i hated doing the mode if-else block for 1000 times

        Args:
            mode (ColorModes): Color mode provided
        """

        return (StyleSheets.dark.GraphFrame if mode == ColorModes.DARK\
                    else StyleSheets.light.GraphFrame).value

    
    def SwitchColorMode(self, mode : ColorModes):
        """On click of the sidebar change mode button

        Args:
            mode (ColorModes): The Color Mode Provided.
        """ 

        self.setStyleSheet(self.GetSheet(mode))

        self.header.SetColor(mode)

        for graph_layout in self.daylist:
            graph_layout.SwitchColorMode(mode)

    



