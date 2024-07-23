"""Contains all the slot connections that should be run on Init in a single function"""
from . import AppConnects
from .SettingsInits import SettingsConnects





def ConnectOnStartup(app, main_window):
    AppConnects.ConnectControllers(app, main_window)
    AppConnects.ConnectThread(app, main_window)
    AppConnects.ConnectSidebarButtons(main_window)
    SettingsConnects.ConnectSettingsMenus(main_window)
    app.ConnectThreadController()