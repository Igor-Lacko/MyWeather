from ..Graph.Light import GraphFrame
WeatherTabWindow = """QFrame#weathertab{
    border: none;
    border-image: url("Assets/Backgrounds/light/bg-weather.jpg") 0 0 0 0 stretch stretch;
}

QLabel, QPushButton{
    color: black;
}

QLabel#title{
    border: none;
    font-size: 40;
}

QFrame#forecast, QFrame#realtime, QFrame#history{
    background-color: rgb(250, 249, 246);
    border: 4px solid black;
    border-radius: 15px;
}

QLabel#forecastdescription, QLabel#realtimedescription, QLabel#historydescription{
    border-top: 2px solid black;
    border-bottom: 2px solid black;
    padding-top: 5px;
    padding-left: 10px;
    padding-right: 10px;
}

QLabel#forecasttitle, QLabel#realtimetitle, QLabel#historytitle{
    border-top: 2px solid black;
}

QLabel#forecastimage, QLabel#realtimeomage, QLabel#historyimage{
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
}

QLabel#forecastimage{
    border-image: url('Assets/StockAPISelections/forecast.jpg');
}

QLabel#realtimeimage{
    border-image: url('Assets/StockAPISelections/realtime.jpg');
}

QLabel#historyimage{
    border-image: url('Assets/StockAPISelections/history.jpg');
}

QPushButton#forecastbutton,
QPushButton#realtimebutton,
QPushButton#historybutton{
    background: transparent;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
}

QPushButton#forecastbutton:hover:!pressed,
QPushButton#realtimebutton:hover:!pressed,
QPushButton#historybutton:hover:!pressed{
    background-color: #11000000;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
}

QFrame{
    background: transparent;
}

QFrame#optionmenu{
    border: none;
    background-color: rgb(250, 249, 246);
    border-radius: 10px;
    margin-left: 20;
    margin-right: 20;
}


QFrame#realtimebuttons, 
QFrame#realtimelocationoption,
QFrame#realtimeviewoption,
QFrame#forecastbuttons,
QFrame#forecastlocationoption,
QFrame#forecastviewoption,
QFrame#forecastdayoption,
QFrame#forecastdateoption,
QFrame#historybuttons,
QFrame#historylocationoption,
QFrame#historyviewoption,
QFrame#historydayoption,
QFrame#historydateoption{
    border-bottom: 3px solid black;
}

QPushButton#resetbutton, QPushButton#submitbutton{
    margin-bottom: 2px;
    color: white;
    border: none;
}

QPushButton#resetbutton{
    background-color: darkred;
}

QPushButton#resetbutton:hover:!pressed{
    background-color: #b81414;
}

QPushButton#submitbutton{
    background-color: darkgreen;
    border-top-right-radius: 10px;
}

QPushButton#submitbutton:hover:!pressed{
    background-color: green;
    border-top-right-radius: 10px;
}

QComboBox{
    border-left: 2px solid black;
    border-right: none;
    border-top: none;
    border-bottom: none;
    color: black;
    background-color: transparent;
    subcontrol-origin: left;
    selection-background-color: #11000000;
    selection-color: black;
}

QComboBox:hover:!pressed{
    border-top: none;
    border-bottom: none;
    border-left: 2px solid black;
    border-right: none;
    color: black;
    background-color: #11000000;
}

QComboBox QAbstractItemView{
    background: rgb(250, 249, 246);
    color: black;
    border: 2px solid black;
    selection-background-color: #11000000;
    selection-color: black;
}

QLineEdit{
    selection-background-color: #11000000;
    selection-color: black;
    border-left: 2px solid black;
    border-right: none;
    border-top: none;
    border-bottom: none;
    color: black;
    background-color: transparent;
    placeholder-text-color: darkgray;
}

QLabel#tenkinokomemetext{
    color: black;
}

QFrame#historydaybar, QFrame#forecastdaybar{
    border-left: 2px solid black;
}

QSlider::groove:horizontal{ 
	background-color: black;
    border: none;
	height: 2px;
    margin: 0px;
}

QSlider::handle:horizontal{ 
	background-color: black;
	border: none; 
	width: 10px; 
	height: 10px;
    margin: -5px 0;
	border-radius: 5px; 
}

QSlider::handle:horizontal:hover:!pressed{
    background-color: rgb(127,255,0);
}

QSlider::handle:horizontal:pressed{
    background-color: rgb(32,178,170);
}""" + f"\n{GraphFrame}"