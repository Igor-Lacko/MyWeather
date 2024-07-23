"""Contains the header for the home tab, with a icon, temperature and some other data with all it's sub-components"""
from PyQt6.QtWidgets import *
from MyWeather.Model.obj import Realtime
from MyWeather.View.Styles.Sheets import StyleSheets
from MyWeather.View.utils.enumerations import *
from MyWeather.Init import FONTS
from MyWeather.Constdata.Mode import MODE
from PyQt6.QtGui import QFont