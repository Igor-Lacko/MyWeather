SettingsMain = """QWidget{
    background-color: rgb(250, 249, 246);
}"""

SettingsItem = """QFrame#theme, QFrame#bottom, QFrame#location{
    border: 3px solid black;
    background-color: rgb(250,249,246);
}

QFrame#num_days{
    border-top: none;
    border-left: 3px solid black;
    border-right: 3px solid black;
    border-bottom: none;
}

QFrame{
    border-left: 3px solid black;;
    border-right: 3px solid black;
    border-top: 3px solid black;
    border-bottom: none;
}

QLabel{
    border-right: 2px solid black;
    border-left: none;
    border-top: none;
    border-bottom: none;
    color: black;
}

QLabel#general, QLabel#font{
    color: black;
    border: none;
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
    background: rgb(250,249,246);
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
}"""