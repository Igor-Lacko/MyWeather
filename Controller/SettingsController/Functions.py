"""Contains functions that are called on update in the settings tab"""
from . import *

def UpdateSettings():
    """Function that updates the settings on exit"""
    with open("Config/settings.json", "w") as config_obj:
        json.dump(settings, config_obj, indent=2)



    
def ColorModeUpdate(mode : str):
    print(mode)
    settings['theme'] = mode.lower()
    UpdateSettings()

