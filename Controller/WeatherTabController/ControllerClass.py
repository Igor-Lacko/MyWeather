"""Contains the main Weather tab controller class."""
from . import *
from PyQt6.QtCore import QObject, QAbstractAnimation, QTimer, pyqtSignal
from PyQt6.QtWidgets import *
from MyWeather.Init.WeatherInits.OptionMenuInit import OptionMenuParser
from MyWeather.Init.WeatherInits.DataViewInit import GetView, GetSingleGraph
from MyWeather.Model.request import *
from MyWeather.Model.obj import BulkData, Timeline, Realtime, Day
from MyWeather.View.components.Graphs.Container import BaseGraphContainer
from .Animations import *
from .Utilities import *
from .OptionsParse import GetOptions


class WeatherController(QObject):
    """Inherits from QObject for access to signals/slots... etc"""
    fetch_data = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.weather_tab : WeatherTab = None
        self.animations = None
        self.api : str = None
        self.data : Realtime | Timeline | BulkData | Day = None


    def ConnectWeatherTab(self, tab : WeatherTab):
        """Run on app startup, connects the controller and the Weather Tab instance together"""
        self.weather_tab = tab
        self.ConnectSelections()


    def ConnectSelections(self):
        """Connects each selection's button to the 0-->1 stage transition"""
        for selection in self.weather_tab.selections:
            selection.user_submitted.connect(lambda choice: self.StageTransition((0,1), **choice))


    def ResponseSuccess(self, data):
        """Set the stage transition into motion"""
        self.data = data
        self.StageTransition((1,2))




    def GetResponse(self):
        """Calls the worker object which will either return None or a response\n
        - If the operation fails, the controller remains in stage 1 and shows a error popup\n
        - If it succeeds, it will begin the stage transition from 1 to 2"""
        self.fetch_data.emit(GetOptions(self.api, self.weather_tab.menu))


    def SetGraph(self, data : obj.Day):
        """Intermediate function, calls the 2-->3 stage transition with the provided data and locks the stylesheets for the graph options"""
        for selection in self.weather_tab.tabs:
            selection.submitted = True

        self.StageTransition((2,3), **{'data' : data})


    def SetLayoutNextStage(self, stage_pair : tuple=(0,1), **kwargs):
        """Modifies the layout for the next stage

        Args:
            stage_pair (tuple): a pair of (current_stage, next_stage)
        """
        match stage_pair:
            case(0,1): #the first stage transition
                self.weather_tab._layout_.setStretch(0, 30)
                self.weather_tab._layout_.setStretch(2, 5)
                self.weather_tab._layout_.insertWidget(3, menu := OptionMenuParser(self.api, self.weather_tab.color_mode,
                    lambda: self.StageTransition((1,0)), lambda: self.GetResponse())) #the reset/submit button slots
                self.weather_tab.menu = menu
                self.weather_tab.menu.hide()
                self.weather_tab._layout_.setStretch(3, 45)


            case(1,0): #back from second to first
                #remove the menu
                self.weather_tab._layout_.removeWidget(self.weather_tab.menu)
                self.weather_tab.menu.deleteLater()
                self.weather_tab.menu = None

                #adjust the initial stretch before the title and the one after the title
                self.weather_tab._layout_.setStretch(0,5)
                self.weather_tab._layout_.setStretch(2,45)

                #add the layout with api selections
                self.weather_tab._layout_.insertLayout(3, self.weather_tab.selection_layout, 30)

            case(1,2):
                #delete the old option menu
                self.weather_tab._layout_.removeWidget(self.weather_tab.menu)
                self.weather_tab.menu.deleteLater()
                self.weather_tab.menu = None

                #insert the view layout
                self.weather_tab._layout_.insertLayout(3, self.weather_tab.view_layout, 45)

            case(2,3):
                #from the second stage to the final one, so when the graph pickers are clicked and a graph is shown
                #basically just replace one view layout with another

                #first remove all items from the current instance
                ClearLayout(kwargs['old_layout'])

                #remove the old view layout from the weather
                self.weather_tab._layout_.removeItem(kwargs['old_layout'])
                kwargs['old_layout'].deleteLater()

                #reset some instance attributes
                self.weather_tab.tabs = []
                self.weather_tab.return_option = None

                #Insert the new layout into the main one
                self.weather_tab._layout_.insertLayout(3, self.weather_tab.view_layout)

            case(2,0):
                #rearrange spacing
                self.weather_tab._layout_.setStretch(0, 5)
                self.weather_tab._layout_.setStretch(2, 45)

                #free up the graph memotry if a graph is displayed
                if self.weather_tab.graph is not None:
                    self.weather_tab.graph.DeleteGraph()

                #remove all items from the view layout
                ClearLayout(self.weather_tab.view_layout)

                #remove the view layout from the main/parent layout and delete it
                self.weather_tab._layout_.removeItem(self.weather_tab.view_layout)
                self.weather_tab.view_layout.deleteLater()

                #reset instance attributes
                self.weather_tab.tabs = []
                self.weather_tab.return_option = None
                self.weather_tab.graph = None
                self.weather_tab.view_layout = None
                self.api = None
                self.data = None

                #insert the selection layout into the main layout
                self.weather_tab._layout_.insertLayout(3, self.weather_tab.selection_layout, 30)

            case(3,2):
                #basically the same as (2,3), just replaces one view_layout with another and resets some instance attributes

                #remove the matplotlib figure
                self.weather_tab.graph.DeleteGraph()

                #remove all items from the old view_layout
                ClearLayout(kwargs['old_layout'])

                #remove the old layout from the main layout and delete it
                self.weather_tab._layout_.removeItem(kwargs['old_layout'])
                kwargs['old_layout'].deleteLater()

                #reset the graph instance attribute
                self.weather_tab.graph = None

                #insert the new view_layout
                self.weather_tab._layout_.insertLayout(3, self.weather_tab.view_layout, 45)





    def StageTransition(self, stage_pair : tuple, **kwargs):
        """Performs operations needed to move the weather tab to the next stage

        Args:
            stage_pair (tuple): pair of (current_stage, next_stage)
            kwargs (dict): various arguments, such as the API choice string, the pressed button (for the choice animation)... since each transition has different arguments
        """

        match stage_pair:
            case(0,1):
                #----Transition from the first stage to the second----#
                """Hides the three API selections, should be run after the user makes a choice\n
                Runs three animations which validate the choice with a filling effect and remove the elements\n
                The layout immediately after removal looks like this:\n
                    \t-stretch 5\n
                    \t-label 10\n
                    \t-stretch 45\n
                    \t-stretch 10"""

                self.api = kwargs['api'].lower()

                #---Parallel animation groups running at the same time for the movement and fading of the api choices---#
                move_animations = GetParallelGroup([MoveOutAnimation(selection, 2500) for selection in self.weather_tab.selections])
                fade_animations = GetParallelGroup([FadeOutAnimation(selection, 2500) for selection in self.weather_tab.selections])

                #---Title fade animation---#
                title_fade = FadeOutAnimation(self.weather_tab.title, 2000)

                #---A sequential group with those animations running second, and the choice animation running first---#
                self.animations = GetSequentialGroup([ChoiceAnimation(kwargs['button'], 300), GetParallelGroup([move_animations, fade_animations]), title_fade],
                                                        slot=lambda: HideAnimationFinished(self))

                #---Change title text on finish---#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText(f"{self.api.title()} API configuration"))

                self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)


            case(1,0):
                #----Opposite case, transition from the second stage back to the first----#
                self.api = None

                #----Recreate the selection layout----#
                selection_layout = GetSelectionLayout(self.weather_tab)
                self.ConnectSelections()
                self.effects = SetGroupInvisible(self.weather_tab.selections)

                #----Parallel animation groups with the title fading and the option menu sizing in----#
                self.animations = GetParallelGroup([FadeOutAnimation(self.weather_tab.title, 1500),
                                                    SizeInAnimation(self.weather_tab.menu, 700, self.weather_tab)],
                                                    slot=lambda: self.SetLayoutNextStage((1,0), **{'selection_layout' : selection_layout}))

                #----Change title text on finish----#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText("Choose your mode."))

                #wait 100 ms and show the options and the title
                self.animations.finished.connect(lambda: QTimer.singleShot(100, lambda: ShowTitleSelections(self)))

                self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)


            case(1,2):
                #----Transition from the second stage to the third----#

                #----Set the layout for next stage with the view layout as the keyword argument----#
                GetView(self.data, self.api, self.weather_tab)

                #----If a multiple day choice is made, hide the tabs until their animation starts----#
                if len(self.weather_tab.tabs) != 0:
                    self.effects = SetGroupInvisible(self.weather_tab.tabs)

                #----Hide the title and delete the option menu----#
                self.animations = GetParallelGroup([SizeInAnimation(self.weather_tab.menu, 700, self.weather_tab),
                                                    FadeOutAnimation(self.weather_tab.title, 1000)],
                                                    slot=lambda: self.SetLayoutNextStage((1,2)))

                #----Set the title text accordingly to the API type, location, and length----#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText(GetTitle(self.data, self.api)))

                #----Perform the animations which show the data displayed----#
                self.animations.finished.connect(lambda: QTimer.singleShot(200, lambda: ShowViewTitle(self)))

                #----Connect the new view to the reverse stage transition----#
                self.animations.finished.connect(lambda: ConnectReturnButton(self))

                #----Connect the graph pickers (if they exist) to the final stage transition----#
                if len(self.weather_tab.tabs) != 0:
                    self.animations.finished.connect(lambda: ConnectGraphPickers(self))

                self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)

            case(2,3):
                #----Transition to the final stage, when a graph is picked from multiple choices. Only Forecast/History API----#

                #----Make a copy of the current view layout since GetSingleGraph replaces it----#
                old_layout = self.weather_tab.view_layout

                #----Make a single graph in the view layout----#
                GetSingleGraph(kwargs['data'], self.api, self.weather_tab)

                #----Connect the graph's reset button to the reverse stage transition----#
                self.weather_tab.graph.header.reset_button.clicked.connect(lambda: self.StageTransition((3,2)))

                #----Create animations that move out/fade the selections and fade the title out and back in----#
                self.animations = GetParallelGroup(
                    [MoveOutAnimation(tab, 1000) for tab in self.weather_tab.tabs]
                    +
                    [FadeOutAnimation(tab, 1000) for tab in self.weather_tab.tabs]
                    +
                    [FadeOutAnimation(self.weather_tab.title, 1000)],
                    slot=lambda: self.SetLayoutNextStage((2,3), **{'old_layout' : old_layout}))

                #----Change the title as the animations finish----#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText(
                    GetTitle(self.data, self.api, one_day=True, date_str=kwargs['data'].date_str)))

                #----Show the graph a while after the animations finish----#
                self.animations.finished.connect(lambda: QTimer.singleShot(100, lambda: ShowGraph(self)))

                self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)


            case(2,0):
                #----Transition from the third stage to the start, used when the return button on the realtime graph is clicked or the return option among graph pickers----#
                
                #----Recreate the API selection layout----#
                selection_layout = GetSelectionLayout(self.weather_tab)
                self.ConnectSelections()

                #----Set the selections invisible until their animation begins----#
                self.effects = SetGroupInvisible(self.weather_tab.selections)

                #----Create animations depending on the current view----#
                if self.weather_tab.return_option is not None:
                    self.animations = GetParallelGroup(
                        [MoveOutAnimation(tab, 1000) for tab in self.weather_tab.tabs]
                        +
                        [FadeOutAnimation(tab, 1000) for tab in self.weather_tab.tabs]
                        +
                        [FadeOutAnimation(self.weather_tab.title, 1000)],
                        slot=lambda: self.SetLayoutNextStage((2,0)))
                    
                    for selection in self.weather_tab.tabs:         #also lock the stylesheet for the other selections
                        if selection is not self.weather_tab.return_option:
                            selection.submitted = True


                elif self.weather_tab.graph is not None:
                    self.animations = GetParallelGroup(
                        [SizeInAnimation(self.weather_tab.graph, 1000, self.weather_tab),
                        FadeOutAnimation(self.weather_tab.title, 1000)],
                        slot=lambda: self.SetLayoutNextStage((2,0))
                    )

                else:
                    raise NameError("Neither graph nor return option exist")

                #----Restore initial text and begin the selection animation after a while----#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText("Choose your mode"))
                self.animations.finished.connect(lambda: QTimer.singleShot(100, lambda: ShowTitleSelections(self)))

                self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)

            case(3,2):
                #----Transition from the final stage (one graph) to the previous where a selection of graphs is displayed----#

                #----Again, make a copy of the old view layout----#
                old_layout = self.weather_tab.view_layout

                #----Create a new view_layout----#
                GetView(self.data, self.api, self.weather_tab)

                #----Hide the selections until their animation starts----#
                self.effects = SetGroupInvisible(self.weather_tab.tabs)

                #----Create animations that size in the graph and fade the title----#
                self.animations = GetParallelGroup([
                    SizeInAnimation(self.weather_tab.graph, 1000, self.weather_tab),
                    FadeOutAnimation(self.weather_tab.title, 1000),
                ], slot=lambda: self.SetLayoutNextStage((3,2), **{'old_layout' : old_layout}))

                #----Change the title on animation finish and show the title again after a while----#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText(GetTitle(self.data, self.api)))
                self.animations.finished.connect(lambda: QTimer.singleShot(100, lambda: ShowViewTitle(self)))

                #----Connect the return option and the other graph pickers----#
                self.animations.finished.connect(lambda: ConnectReturnButton(self))
                self.animations.finished.connect(lambda: ConnectGraphPickers(self))

                self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)



