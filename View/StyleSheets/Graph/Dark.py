GraphFrame = """QFrame#graph_frame{
    border: 5px solid silver;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    background-color: rgb(33,33,33);
}

QPushButton#right_button, QPushButton#left_button{
    background: transparent;
    border: none;
}

QPushButton#right_button:hover:!pressed,
QPushButton#left_button:hover:!pressed{
    background-color: #11c0c0c0;
}

QFrame#header_widget{
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom: 2px solid silver;
    border-top: none;
    border-left: none;
    border-right: none;
    background: transparent;
}

QLabel#extended_title, QLabel#base_title{
    color: silver;
    border-right: 2px solid silver;
    border-bottom: none;
    border-top: none;
}

QLabel#base_title{
    border-left: none;
}

QLabel#extended_title{
    border-left: 2px solid silver;
}

QComboBox#extended_menu, QComboBox#base_menu{
    border-top: none;
    border-bottom: none;
    border-left: none;
    background: transparent;
    color: silver; 
    selection-background-color: #11c0c0c0;
    padding: 1px 0px 1px 3px;
}

QComboBox#extended_menu{
    border-right: 2px solid silver;
}

QComboBox#base_menu{
    border-right: none;
}

QComboBox#extended_menu:hover:!pressed,
QComboBox#base_menu:hover:!pressed{
    border-top: none;
    border-bottom: none;
    border-left: none;
    color: silver;
    background-color: #11c0c0c0;
}

QComboBox#extended_menu:hover:!pressed{
    border-right: 2px solid silver;
}

QComboBox#base_menu:hover:!pressed{
    border-right: none;
}

QComboBox#extended_menu QAbstractItemView,
QComboBox#base_menu QAbstractItemView{
    background-color: rgb(33,33,33);
    color: silver;
}

QLabel#base_title{
    border-right: 2px solid silver;
    border-left: none;
}"""