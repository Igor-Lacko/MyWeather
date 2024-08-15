"""Contains the animation for the weather tab's components"""
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QParallelAnimationGroup, QAbstractAnimation, QSequentialAnimationGroup, QRect, QTimer
from . import *

def GetParallelGroup(animations : list[QAbstractAnimation], slot=None) -> QParallelAnimationGroup:
    """Returns a parallel animation group. If a slot is passed, connect's the animation's end to it"""
    group = QParallelAnimationGroup()

    for animation in animations:
        group.addAnimation(animation)

    if slot is not None:
        group.finished.connect(slot)

    return group


def GetSequentialGroup(animations : list[QAbstractAnimation], slot=None) -> QSequentialAnimationGroup:
    """Returns a sequential animation group. If a slot is passed, connect's the animation's end to it"""
    group = QSequentialAnimationGroup()

    for animation in animations:
        group.addAnimation(animation)

    if slot is not None:
        group.finished.connect(slot)

    return group



def ChoiceAnimation(widget : QWidget, duration : int) -> QPropertyAnimation:
    """Animation that fills a widget with a filled_part property with color according to it's paintEvent"""
    (choice_animation := QPropertyAnimation(widget, b"filled_part"))
    choice_animation.setDuration(duration)
    choice_animation.setStartValue(0)
    choice_animation.setEndValue(100)

    return choice_animation



def MoveOutAnimation(widget : QWidget, duration : int) -> QPropertyAnimation:
    """Animation that moves a widget out of screen controlling it's pos property"""
    (move_animation := QPropertyAnimation(widget, b"pos")).setDuration(duration)
    move_animation.setEndValue(QPoint(widget.x(), widget.parentWidget().parentWidget().height()))
    move_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

    return move_animation


def MoveInAnimation(widget : QWidget, duration : int) -> QPropertyAnimation:
    """Opposite of MoveOutAnimation, moves a widget into position from the bottom of the screen"""
    (move_animation := QPropertyAnimation(widget, b"pos")).setDuration(duration)
    move_animation.setStartValue(QPoint(widget.x(), widget.parentWidget().parentWidget().height()))
    move_animation.setEndValue(QPoint(widget.x(), widget.y()))
    move_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

    return move_animation


def FadeOutAnimation(widget : QWidget, duration : int) -> QPropertyAnimation:
    """Animation that fades a widget until it isn't visible"""

    #set a effect to the widget if it isn't there already
    if widget.graphicsEffect() is None:
        fade = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(fade)

    else:
        fade = widget.graphicsEffect()

    fade.setOpacity(1)              #so that the effect doesn't show immediately
    (fade_animation := QPropertyAnimation(fade, b"opacity")).setDuration(duration)
    fade_animation.setStartValue(1)
    fade_animation.setEndValue(0)

    return fade_animation


def FadeInAnimation(widget : QWidget, duration : int) -> QPropertyAnimation:
    """Opposite of FadeOutAnimation, fades a widget in until it's fully visible"""

    #set a effect to the widget if it isn't there already
    if widget.graphicsEffect() is None:
        fade = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(fade)

    else:
        fade = widget.graphicsEffect()

    fade.setOpacity(0)              #so that the effect doesn't show immediately
    (fade_animation := QPropertyAnimation(fade, b"opacity")).setDuration(duration)
    fade_animation.setStartValue(0)
    fade_animation.setEndValue(1)

    return fade_animation


def SizeOutAnimation(widget : QWidget, duration : int, parent : QWidget) -> QPropertyAnimation:
    """Stretches a widget from the middle out until it has it's full size"""
    widget.show()

    #----Get the widget midpoint and top left coordinates----#
    midpoint = widget.mapTo(parent, QPoint(parent.width() // 2, parent.height() // 2))
    topleft = widget.mapTo(parent, QPoint(0, 0))

    #----Inititalize the animation and it's duration----#
    (size_out_animation := QPropertyAnimation(widget, b"geometry")).setDuration(duration)

    #----Pass the old size and new size to the animation----#
    size_out_animation.setStartValue(QRect(midpoint.x(), midpoint.y(), 0, 0))
    size_out_animation.setEndValue(QRect(topleft.x(), topleft.y(), widget.width(), widget.height()))

    return size_out_animation


def SizeInAnimation(widget : QWidget, duration : int, parent : QWidget) -> QPropertyAnimation:
    """Opposite of SizeOutAnimation, stretches a widgit into itself until it's not visible"""

    #----Get the widget midpoint/topleft coordinate (so the animation's finishing/starting point)----#
    midpoint = widget.mapTo(parent, QPoint(parent.width() // 2, parent.height() // 2))
    topleft = widget.mapTo(parent, QPoint(0, 0))

    #----Initialize the animation and it's duration----#
    (size_in_animation := QPropertyAnimation(widget, b"geometry")).setDuration(duration)

    #----Pass the old size and new size to the animation----#
    size_in_animation.setStartValue(QRect(topleft.x(), topleft.y(), widget.width(), widget.height()))
    size_in_animation.setEndValue(QRect(midpoint.x(), midpoint.y(), 0, 0))

    return size_in_animation


def ShowIfStarted(state : QAbstractAnimation.State, effects : list[QGraphicsOpacityEffect]):
    """Utility function for some animations to keep widgets invisible until the animation is running"""
    if state == QAbstractAnimation.State.Running:
        if len(effects) == 1:
            QTimer.singleShot(100, lambda: effects[0].setOpacity(1))

        else:
            QTimer.singleShot(100, lambda: MakeGroupVisible(effects))


def MakeGroupVisible(effects : list[QGraphicsOpacityEffect]):
    """Used as a complement for ShowIfStarted, if needed to use on multiple widgets at once"""
    for effect in effects:
        effect.setOpacity(1)


def SetGroupInvisible(group : list[QWidget]):
    """Utility function to create a list of value 0 QGraphicsOpacityEffect objects for the group list"""
    effects = []
    for widget in group:
        widget.setGraphicsEffect(invisible := QGraphicsOpacityEffect(widget))
        invisible.setOpacity(0)
        effects.append(invisible)

    return effects
