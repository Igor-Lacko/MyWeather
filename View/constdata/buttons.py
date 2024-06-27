from .mode import DEFAULT

buttons = [

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/home.png",
        "text" : "Home"
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/weather.png",
        "text" : "Weather"
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/settings.png",
        "text" : "Settings"
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{DEFAULT.value}/mode.png",
        "text" : "Light mode"
    }
]

def UpdateButtons(MODE):
    global buttons 
    buttons = [

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/home.png",
        "text" : "Home"
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/weather.png",
        "text" : "Weather"
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/settings.png",
        "text" : "Settings"
    },

    {
        "icon" : f"View/Assets/SidebarIcons/{MODE.value}/mode.png",
        "text" : "Light mode"
    }
]