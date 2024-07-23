from MyWeather.Controller.App import Application
from MyWeather.View.MainWindow import MainWindow
from functools import partial




def ConnectThread(app : Application, main_window : MainWindow):
    """Connects the app's worker thread to all components which are to be updated"""
    main_window.home.header.update_data.connect(app.worker_object.UpdateData)
    main_window.home.header.fetch_new_data.connect(app.worker_object.FetchNewData)



def ConnectControllers(app : Application, main_window : MainWindow):
    """Connects the main window's subcomponents to their respective controllers in the app"""
    app.header_controller.ConnectHeader(main_window.home.header)
    app.graph_controller.ConnectGraph(main_window.home.window.graph)
    app.sidebar_controller.ConnectSidebar(main_window.sidebar)


def ConnectSidebarButtons(main_window : MainWindow):
    """Connects some components together (for example, the sidebar light/dark mode button to other parts of the app)"""
    for button in main_window.sidebar.buttons:
        #color switch button case
        if button is main_window.sidebar.mode_trigger:
            button.color_switch_signal.connect(main_window.home.header.SwitchColorMode)
            button.color_switch_signal.connect(main_window.home.window.SwitchColorMode)
            button.color_switch_signal.connect(main_window.settings.SetColorMode)
            button.color_switch_signal.connect(main_window.weather.SetColorMode)

        #normal button case
        else:
            button.tab_switch_signal.connect(partial(main_window.tabs.setCurrentIndex, button.index))
