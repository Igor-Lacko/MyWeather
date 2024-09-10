from . import *
from typing import Callable
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from MyWeather.View.utils.enumerations import ColorModes
from View.StyleSheets.ListView import Dark, Light



class SettingsItem(QFrame):
    """Base class contains one QLabel as a header"""

    
    def __init__(self, description : str):
        """Constructs the settings item with the given parameters.

        Args:
            description (str): The leading text, used in the QLabel
        """

        super().__init__()
        self.setFrameStyle(QFrame.Shape.StyledPanel)

        #initialize the item components and it's layout
        self.InitLayout()
        self.description = self.InitText(description)



    
    def InitText(self, description : str) -> QLabel:
        """Initializes the QLabel with the item description 


        Args:
            description (str): The header text

        Returns:
            QLabel: The initialized QLabel widget
        """

        (lead_text := QLabel(text=description))
        lead_text.setFont(QFont(FONTS.other, pointSize=14))
        lead_text.setAlignment(Alignments.Center)

        self._layout_.addWidget(lead_text)
        lead_text.setFixedWidth(200)
        self._layout_.setStretch(0,10)

        lead_text.setWordWrap(True)
        return lead_text


    def InitLayout(self):
        """Removes some boilerplate code arount stretching/spacing the layout"""
        self._layout_ = QHBoxLayout()
        self._layout_.setContentsMargins(0,0,0,0)
        self._layout_.setSpacing(0)
        self.setLayout(self._layout_)




class SettingsMenuItem(SettingsItem):
    """Settings item with a combo box as a menu"""

    def __init__(self, description: str, items : list[str], slot : Callable):
        """Constructs the settings item with the given parameters

        Args:
            description (str): Description from the superclass
            items (list[str]): List of menu items
            slot (Callable): Menu functionality
        """ 
        
        super().__init__(description)
        self._layout_.addStretch(80)                            #spacer between menu and description
        self.menu = self.InitMenu(items,slot)
        





    def InitMenu(self, items : list[str], slot : Callable) -> QComboBox:
        """Initializes the item's menu

        Args:
            items (list[str]): List items, passed as strings
            active (str): The current active item, on the list view there is a checkmark next to it
            slot (Callable): What the menu connects to

        Returns:
            QComboBox: The initialized menu object
        """
        
        menu = QComboBox()

        for item in items:
            menu.addItem(item.title())

        menu.currentTextChanged.connect(slot)

        self._layout_.addWidget(menu)
        self._layout_.setStretch(2,10)

        menu.setFont(QFont(FONTS.other, pointSize=14))
        menu.setFixedHeight(70)
        menu.setFixedWidth(200)

        return menu
    

class SettingsFontMenuItem(SettingsItem):
    """Item with a QFontComboBox for font selection"""

    
    def __init__(self, description: str, slot : Callable):
        """Font selector constructor

        Args:
            description (str): Description from parent class constructor
            slot (Callable): Menu functionality (which font does it change)
        """
        
        super().__init__(description)
        self._layout_.addStretch(90)
        self.menu = self.InitMenu(slot)
        

    def InitMenu(self, slot : Callable):
        
        (menu := QFontComboBox()).setWritingSystem(QFontDatabase.WritingSystem.Latin)
        menu.setFontFilters(QFontComboBox.FontFilter.ScalableFonts)

        self._layout_.addWidget(menu)
        self._layout_.setStretch(2,10)

        menu.setFont(QFont(FONTS.other, pointSize=14))
        menu.setFixedHeight(70)

        menu.currentTextChanged.connect(slot)

        return menu
    



class SettingsSubmitItem(SettingsItem):

    submitted = pyqtSignal(str)

    def __init__(self, description: str, completeritems : list, slot : Callable):
        """Settings item with a LineEdit instead of a QComboBox with a submit button

        Args:
            description (str): Description form superclass
            completeritems (list): List of the items to initialize the LineEdit's autocompleter with
            slot (Callable): Item functionality
        """
        
        super().__init__(description)
        self._layout_.addStretch(80)

        self.completer, self.form = self.InitSubmitForm(completeritems)
        self.submitted.connect(slot)



    def InitSubmitForm(self, completeritems : list):
        (completer := QCompleter(completeritems, self)).setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        (form := QLineEdit()).setCompleter(completer)
        form.returnPressed.connect(self.OnSubmit)
        form.setFixedHeight(70)
        form.setFixedWidth(200)
        form.setAlignment(Alignments.Justify)
        form.setFont(QFont(FONTS.other, pointSize=14))

        self._layout_.addWidget(form)


        return completer, form
    

    def SetPopupStyle(self, mode : ColorModes):
        """Applies a style sheet to the item's popup depending on the color mode provided"""
        sheet = (Dark if mode == ColorModes.DARK else Light).ListViewPopup
        self.completer.popup().setStyleSheet(sheet)



    @pyqtSlot()
    def OnSubmit(self):
        """Emits the submitted signal with submit_text as argument"""
        self.submitted.emit(current := self.form.text())
        self.form.setPlaceholderText(current)

