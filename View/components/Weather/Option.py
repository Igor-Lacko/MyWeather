"""Contains the QFrame Option subclass that makes up the OptionMenu"""
from . import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtProperty
from math import ceil

class AbstractOption(QFrame):
    """"Main" option class, contains things that almost every option has (so a description and a HBox layout with 50/ stretch), subclasses fill out the second half of the option"""
    def __init__(self, text : str, pointsize : int):
        """Option constructor"""
        super().__init__()
        self._layout_ = QHBoxLayout()
        self._layout_.setContentsMargins(10,0,0,0)              #some padding at the left border for the text
        self._layout_.setSpacing(0)
        self.setLayout(self._layout_)

        if text is not None and pointsize is not None:
            self.description = self.GetLabel(text, pointsize)
            self._layout_.addWidget(self.description, stretch=50)





    def GetLabel(self, text : str, pointsize : int, wrap : bool=False) -> QLabel:
        (label := QLabel(text=text)).setFont(QFont(FONTS.weather_tab, pointSize=pointsize))
        label.setWordWrap(wrap)
        return label


class TwoButtonsOption(AbstractOption):
    """Abstract option subclass which contains two buttons (the reset and submit buttons, probably never used after that)"""
    def __init__(self, pointsize : int, space : int):
        super().__init__(None, None)

        self._layout_.addStretch(space)
        self.reset_button, self.submit_button = QPushButton(text="✖"), QPushButton(text="✔")
        self._layout_.addWidget(self.reset_button, stretch=(100 - space) // 2)          #space + 2 buttons should add up to 100
        self._layout_.addWidget(self.submit_button, stretch=(100 - space) // 2)

        for button in [self.reset_button, self.submit_button]:
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.setFont(QFont(FONTS.weather_tab, pointSize=pointsize))



class ComboBoxOption(AbstractOption):
    """Abstract option subclass which contains a combobox to select items from"""
    def __init__(self, text: str, pointsize: int, items : list[str]):
        super().__init__(text, pointsize)
        self.combo_box = QComboBox()

        self.combo_box.setEditable(True)
        self.combo_box.addItems(items)

        (completer := QCompleter(items, self.combo_box)).setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer = completer
        self.combo_box.setCompleter(completer)


        self.combo_box.setFixedWidth(300)
        self.combo_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.combo_box.setFont(QFont(FONTS.other, pointSize=15))

        self._layout_.addWidget(self.combo_box)


class LineEditOption(AbstractOption):
    """Abstract option subclass with a line edit to type in an item"""
    def __init__(self, text: str, pointsize: int, placeholder : str, items : list[str]):
        super().__init__(text, pointsize)
        self.line_edit = QLineEdit()

        (completer := QCompleter(items, self.line_edit)).setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer = completer
        self.line_edit.setCompleter(completer)

        self.line_edit.setFont(QFont(FONTS.other, pointSize=15))
        self.line_edit.setPlaceholderText(placeholder)

        self.line_edit.setFixedWidth(300)
        self.line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._layout_.addWidget(self.line_edit)


class ImageOption(AbstractOption):
    """Abstract option subclass with another QLabel used with QPixmap"""
    def __init__(self, text: str, pointsize: int, image_path : str):
        super().__init__(text, pointsize)
        self.image = QLabel()

        self.image.setPixmap(QPixmap(image_path))
        self.image.setAlignment(Alignments.CenterLeft)
        self.description.setAlignment(Alignments.CenterRight)

        self._layout_.addWidget(self.image, stretch=50)
        self._layout_.setSpacing(10)


class SliderOption(AbstractOption):
    """Abstract option subclass with a slider to pick from a range"""
    def __init__(self, text: str, pointsize: int, range : int):
        super().__init__(text, pointsize)
        self.slider = Slider(range, pointsize)

        self.slider.setFixedWidth(300)
        self.slider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        self._layout_.addWidget(self.slider, stretch=50)


class Slider(QFrame):
    """Custom widget that includes a QSlider which shows the current, minimum and maximum values"""
    def __init__(self, range : int, pointsize : int):
        super().__init__()

        #add a range instance variable since we are using 100 for smooth movement
        self.range = range

        #set spacing/layout settings
        self._layout_ = QVBoxLayout()
        self._layout_.setSpacing(0)
        self._layout_.setContentsMargins(0,0,0,0)
        self.setLayout(self._layout_)

        #add a Slider first
        self.slider = QSlider(orientation=Qt.Orientation.Horizontal)
        self.slider.setRange(1, 100)

        #create a QLabel with the current value and add it to the widget's layout
        self.current = QLabel(text=str(self.slider.value()))
        self.current.setFont(QFont(FONTS.weather_tab, pointSize=pointsize))
        self.current.setAlignment(Alignments.BottomCenter)
        self._layout_.addWidget(self.current, stretch=50)

        #connect the slider to modify the current's value
        self.slider.valueChanged.connect(lambda: self.current.setText(str(self.value)))

        #create a QHBoxLayout with |min|----Slider----|max|
        self.slider_layout = QHBoxLayout()
        self.slider_layout.setSpacing(0)
        self.slider_layout.setContentsMargins(0,0,0,20)

        #create the individual labels and apply font/alignment settings
        self.min = QLabel(text='1')
        self.max = QLabel(text=str(self.range))

        for label in [self.min, self.max]:
            label.setFont(QFont(FONTS.weather_tab, pointSize=pointsize))
            label.setAlignment(Alignments.Center)

        #add them to the slider layout and add that layout to the main one
        self.slider_layout.addWidget(self.min, stretch=15)
        self.slider_layout.addWidget(self.slider, stretch=70)
        self.slider_layout.addWidget(self.max, stretch=15)

        self._layout_.addLayout(self.slider_layout, stretch=50)


    #property used for calculating the slider value from the intervals in (100 // range)
    @pyqtProperty(int)
    def value(self):
        if (result := (ceil(self.slider.value() / (100 // self.range)))) > self.range:
            return self.range

        return result