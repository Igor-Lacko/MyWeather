from MyWeather.Controller.App import Application
from MyWeather.View.MainWindow import MainWindow




def ConnectThread(app : Application, main_window : MainWindow):
    """Connects the app's worker thread to all components which are to be updated"""
    main_window.home.header.update_data.connect(app.worker_object.UpdateData)
    main_window.home.header.fetch_new_data.connect(app.worker_object.FetchNewData)



def ConnectControllers(app : Application, main_window : MainWindow):
    """Connects the main window's subcomponents to their respective controllers in the app"""
    app.header_controller.ConnectHeader(main_window.home.header)
    app.graph_controller.ConnectGraph(main_window.home.window.graph)