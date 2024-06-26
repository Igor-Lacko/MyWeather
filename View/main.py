#starts the app's main window
import PyQt6.QtWidgets as widgets
from .MainWindow import MainWindow
from os import system as terminal
from .constdata.mode import *



    



def Main():
    MyWeather = widgets.QApplication([])
    
    main_window = MainWindow()
    main_window.Run()
    
    MyWeather.exec()
    
    terminal("clear")



if __name__ == "__main__":
    Main()
