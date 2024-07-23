#starts the app's main window
from View.MainWindow import MainWindow
from os import system as terminal
from Controller.App import Application
from Init import Connect

MyWeather = Application([])
main_window = MainWindow()



def Main():
    Connect.ConnectOnStartup(MyWeather, main_window)
    main_window.Run()
    MyWeather.exec()
    terminal("clear")



if __name__ == "__main__":
    Main()