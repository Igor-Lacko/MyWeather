#starts the app's main window
from View.MainWindow import MainWindow
from os import system as terminal
from Controller.App import Application
from Init import AppConnects




def Main():

    MyWeather = Application([])
    main_window = MainWindow()

    AppConnects.ConnectControllers(MyWeather, main_window)
    AppConnects.ConnectThread(MyWeather, main_window)
    MyWeather.ConnectThreadController()

    main_window.Run()
    MyWeather.exec()
    
    
    terminal("clear")



if __name__ == "__main__":
    Main()