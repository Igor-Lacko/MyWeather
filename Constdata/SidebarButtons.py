from .Mode import MODE

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
        "text" : f"{'Light' if MODE.value == 'dark' else 'Dark'} mode"
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
        "text" : f"{'Light' if MODE.value == 'dark' else 'Dark'} mode"
    }
]