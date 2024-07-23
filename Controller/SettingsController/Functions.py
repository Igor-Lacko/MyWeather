"""Contains functions that are called on update in the settings tab"""
from . import *
from PyQt6.QtWidgets import QLabel



def UpdateSettings():
    """Function that updates the settings on exit"""
    with open("Settings.json", "w") as config_obj:
        json.dump(settings, config_obj, indent=2)



    
def ColorModeUpdate(mode : str):
    settings['theme'] = mode.lower()
    UpdateSettings()


def LocationUpdate(location : str):
    settings['location'] = location.title()
    UpdateSettings()

def SidebarFontUpdate(font : str):
    settings['fonts']['sidebar'] = font
    UpdateSettings()

def HeaderLeadFontUpdate(font : str):
    settings['fonts']['header_lead'] = font
    UpdateSettings()


def HeaderDataFontUpdate(font : str):
    settings['fonts']['header_data'] = font
    UpdateSettings()


def GraphHeaderFontUpdate(font : str):
    settings['fonts']['graph_header'] = font
    UpdateSettings()


def OtherFontUpdate(font : str):
    settings['fonts']['other'] = font
    UpdateSettings()




def UpdateSettingsFonts(settings : SettingsTab, font : str):
    """Called when settings fonts are to be changed (The "Other" Section In Fonts)"""
    for item in settings.items:
        
        if type(item) == QLabel:
            item.setFont(QFont(font, pointSize=14))

        elif type(item) == SettingsSubmitItem:
            item.form.setFont(QFont(font, pointSize=14))
            item.description.setFont(QFont(font, pointSize=14))

        else:
            item.description.setFont(QFont(font, pointSize=14))