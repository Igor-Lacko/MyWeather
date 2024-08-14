ListViewPopup = """QListView{
    background-color: rgb(250, 249, 246);
    color: black;
    border: 2px solid black;
}

QListView::item{
    color: black;
    border: none;
}

QListView::item:hover{
    background-color: #11000000;
}

QScrollBar:vertical{
    background-color: rgb(250, 249, 246);
    border-left: 1px solid black;
    border-right: none;
    border-top: none;
    border-bottom: none;
}

QScrollBar::handle:vertical{
    border-bottom: 1px solid black;
    border-top: 1px solid black;
    border-right: none;
    border-left: none;
}

QScrollBar::add-line:vertical {
    height: 0px;
}

QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    height: 0px;
}"""