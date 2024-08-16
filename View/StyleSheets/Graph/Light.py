GraphFrame = """QFrame#graph_frame{
    border: 5px solid black;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    background-color: white;
}

QPushButton{
    background: transparent;
    border: none;
}

QPushButton:hover:!pressed{
    background-color: #11000000;
}

QFrame#header_widget{
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom: 2px solid black;
    background: transparent;
}

QLabel{
    color: black;
    border-left: 2px solid black;
    border-right: 2px solid black;
    border-bottom: none;
    border-top: none;
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
}"""