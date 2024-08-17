"""Parser module for initializing the option menu and it's layout"""
from . import *
from MyWeather.View.components.Weather.OptionsMenu import OptionMenu
from MyWeather.View.components.Weather.Option import *
from MyWeather.View.utils.enumerations import ColorModes
from .OptionMenuLayout import *
from typing import Callable

def OptionMenuParser(api_choice : str, color_mode : ColorModes, reset : Callable, submit : Callable) -> OptionMenu:
    """Parses a dictionary with the option menu for api_choice and returns it

    Args:
        api_choice (str): The api choice from ["Realtime", "Forecast", "History"]
        color_mode (ColorModes): Initial color mode
        reset (Callable): Menu's reset button slot
        submit (Callable): Menu's submit button slot

    Returns:
        OptionMenu: Initialized OptionMenu object
    """

    menu = OptionMenu(api_choice)
    layout = realtime_menu_layout if api_choice.lower() == "realtime" else\
    (forecast_menu_layout if api_choice.lower() == "forecast" else history_menu_layout)

    for item in layout:
        match item['type']:
            case "twobuttonsoption":
                option = TwoButtonsOption(item['pointsize'], item['space'])
                option.setObjectName(item['name'])

                option.reset_button.setObjectName(item['resetbutton']['name'])
                option.reset_button.clicked.connect(reset)
                option.submit_button.setObjectName(item['submitbutton']['name'])
                option.submit_button.clicked.connect(submit)

                menu._layout_.addWidget(option, stretch=item['stretch'])
                menu.items.append(option)

            case "comboboxoption":
                option = ComboBoxOption(item['label']['text'], item['label']['pointsize'], item['key'], item['combobox']['items'])
                option.setObjectName(item['name'])
                option.description.setObjectName(item['label']['name'])
                option.combo_box.setObjectName(item['combobox']['name'])

                menu._layout_.addWidget(option, stretch=item['stretch'])
                menu.items.append(option)

            case "lineeditoption":
                option = LineEditOption(item['label']['text'], item['label']['pointsize'], item['key'], item['lineedit']['example'], item['lineedit']['items'])
                option.setObjectName(item['name'])
                option.description.setObjectName(item['label']['name'])
                option.line_edit.setObjectName(item['lineedit']['name'])

                menu._layout_.addWidget(option, stretch=item['stretch'])
                menu.items.append(option)

            case "imageoption":
                option = ImageOption(item['label']['text'], item['label']['pointsize'], item['image']['path'])
                option.setObjectName(item['name'])
                option.description.setObjectName(item['label']['name'])
                option.image.setObjectName(item['image']['name'])

                menu._layout_.addWidget(option, stretch=item['stretch'])

            case "slideroption":
                option = SliderOption(item['label']['text'], item['label']['pointsize'], item['key'],item['slider']['range'])
                option.setObjectName(item['name'])
                option.description.setObjectName(item['label']['name'])
                option.slider.setObjectName(item['slider']['name'])

                menu._layout_.addWidget(option, item['stretch'])
                menu.items.append(option)

            case "stretch": #if too much empty space is left there
                menu._layout_.addStretch(item['stretch'])

            case _:
                pass

    menu.SetColorMode(color_mode)
    return menu
