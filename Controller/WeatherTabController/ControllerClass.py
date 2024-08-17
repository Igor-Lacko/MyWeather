"""Contains the main Weather tab controller class."""
from . import *
from PyQt6.QtCore import QObject, QAbstractAnimation, QTimer, pyqtSignal
from PyQt6.QtWidgets import *
from MyWeather.Init.WeatherInits.OptionMenuInit import OptionMenuParser
from MyWeather.Model.request import *
from MyWeather.Model.obj import BulkData, Timeline, Realtime
from MyWeather.View.components.DataViews.GraphView.Container import BaseGraphContainer
from .Animations import *
from .Utilities import *
from .OptionsParse import GetOptions


class WeatherController(QObject):
    """Inherits from QObject for access to signals/slots... etc"""
    fetch_data = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.animations = None
        self.stage = 0
        self.api : str = None
        self.data : Realtime | Timeline | BulkData = None


    def ConnectWeatherTab(self, tab : WeatherTab):
        """Run on app startup, connects the controller and the Weather Tab instance together"""
        self.weather_tab = tab
        self.ConnectSelections()


    def ConnectSelections(self):
        """Connects each selection's button to the 0-->1 stage transition"""
        for selection in self.weather_tab.selections:
            selection.user_submitted.connect(lambda choice: self.StageTransition((0,1), **choice))


    def ResponseSuccess(self, data):
        self.data = data
        self.StageTransition(1,2)




    def GetResponse(self):
        """Calls the worker object which will either return None or a response\n
        - If the operation fails, the controller remains in stage 1 and shows a error popup\n
        - If it succeeds, it will begin the stage transition from 1 to 2"""
        self.fetch_data.emit(GetOptions(self.api.lower(), self.weather_tab.menu))



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
                self.weather_tab._layout_.insertLayout(3, kwargs['selection_layout'], 30)



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

                self.api = kwargs['api']

                #---Parallel animation groups running at the same time for the movement and fading of the api choices---#
                move_animations = GetParallelGroup([MoveOutAnimation(selection, 2500) for selection in self.weather_tab.selections])
                fade_animations = GetParallelGroup([FadeOutAnimation(selection, 2500) for selection in self.weather_tab.selections])

                #---Title fade animation---#
                title_fade = FadeOutAnimation(self.weather_tab.title, 2000)

                #---A sequential group with those animations running second, and the choice animation running first---#
                self.animations = GetSequentialGroup([ChoiceAnimation(kwargs['button'], 300), GetParallelGroup([move_animations, fade_animations]), title_fade],
                                                        slot=lambda: HideAnimationFinished(self))

                #---Change title text on finish---#
                self.animations.finished.connect(lambda: self.weather_tab.title.setText(f"{self.api} API configuration"))

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
                raise NotImplementedError("Next on the TODO list!")


#----END OF THE CONTROLLER CLASS, STAGE OPERATIONS PUT HERE TO AVOID CIRCULAR IMPORTS----#






#----------STAGE 1 OPERATIONS----------#

def HideAnimationFinished(controller : WeatherController):
        """End of the animation that hides the API selections. Removes all items from the layout (including QSpacerItems)"""
        ClearEffect(controller.weather_tab.selections)
        while controller.weather_tab.selection_layout.count():
            item = controller.weather_tab.selection_layout.takeAt(0)

            if type(item) != QSpacerItem:
                item.widget().deleteLater()

            else:
                del(item)

        controller.weather_tab._layout_.removeItem(controller.weather_tab.selection_layout)
        controller.weather_tab.selection_layout.deleteLater()
        controller.weather_tab.selection_layout = None
        controller.weather_tab.selections = []

        controller.SetLayoutNextStage((0,1))
        QTimer.singleShot(100, lambda: ShowTitleMenu(controller))


def ShowTitleSelections(controller : WeatherController):
        """Simillar to ShowTitleMenu, expect in the reverse stage transition"""
        show_animations = GetParallelGroup([MoveInAnimation(selection, 1500) for selection in controller.weather_tab.selections])
        show_animations.stateChanged.connect(lambda state: ShowIfStarted(state, controller.effects))
        controller.animations = GetParallelGroup([FadeInAnimation(controller.weather_tab.title, 2500), show_animations], slot=lambda: ClearEffect(controller.weather_tab.selections))
        controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)








#----------STAGE 2 OPERATIONS----------#



def ShowTitleMenu(controller : WeatherController):
        """Shows the title and the API config menu"""
        controller.weather_tab.menu.setGraphicsEffect(invisible := QGraphicsOpacityEffect(controller.weather_tab.menu))
        invisible.setOpacity(0)         #use a graphics effect to keep the menu invisible
        controller.animations = GetParallelGroup([FadeInAnimation(controller.weather_tab.title, 500), SizeOutAnimation(controller.weather_tab.menu, 500, controller.weather_tab)], 
                                                    slot=lambda: ClearEffect([controller.weather_tab.menu]))
        controller.animations.stateChanged.connect(lambda state: ShowIfStarted(state, [invisible]))    
        controller.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)