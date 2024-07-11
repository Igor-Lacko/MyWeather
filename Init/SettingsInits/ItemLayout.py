"""Contains how the items in the settings tab are structured in the form of a dictionary\n
-the items are in order as in the dictionary\n
-the dictionary contains the item type, stretch, slot (if type == SettingsMenuItem) and name (if unique)"""
from . import *
from MyWeather.Controller.SettingsController.Functions import ColorModeUpdate



def placeholder():
    pass

Items = [
    
    #upper spacing is set already within the layout with SetContentsMargins(), so no need to do it here

    {
        "type"      :   "label",
        "stretch"   :   5,
        "text"      :   "General",
        "objname"   :   "general"
    },

    {
        "type"      :   "stretch",
        "stretch"   :   5
    },

    {
        "type"      :   "SettingsMenuItem",
        "stretch"   :   20,
        "text"      :   "Default color mode",
        "unique"    :   True,
        "objname"   :   "theme",
        "items"     :   [DEFAULT_MODE.value, "Dark" if DEFAULT_MODE.value == "light" else "Light"],
        "slot"      :   ColorModeUpdate
    },

    {
        "type"      :   "SettingsMenuItem",
        "stretch"   :   20,
        "text"      :   "Default location",
        "unique"    :   True,
        "objname"   :   "location",
        "items"     :   ["Current", "Presov"],  #update with city database later
        "slot"      :   placeholder             #update later
    },

    {
        "type"      :   "stretch",
        "stretch"   :   100
    },

    {
        "type"      :   "label",
        "stretch"   :   5,
        "text"      :   "Fonts",
        "objname"   :   "fonts"
    },

    {
        "type"      :   "stretch",
        "stretch"   :   5
    },

    {
        "type"      :   "SettingsFontMenuItem",
        "stretch"   :   20,
        "text"      :   "Sidebar",
        "unique"    :   False,
        "slot"      :   placeholder,
        "current"   :   FONTS.sidebar
    },

    {
        "type"      :   "SettingsFontMenuItem",
        "stretch"   :   20,
        "text"      :   "Header lead",
        "unique"    :   False,
        "slot"      :   placeholder,
        "current"   :   FONTS.header_lead
    },

    {
        "type"      :   "SettingsFontMenuItem",
        "stretch"   :   20,
        "text"      :   "Header data",
        "unique"    :   False,
        "slot"      :   placeholder,
        "current"   :   FONTS.header_data
    },

    {
        "type"      :   "SettingsFontMenuItem",
        "stretch"   :   20,
        "text"      :   "Graph header",
        "unique"    :   False,
        "slot"      :   placeholder,
        "current"   :   FONTS.graph_header
    },

    {
        "type"      :   "SettingsFontMenuItem",
        "stretch"   :   20,
        "text"      :   "Other",
        "unique"    :   True,
        "objname"   :   "bottom",
        "slot"      :   placeholder,
        "current"   :   FONTS.other
    }



]

