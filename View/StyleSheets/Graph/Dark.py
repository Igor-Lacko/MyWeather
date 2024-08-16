GraphFrame = """QFrame#graph_frame{
    border: 5px solid silver;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    background-color: rgb(33,33,33);
}

QPushButton{
    background: transparent;
    border: none;
}

QPushButton:hover:!pressed{
    background-color: #11c0c0c0;
}

QFrame#header_widget{
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom: 2px solid silver;
    background: transparent;
}

QLabel{
    color: silver;
    border-left: 2px solid silver;
    border-right: 2px solid silver;
    border-bottom: none;
    border-top: none;
}

QComboBox{
    border-top: none;
    border-bottom: none;
    border-left: none;
    border-right: 2px solid silver;
    background: transparent;
    color: silver;
    selection-background-color: #11c0c0c0;
    padding: 1px 0px 1px 3px;
}

QComboBox:hover:!pressed{
    border-top: none;
    border-bottom: none;
    border-left: none;
    border-right: 2px solid silver;
    color: silver;
    background-color: #11c0c0c0;
}

QComboBox QAbstractItemView{
    background-color: rgb(33,33,33);
    color: silver;
}"""