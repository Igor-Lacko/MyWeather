from PyQt6.QtWidgets import *

class AbstractPopup(QDialog):
    """Basic popup class, may be specialized further later on"""

    def __init__(self, parent : QWidget, text : str):
        """Popup class constructor

        Args:
            parent (QWidget): Popup parent (the widget that triggers the popup)
            text (str): The error message to be shown
        """
        super().__init__(parent)

        self.setWindowTitle("MyWeather")        #idk what else to put here

        #message/close button
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        self.message = QLabel(text=text)

        #layout/widgets
        self._layout_ = QVBoxLayout()
        self._layout_.addWidget(self.message)
        self._layout_.addWidget(self.buttons)
        self.setLayout(self._layout_)

        #close button
        self.buttons.clicked.connect(lambda: self.done(0))
