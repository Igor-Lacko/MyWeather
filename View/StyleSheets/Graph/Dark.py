GraphFrame = """QFrame#GraphFrame{
    border: 5px solid silver;
    border-radius: 15px;
    background-color: rgb(33,33,33)
}

QPushButton{
    background: transparent;
    border: none;
}

QPushButton:hover:!pressed{
    background-color: #11c0c0c0;
}

QWidget#header_widget{
    border-bottom: 2px solid silver;
}

QLabel#title_widget{
    color: silver;
    border-left: 2px solid silver;
    border-right: 2px solid silver;
    border-bottom: none;
    border-top: none;
    background: transparent;
}

QComboBox{
    border-top: none;
    border-bottom: none;
    border-left: none;
    border-right: 2px solid silver;
    background: transparent;
    color: silver;
    selection-background-color: #11c0c0c0;
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