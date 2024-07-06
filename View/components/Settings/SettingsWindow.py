"""Contains the settings window class"""
from . import *
from PyQt6.QtWidgets import *

class SettingsTab(QVBoxLayout):
    """Main settings vertical layout"""

    def __init__(self):
        super().__init__()
        
        self.setContentsMargins(20,20,20,20)
        self.setSpacing(0)