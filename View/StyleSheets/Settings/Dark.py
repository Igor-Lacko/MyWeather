SettingsMain = """QWidget{
    background-color: rgb(33,33,33)
}"""

SettingsItem = """QFrame#theme, QFrame#bottom, QFrame#location{
    border: 3px solid silver;
    background-color: rgb(33,33,33);
}

QFrame#num_days{
    border-top: none;
    border-left: 3px solid silver;
    border-right: 3px solid silver; 
    border-bottom: none;
}

QFrame{
    border-right: 3px solid silver;
    border-left: 3px solid silver;
    border-top: 3px solid silver;
    border-bottom: none;
}

QLabel{
    border-right: 2px solid silver;
    border-left: none;
    border-top: none;
    border-bottom: none;
    color: silver;
}

QLabel#general, QLabel#font{
    border: none;
    color: silver;
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
}"""