from ..EventHandlers import SidebarEventHandler
from .mode import DEFAULT

buttons = [
    
    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/home.png",
        "text" : "Home",
        "on_click" : SidebarEventHandler.switch_tab
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/rain.png",
        "text" : "Weather",
        "on_click" : SidebarEventHandler.switch_tab
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/settings.png",
        "text" : "Settings",
        "on_click" : SidebarEventHandler.switch_tab
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/mode.png",
        "text" : "Light mode",
        "on_click" : SidebarEventHandler.switch_sidebar_color
    }
]

def UpdateButtons(MODE):
    global buttons 
    buttons = [
    
    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/home.png",
        "text" : "Home",
        "on_click" : SidebarEventHandler.switch_tab
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/rain.png",
        "text" : "Weather",
        "on_click" : SidebarEventHandler.switch_tab
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/settings.png",
        "text" : "Settings",
        "on_click" : SidebarEventHandler.switch_tab
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/mode.png",
        "text" : "Light mode",
        "on_click" : SidebarEventHandler.switch_sidebar_color
    }
]