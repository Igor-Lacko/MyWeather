GraphFrame = """QFrame#GraphFrame{
    border: 7px solid black;
    border-radius: 15px;
    background-color: rgb(250,249,246)
}

QPushButton{
    background: transparent;
    border: none;
}

QPushButton:hover:!pressed{
    background-color: #11000000;
}

QWidget#header_widget{
    border-bottom: 2px solid black;
}

QLabel#title_widget{
    color: black;
    border-left: 2px solid black;
    border-right: 2px solid black;
    border-bottom: none;
    border-top: none;
    background: transparent;
}

QComboBox{
    border-top: none;
    border-bottom: none;
    border-right: 2px solid black;
    background: transparent;
    color: black; 
    selection-background-color: #11000000;
    padding: 1px 0px 1px 3px;
}

QComboBox:hover:!pressed{
    border-top: none;
    border-bottom: none;
    border-left: none;
    border-right: 2px solid black;
    color: black;
    background-color: #11000000;
}

QComboBox QAbstractItemView{
    background-color: rgb(250,249,246);
    color: black;
}

FigureCanvasQTAgg{
    border-bottom: 2px black solid;
}"""