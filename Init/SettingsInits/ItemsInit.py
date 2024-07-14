from . import *
from .ItemLayout import Items
from MyWeather.View.components.Settings.SettingsItem import *
from MyWeather.View.components.Settings.SettingsWindow import SettingsTab





def GetHeaderLabel(text : str, name : str):
    """Returns a left-aligned QLabel"""

    (label := QLabel(text=text)).setFont(QFont(FONTS.other, pointSize=20))
    label.setAlignment(Alignments.Left)
    label.setObjectName(name)

    return label




def AddItemStretch(settings : SettingsTab, item : QWidget, stretch : int, index : int):
    settings._layout_.addWidget(item)
    settings._layout_.setStretch(index, stretch)



def ParseSettingsItems(settings : SettingsTab):

    initialized = []

    for index, item in enumerate(Items):
        
        match item["type"]:
            
            case "label":
                label = GetHeaderLabel(item["text"], item["objname"])
                
                AddItemStretch(settings, label, item["stretch"], index)
                initialized.append(label)

            
            case "stretch":
                settings._layout_.addStretch(item["stretch"])
            
            
            case "SettingsMenuItem":
                menu_item = SettingsMenuItem(item["text"], item["items"], item["slot"])

                if item["unique"]:
                    menu_item.setObjectName(item["objname"])

                AddItemStretch(settings, menu_item, item["stretch"], index)
                initialized.append(menu_item)

            
            case "SettingsFontMenuItem":
                menu_font_item = SettingsFontMenuItem(item["text"], item["slot"])
                menu_font_item.menu.setCurrentFont(QFont(item["current"]))

                if item["unique"]:
                    menu_font_item.setObjectName(item["objname"])

                AddItemStretch(settings, menu_font_item, item["stretch"], index)
                initialized.append(menu_font_item)

    return initialized


