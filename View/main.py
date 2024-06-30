#starts the app's main window
from . import *
from .MainWindow import MainWindow
from os import system as terminal




    



def Main():

    MyWeather = widgets.QApplication([])
    
    main_window = MainWindow()
    main_window.Run()
    
    MyWeather.exec()
    
    terminal("clear")



if __name__ == "__main__":
    Main()
