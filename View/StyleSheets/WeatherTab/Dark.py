from ..Graph.Dark import GraphFrame
WeatherTabWindow = """QFrame#weathertab{
    border: none;
    border-image: url("Assets/Backgrounds/dark/bg-weather.jpg") 0 0 0 0 stretch stretch;
}

QLabel, QPushButton{
    color: silver;
}

QLabel#title{
    border: none;
    font-size: 40;
}

QFrame#forecast, QFrame#realtime, QFrame#history{
    background-color: rgb(33,33,33);
    border: 4px solid silver;
    border-radius: 15px;
}

QLabel#forecastdescription, QLabel#realtimedescription, QLabel#historydescription{
    border-top: 2px solid silver;
    border-bottom: 2px solid silver;
    padding-top: 5px;
    padding-left: 10px;
    padding-right: 10px;
}

QLabel#forecasttitle, QLabel#realtimetitle, QLabel#historytitle{
    border-top: 2px solid silver;
}

QLabel#forecastimage, QLabel#realtimeomage, QLabel#historyimage, QLabel#graph_picker_return_image{
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

QLabel#graph_picker_return_image{
    border-image: url('Assets/door.jpg');
}

QPushButton#forecastbutton,
QPushButton#realtimebutton,
QPushButton#historybutton,
QPushButton#graph_picker_return_button{
    background: transparent;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
}

QPushButton#forecastbutton:hover:!pressed,
QPushButton#realtimebutton:hover:!pressed,
QPushButton#historybutton:hover:!pressed,
QPushButton#graph_picker_return_button:hover:!pressed{
    background-color: #11c0c0c0;
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
    background-color: rgb(33, 33, 33);
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
    border-bottom: 3px solid silver;
}

QPushButton#resetbutton, QPushButton#submitbutton{
    margin-bottom: 2px;
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
    border-left: 2px solid silver;
    border-right: none;
    border-top: none;
    border-bottom: none;
    color: silver;
    background-color: transparent;
    subcontrol-origin: left;
    selection-background-color: #11c0c0c0;
    selection-color: silver;
}

QComboBox:hover:!pressed{
    border-top: none;
    border-bottom: none;
    border-left: 2px solid silver;
    border-right: none;
    color: silver;
    background-color: #11c0c0c0;
}

QComboBox QAbstractItemView{
    background: rgb(33,33,33);
    color: silver;
    border: 2px solid white;
    selection-background-color: #11c0c0c0;
    selection-color: silver;
}

QLineEdit{
    selection-background-color: #11c0c0c0;
    selection-color: silver;
    border-left: 2px solid silver;
    border-right: none;
    border-top: none;
    border-bottom: none;
    color: silver;
    background-color: transparent;
    placeholder-text-color: darkgray;
}

QLabel#tenkinokomemetext{
    color: silver;
}

QFrame#historydaybar, QFrame#forecastdaybar{
    border-left: 2px solid silver;
}

QSlider::groove:horizontal{ 
	background-color: silver;
    border: none;
	height: 2px;
    margin: 0px;
}

QSlider::handle:horizontal{ 
	background-color: silver;
	border: none; 
	width: 10px; 
	height: 10px;
    margin: -5px 0;
	border-radius: 5px; 
}

QSlider::handle:horizontal:hover:!pressed{
    background-color: rgb(127, 255, 0);
}

QSlider::handle:horizontal:pressed{
    background-color: rgb(32, 178, 170);
}

QFrame#graph_picker_return{
    border: 5px solid turquoise;
    background-color: rgb(33, 33, 33);
    color: silver;
    border-radius: 15px;
}""" + f"\n{GraphFrame}"

