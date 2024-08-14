ListViewPopup = """QListView{
    background-color: rgb(33, 33, 33);
    color: silver;
    border: 2px solid silver;
}

QListView::item{
    color: silver;
    border: none;
}

QListView::item:hover{
    background-color: #11c0c0c0;
}

QScrollBar:vertical{
    background-color: rgb(33, 33, 33);
    border-left: 1px solid silver;
    border-right: none;
    border-bottom: none;
    border-top: none;
}

QScrollBar::handle:vertical{
    border-bottom: 1px solid silver;
    border-top: 1px solid silver;
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