GraphFrame = """QFrame#graph_frame{
    border: 5px solid black;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    background-color: white;
}

QPushButton#right_button, QPushButton#left_button{
    background: transparent;
    border: none;
}

QPushButton#right_button:hover:!pressed,
QPushButton#left_button:hover:!pressed{
    background-color: #11000000;
}

QFrame#header_widget{
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom: 2px solid black;
    border-top: none;
    border-left: none;
    border-right: none;
    background: transparent;
}

QLabel#extended_title, QLabel#base_title{
    color: black;
    border-right: 2px solid black;
    border-bottom: none;
    border-top: none;
}

QLabel#base_title{
    border-left: none;
}

QLabel#extended_title{
    border-left: 2px solid black;
}

QComboBox#extended_menu, QComboBox#base_menu{
    border-top: none;
    border-bottom: none;
    border-left: none;
    background: transparent;
    color: black; 
    selection-background-color: #11000000;
    padding: 1px 0px 1px 3px;
}

QComboBox#extended_menu{
    border-right: 2px solid black;
}

QComboBox#base_menu{
    border-right: none;
}

QComboBox#extended_menu:hover:!pressed,
QComboBox#base_menu:hover:!pressed{
    border-top: none;
    border-bottom: none;
    border-left: none;
    color: black;
    background-color: #11000000;
}

QComboBox#extended_menu:hover:!pressed{
    border-right: 2px solid black;
}

QComboBox#base_menu:hover:!pressed{
    border-right: none;
}

QComboBox#extended_menu QAbstractItemView,
QComboBox#base_menu QAbstractItemView{
    background-color: rgb(250,249,246);
    color: black;
}

QLabel#base_title{
    border-right: 2px solid black;
    border-left: none;
}"""