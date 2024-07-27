"""Contains the main Weather tab controller class."""
from . import *
from PyQt6.QtCore import QObject, QPropertyAnimation, QPoint, QEasingCurve, QParallelAnimationGroup, QAbstractAnimation, QSequentialAnimationGroup
from functools import partial
from PyQt6.QtWidgets import *
from MyWeather.Init.WeatherInits.ItemLayout import layout as structure
from MyWeather.Init.WeatherInits.ItemsInit import ParseItems


class WeatherController(QObject):
    """Inherits from QObject for access to signals/slots... etc"""

    def __init__(self):
        super().__init__()
        self.animations = None




    def ConnectWeatherTab(self, tab : WeatherTab):
        """Run on app startup, connects the controller and the Weather Tab instance together"""
        self.weather_tab = tab

        for selection in self.weather_tab.selections:
            selection.user_submitted.connect(lambda index: self.HideAPISelections(index))


    def HideAPISelections(self, index : int):
        """Hides the three API selections, should be run after the user makes a choice\n
        Runs three animations which validate the choice with a filling effect and remove the elements\n
        The layout immediately after removal looks like this:\n
        \t-stretch 5\n
        \t-label 10\n
        \t-stretch 45\n
        \t-stretch 10"""

        self.animations = QSequentialAnimationGroup()
        self.animations.finished.connect(self.HideAnimationFinished)

        #---Starting animation that fills the user's choice with green---#
        (choice_animation := QPropertyAnimation(self.weather_tab.selections[index].button, b"filled_part"))
        choice_animation.setDuration(1000)
        choice_animation.setStartValue(0)
        choice_animation.setEndValue(100)


        #---Parallel animation groups running at the same time---#
        move_animations = QParallelAnimationGroup()
        fade_animations = QParallelAnimationGroup()

        for selection in self.weather_tab.selections:
            #---Animation that moves the selection out of the screen---#
            (move_animation := QPropertyAnimation(selection, b"pos"))
            move_animation.setDuration(2500)
            move_animation.setEndValue(QPoint(selection.x(), self.weather_tab.height()))
            move_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
            move_animations.addAnimation(move_animation)


            #---Animation that fades the selection out of vision---#
            selection.setGraphicsEffect(fade := QGraphicsOpacityEffect(selection))
            fade.setOpacity(1)              #so that the effect doesn't show immediately
            (fade_animation := QPropertyAnimation(fade, b"opacity")).setDuration(2500)
            fade_animation.setStartValue(1)
            fade_animation.setEndValue(0)
            fade_animations.addAnimation(fade_animation)


        #---Add the animations in order to the queue---#
        (hide_animations := QParallelAnimationGroup()).addAnimation(move_animations)
        hide_animations.addAnimation(fade_animations)

        self.animations.addAnimation(choice_animation)
        self.animations.addAnimation(hide_animations)
        self.animations.start(policy=QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)



    def HideAnimationFinished(self):
        """End of the animation that hides the API selections. Removes all items from the layout (including QSpacerItems)"""
        while self.weather_tab.selection_layout.count():
            item = self.weather_tab.selection_layout.takeAt(0)

            if type(item) != QSpacerItem:
                item.widget().deleteLater()

            else:
                del(item)

        self.weather_tab._layout_.removeItem(self.weather_tab.selection_layout)
        self.weather_tab.selection_layout.deleteLater()
        self.weather_tab.selection_layout = None
        self.weather_tab.selections = []


        self.SetLayoutApiChosen()


    def ShowApiSelections(self):
        self.weather_tab.selection_layout = QHBoxLayout()
        self.weather_tab._layout_.insertLayout(3, self.weather_tab.selection_layout, 30)

        #find the selection layout among the entire page layout
        for item in structure:
            if item['type'] == "layout":
                selection_layout = item['items']
                break

        ParseItems(selection_layout, self.weather_tab.selection_layout, self.weather_tab)


    def SetLayoutApiChosen(self):
        """Handles the restructuring of the window after the user makes a API choice and the animations finish running"""
        self.weather_tab._layout_.takeAt(3)
        self.weather_tab._layout_.setStretch(2, 10)

        """Now the window is structured like this:
            stretch 5
            label 10
            stretch 10, so 75% of the screen is free"""

        self.weather_tab._layout_.addLayout(menu_layout := QHBoxLayout(), stretch=65)
        self.weather_tab.menu_layout = menu_layout

        self.weather_tab._layout_.addStretch(10) #fill out the remaining space on the screen
        self.ShowMenu()


    def ShowMenu(self, api_choice : str = "realtime"):
        raise NotImplementedError("TURURURURU")


