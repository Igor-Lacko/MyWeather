import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedLayout, QPushButton, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setCentralWidget(w := QWidget())
        w.setAutoFillBackground(True)
        w.setStyleSheet("QWidget{background-color: blue;}")
        w.setLayout(QVBoxLayout())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
