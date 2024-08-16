"""Module containing the QFrame subclass (GraphContainer) which contains the entire Header + Graph and MultiGraphContainer (which contains multiple StackedGraphLayouts)"""
from . import *
from PyQt6.QtCore import pyqtSlot
from .Header import BaseGraphHeader, ExtendedGraphHeader
from .StackedGraphLayout import StackedGraphLayout
from MyWeather.View.StyleSheets.Graph import Dark, Light
from MyWeather.View.utils.enumerations import ColorModes #absolute import to avoid enum comparision issues
from MyWeather.Model.obj import Timeline


class BaseGraphContainer(QFrame):
    """Graph container class"""

    def __init__(self, data : Day | Timeline, mode : ColorModes, api : str):
        """Graph constructor

        Args:
            data (Day): Weather data, passed to the graph header/body
            mode (ColorModes): Initial color mode, kept as an instance attribute
            api (str): What API does the data represent between Realtime/Forecast/History
        """
        super().__init__()
        self.setObjectName("graph_frame")

        #instance attributes
        self.color_mode = mode
        self.data = data
        self.api = api

        #initialize layout/spacing
        self._layout_ = QVBoxLayout()
        self._layout_.setSpacing(0)
        self._layout_.setContentsMargins(0,0,0,0)
        self.setLayout(self._layout_)

        #initialize/add header
        self._layout_.addWidget(self.AddHeader(), stretch=10)

        #initialize/add graphs
        self._layout_.addLayout(self.AddGraphs(), stretch=90)

        #connect needed slots
        self.ConnectGraphSwitcher()

        #initial sheet
        self.setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).GraphFrame)



    def AddHeader(self) -> BaseGraphHeader:
        """Base method returning a graph header object\n
        - Kept as a method to make graph header inheritance possible

        Returns:
            BaseGraphHeader: Initialized graph header
        """

        self.header = BaseGraphHeader(**{
            'date'      :   self.data.date_str,
            'location'  :   self.data.location,
            'api'       :   self.api
        })
        return self.header



    def AddGraphs(self) -> StackedGraphLayout:
        """Base method returning ONE StackedGraphLayout object
        - Also kept as an method instead of being used on init to make inheritance possible (with ExtendedGraphContainer overriding this)

        Returns:
            StackedGraphLayout: Initialized StackedLayout, each containing one graph
        """

        self.graphs = StackedGraphLayout(self.data, self.data.location)
        return self.graphs



    def ConnectGraphSwitcher(self):
        """Connects the graph's combobox to switch between the graphs (at least in the base class)"""
        self.header.menu.currentIndexChanged.connect(self.graphs.SwitchGraph)



    def SwitchColorMode(self):
        """Switches the color scheme for the graph, the base version just switches the style sheet and one graph"""
        self.setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).GraphFrame)
        self.color_mode = ColorModes.DARK if self.color_mode == ColorModes.LIGHT else ColorModes.LIGHT
        self.graphs.SwitchColorMode(self.color_mode)






class ExtendedGraphContainer(BaseGraphContainer):
    """Extended graph container which contains a extended header and multiple StackedGraphLayout objects"""
    def __init__(self, data : Timeline, mode : ColorModes, api : str) -> None:
        self.dummy_widgets : list[QWidget] = []
        self.layouts : list[StackedGraphLayout] = []
        self.index = 0 #index of the DAY in the list, not the graphs themselves
        super().__init__(data, mode, api)


        #connect the header's buttons to the day switcher
        self.header.left_button.clicked.connect(self.SwitchDayBackward)
        self.header.right_button.clicked.connect(self.SwitchDayForward)





    def AddHeader(self) -> ExtendedGraphHeader:
        """Override of the superclass AddHeader method, returns a ExtendedGraphHeader instead

        Returns:
            ExtendedGraphHeader: Initialized header
        """

        self.header = ExtendedGraphHeader(**{
            'date'          :   self.data.days[0].date_str,
            'location'      :   self.data.location,
            'api'           :   self.api,
            'color_mode'    :   self.color_mode
        })
        return self.header



    def AddGraphs(self) -> QStackedLayout:
        """Override of the AddGraphs method for the base container

        Returns:
            QStackedLayout: A QStackedLayout where each item has a QWidget which has a GraphStackedLayout set onto itself
        """
        self.graphs = QStackedLayout()

        #add a new graph layout for each day in the list
        for day in self.data.days:
            (dummy := QWidget()).setLayout(graph := StackedGraphLayout(day, self.data.location))
            self.graphs.addWidget(dummy)
            self.layouts.append(graph)
            self.dummy_widgets.append(dummy)    #TODO: evaluate whether this isn't useless later on tbh

        return self.graphs



    def ConnectGraphSwitcher(self):
        """Override of the graph switcher, does the same as in the base class except for each StackedGraphLayout"""
        for layout in self.layouts:
            self.header.menu.currentIndexChanged.connect(layout.SwitchGraph)



    @pyqtSlot()
    def SwitchDayForward(self):
        """Header's right button slot. Switches the current StackedGraphLayout one forward, if at the end switches back to the first"""
        self.index = (self.index + 1 if (self.index < len(self.data.days) - 1) else 0)
        self.graphs.setCurrentIndex(self.index)
        self.header.ChangeTitle(self.data.days[self.index].date_str, self.data.location)



    @pyqtSlot()
    def SwitchDayBackward(self):
        """Header's left button slot. Switches the current StackedGraphLayout to one back, if already at the start switches to the last one in the list"""
        self.index = (self.index - 1 if self.index > 0 else (len(self.data.days) - 1))
        self.graphs.setCurrentIndex(self.index)



    def SwitchColorMode(self):
        """Color mode switcher, does the same as the base version but for multiple GraphStackedLayout objects"""
        self.color_mode = ColorModes.DARK if self.color_mode == ColorModes.LIGHT else ColorModes.LIGHT
        self.setStyleSheet((Dark if self.color_mode == ColorModes.DARK else Light).GraphFrame)

        self.header.SetButtonIcons(self.color_mode)

        for layout in self.layouts:
            layout.SwitchColorMode(self.color_mode)