#----END OF THE CONTROLLER CLASS, STAGE OPERATIONS PUT HERE TO AVOID CIRCULAR IMPORTS----#






#----------STAGE 1 OPERATIONS----------#

def HideAnimationFinished(controller : WeatherController):
        """End of the animation that hides the API selections. Removes all items from the layout (including QSpacerItems)"""

        #reset the effects attribute
        ClearEffect(controller.weather_tab.selections)
        controller.effects = []

        #remove all items from the layout
        ClearLayout(controller.weather_tab.selection_layout)

        #remove the layout from ther main/parent layout and delete it
        controller.weather_tab._layout_.removeItem(controller.weather_tab.selection_layout)
        controller.weather_tab.selection_layout.deleteLater()
        controller.weather_tab.selection_layout = None
        controller.weather_tab.selections = []

        controller.SetLayoutNextStage((0,1))
        QTimer.singleShot(100, lambda: ShowTitleMenu(controller))


def ShowTitleSelections(controller : WeatherController):
        """Simillar to ShowTitleMenu, expect in the reverse stage transition"""
        show_animations = GetParallelGroup([MoveInAnimation(selection, 1500) for selection in controller.weather_tab.selections] + 
                                            [FadeInAnimation(selection, 1500) for selection in controller.weather_tab.selections])

        controller.animations = GetParallelGroup([FadeInAnimation(controller.weather_tab.title, 2500), show_animations], 
                                                    slot=lambda: ClearEffect(controller.weather_tab.selections))

        controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)








