"""contains a list of slot connections for sidebar buittons to avoid circular import"""
from ..EventHandlers import SidebarEventHandler

slots = {
    "default"   :   SidebarEventHandler.switch_tab,
    "trigger"   :   SidebarEventHandler.switch_sidebar_color
}