from PyQt6.QtWidgets import *
from ..components.test import ColoredBar
from . import enumerations 


class SettingsTab(QVBoxLayout):
    """contains the settings tab for the application

    Args:
        QVBoxLayout (QVBoxLayout): Has items aligned vertically
    """

    def __init__(self):
        """home tab constructor"""
        super().__init__()

        self.addWidget(ColoredBar(color=enumerations.Colors.Cream))
        self.setContentsMargins(0,0,0,0)