#----------STAGE 2 OPERATIONS----------#
def ShowTitleMenu(controller : WeatherController):
        """Shows the title and the API config menu"""
        controller.weather_tab.menu.setGraphicsEffect(invisible := QGraphicsOpacityEffect(controller.weather_tab.menu))
        invisible.setOpacity(0)         #use a graphics effect to keep the menu invisible
        controller.animations = GetParallelGroup([FadeInAnimation(controller.weather_tab.title, 500), 
                                                    SizeOutAnimation(controller.weather_tab.menu, 500, controller.weather_tab)], 
                                                    slot=lambda: ClearEffect([controller.weather_tab.menu]))

        controller.animations.stateChanged.connect(lambda state: ShowIfStarted(state, [invisible]))    
        controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)









#----------STAGE 3 OPERATIONS----------#
def ShowViewTitle(controller : WeatherController):
    """Shows the view depending on the controller API (so either a graph, or the tabs to select a graph)\n
    - Also, just like with all stage transitions, fades the title back into view"""
    #Show the title first
    title_animation = FadeInAnimation(controller.weather_tab.title, 1000)

    #create a data show animation depending on the API type
    if controller.api == 'realtime' or len(controller.data.days) == 1:
        controller.animations = GetParallelGroup([title_animation, SizeOutAnimation(controller.weather_tab.graph, 500, controller.weather_tab)])
        controller.animations.stateChanged.connect(lambda state: ShowIfStarted(state, [controller.weather_tab.graph.graphicsEffect()]))
        controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)

    else:
        #create a MoveInAnimation group for the graph pickers and a fade animation for the title
        controller.animations = GetParallelGroup([
            FadeInAnimation(controller.weather_tab.title, 1000),
            show_animations := GetParallelGroup([MoveInAnimation(selection, 1500) for selection in controller.weather_tab.tabs] + [FadeInAnimation(selection, 1500) for selection in controller.weather_tab.tabs])])

        #make the graph pickers visible upon starting the show animations and clear the effects upon their end
        controller.animations.finished.connect(lambda: ClearEffect(controller.weather_tab.tabs))
        controller.animations.finished.connect(lambda: SelectionsSet(controller))
        controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)



