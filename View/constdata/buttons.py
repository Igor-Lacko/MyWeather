from .mode import DEFAULT

buttons = [

    {
        "icon" : f"Assets/SidebarIcons/{DEFAULT.value}/home.png",
        "text" : "Home"
    },

    {
        "icon" : f"Assets/SidebarIcons/{DEFAULT.value}/weather.png",
        "text" : "Weather"
    },

    {
        "icon" : f"Assets/SidebarIcons/{DEFAULT.value}/settings.png",
        "text" : "Settings"
    },

    {
        "icon" : f"Assets/SidebarIcons/{DEFAULT.value}/mode.png",
        "text" : "Light mode"
    }
]

def UpdateButtons(MODE):
    global buttons 
    buttons = [

    {
        "icon" : f"Assets/SidebarIcons/{MODE.value}/home.png",
        "text" : "Home"
    },

    {
        "icon" : f"Assets/SidebarIcons/{MODE.value}/weather.png",
        "text" : "Weather"
    },

    {
        "icon" : f"Assets/SidebarIcons/{MODE.value}/settings.png",
        "text" : "Settings"
    },

    {
        "icon" : f"Assets/SidebarIcons/{MODE.value}/mode.png",
        "text" : "Light mode"
    }
]