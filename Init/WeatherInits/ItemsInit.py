from . import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from MyWeather.View.components.Weather.WeatherWindow import WeatherTab
from MyWeather.View.components.Weather.WeatherChooseButton import TextImageButton
from .. import FONTS




def ParseItems(layout : list, parent_layout : QLayout, tab : WeatherTab):
    """Parses the dictionary containing the structure for the weather tab and initializes it accordingly

    Args:
        layout (list): List containing a dictionary for each item
        parent_layout (QLayout): Layout which the items will be added to, on init the tab's layout is passed as an argument, but if one of the items is a layout with it's own set of items a recursive call is made
        tab (WeatherTab): Items will also be appended to this tab's constant_items attribute
    """
    for item in layout:
        match item['type']:

            case "label":
                label = QLabel(text=item['text'])
                label.setFont(QFont(FONTS.weather_tab, pointSize=item['pointsize']))

                try:
                    label.setObjectName(item['objname'])

                except KeyError:
                    pass

                tab.title = label
                parent_layout.addWidget(label, stretch=item['stretch'], alignment=item['alignment'])


            case "stretch":
                parent_layout.addStretch(item['stretch'])


            case "layout":
                layout = QVBoxLayout() if item['layout'] == "vertical" else QHBoxLayout()
                layout.setContentsMargins((margins := item['margins'])[0], margins[1], margins[2], margins[3])
                layout.setSpacing(item['spacing'])

                ParseItems(item['items'], layout, tab) #recursion woohoo

                tab.selection_layout = layout
                parent_layout.addLayout(layout, stretch=item['stretch'])

            case "TextImageButton":
                button = TextImageButton(item['title'], item['description'], item['index'])

                try:
                    button.setObjectName(item['objname'])

                except KeyError:
                    pass


                tab.selections.append(button)
                parent_layout.addWidget(button, stretch=item['stretch'])