def ShowGraph(controller : WeatherController):
    """Special case of ShowViewTitle, used when a graph needs to be shown"""
    controller.animations = GetParallelGroup([FadeInAnimation(controller.weather_tab.title, 1000), SizeOutAnimation(controller.weather_tab.graph, 1000, controller.weather_tab)])
    controller.animations.stateChanged.connect(lambda state: ShowIfStarted(state, [controller.weather_tab.graph.graphicsEffect()]))
    controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)


def ConnectReturnButton(controller : WeatherController):
    """Connects return button for either graph or the graph pickers to the 2-->0 stage transition

    Args:
        controller (WeatherController): The controller instance, has access to the weather tab
    """

    if controller.weather_tab.return_option is not None:
        controller.weather_tab.return_option.button.clicked.connect(lambda: controller.StageTransition((2,0)))

    elif controller.weather_tab.graph is not None:
        controller.weather_tab.graph.header.reset_button.clicked.connect(lambda: controller.StageTransition((2,0)))

    else:
        raise NameError("Neither graph button nor tab return button exist")



def ConnectGraphPickers(controller : WeatherController):
    """Connects all the options when picking from days to show a graph for to actually show the graph

    Args:
        controller (WeatherController): The controller instance, has access to both the weather window/tab and the data to be displayed
    """

    if len(controller.weather_tab.tabs) == 0:
        raise ValueError("Error: Cannot connect the graph selections since they don't exist")

    for selection in controller.weather_tab.tabs[1:]:     #skip the first item since it's the return option
        selection.clicked.connect(controller.SetGraph)



def SelectionsSet(controller : WeatherController):
    """Changes the selection's Set state to True so the StyleSheet can change"""
    for selection in controller.weather_tab.tabs[1:]:
        selection.set = True