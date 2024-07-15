#starts the app's main window
from View.MainWindow import MainWindow
from os import system as terminal
from Model.App import Application




def Main():

    MyWeather = Application([])
    
    main_window = MainWindow()
    main_window.Run()
    
    MyWeather.exec()
    
    terminal("clear")



if __name__ == "__main__":
    Main()