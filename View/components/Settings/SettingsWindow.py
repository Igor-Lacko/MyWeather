"""Contains the settings window class"""
from . import *
from MyWeather.View.utils.enumerations import Colors, ColorModes
from PyQt6.QtGui import QPalette
from View.StyleSheets.Settings import Dark, Light

class SettingsTab(QWidget):
    """Main settings widget window"""

    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self._layout_ = QVBoxLayout()
        
        self._layout_.setContentsMargins(20,80,20,50)
        self._layout_.setSpacing(0)
        self.setLayout(self._layout_)

        self.items = ItemsInit.ParseSettingsItems(self)
        self.SetColorMode(DEFAULT_MODE)


    def GetItemSheet(self, mode : ColorModes) -> str:
        """Helper function because i hated doing the mode if-else block for 1000 times
        Args:
            mode (ColorModes): Color mode provided

        Returns:
            StyleSheets: Style sheet to be used
        """
        return (Dark if mode == ColorModes.DARK else Light).SettingsItem


    def SetColorMode(self, mode : ColorModes):
        """Color mode switch

        Args:
            mode (ColorModes): The color mode to be switched to
        """
        
        (palette := QPalette()).setColor(QPalette.ColorRole.Window,
        Colors.CoolGrey if mode == ColorModes.DARK else Colors.OffWhite)
        self.setPalette(palette)

        
        for item in self.items:
            item.setStyleSheet(self.GetItemSheet(mode))

            if hasattr(item, "completer"):
                item.SetPopupStyle(mode)

