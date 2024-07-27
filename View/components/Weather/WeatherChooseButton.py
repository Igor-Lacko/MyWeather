from . import *
from PyQt6.QtGui import QFont, QPainter, QColor, QBrush
from PyQt6.QtCore import pyqtProperty, QRect, Qt, pyqtSignal





class TextImageButton(QFrame):
    user_submitted = pyqtSignal(int)
    def __init__(self, title : str, description_text : str, index : int):
        super().__init__()
        self.index = index

        self._layout_ = QVBoxLayout()
        self._layout_.setContentsMargins(0,0,0,0)
        self._layout_.setSpacing(0)

        self.image = self.GetImageContainer(title, 50)
        self.text_container = self.GetTextContainer(title, description_text, 40)
        self.button = self.GetButton(title, 10)

        self.setLayout(self._layout_)



    def GetTextContainer(self, title : str, description_text : str, stretch : int) -> QVBoxLayout:
        """Returns a initialized QVBoxLayout containing the widget's title and description

        Args:
            title (str): Widget title
            description_text (str): Widget description
            stretch (int): Layout's stretch inside the widget's main layout

        Returns:
            QVBoxLayout: Initialized QVBoxLayout
        """

        (text_layout := QVBoxLayout()).addWidget(title_widget := self.GetTitle(title), stretch=10)
        text_layout.addWidget(description_widget := self.GetDescription(title, description_text), stretch=30)

        text_layout.setContentsMargins(0,0,0,0)
        text_layout.setSpacing(0)

        self.title = title_widget
        self.description = description_widget

        self._layout_.addLayout(text_layout, stretch=stretch)
        return text_layout


    def GetImageContainer(self, title : str, stretch : int) -> QLabel:
        """Initializes and returns the image QLabel. Image is set by QSS by object name, so no need to do it here

        Args:
            title (str): Widget title. Used for setting the object name so QSS sets the correct image to the container
            stretch (int): The container's strech inside the  widget's layout

        Returns:
            QLabel: The initialized QLabel image container
        """

        self._layout_.addWidget((image := QLabel()), stretch=stretch)
        image.setObjectName(f"{title}image".lower())    #So the QSS knows which image to set

        return image


    def GetTitle(self, title_text : str) -> QLabel:
        """Initializes and returns the widget title

        Args:
            title_text (str): The text of the title

        Returns:
            QLabel: Initialized title QLabel
        """

        (title := QLabel(text=title_text)).setObjectName(f"{title_text}title".lower())
        title.setAlignment(Alignments.Center)
        title.setObjectName(f"{title_text}title".lower())
        title.setFont(QFont(FONTS.weather_tab, pointSize=20))

        return title


    def GetDescription(self, title : str, description_text : str) -> QLabel:
        """Initializes and returns the widget description text

        Args:
            title (str): The widget title. Used for setting object name
            description_text (str): The description text

        Returns:
            QLabel: Initialized description QLabel
        """

        (description := QLabel(text=description_text)).setAlignment(Alignments.Justify)
        description.setWordWrap(True)
        description.setObjectName(f"{title}description".lower())
        description.setFont(QFont(FONTS.weather_tab))

        return description



    def GetButton(self, title : str, stretch : int) -> QPushButton:
        """Initializes and returns the widget's push button

        Args:
            title (str): Widget title. Used to set the button's name
            stretch (int): Button's stretch inside the widget's main layout

        Returns:
            QPushButton: The initialized QPushButton
        """

        (button := AnimatedButton()).setObjectName(f"{title}button".lower())
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button.setFont(QFont(FONTS.weather_tab, pointSize=14))
        button.setText(f"Press to get {title.lower()} data.")
        button.clicked.connect(self.OnClick)

        self._layout_.addWidget(button, stretch=stretch)

        return button


    def OnClick(self):
        self.user_submitted.emit(self.index)





class AnimatedButton(QPushButton):
    """Custom widget that fills up with green on click"""
    def __init__(self):
        super().__init__()
        self._filled_part = 0 #percentage of being filled


    @pyqtProperty(int)
    def filled_part(self):
        return self._filled_part

    @filled_part.setter
    def filled_part(self, value):
        if self._filled_part != value:
            self._filled_part = value
            self.update()

    def paintEvent(self, a0: QPaintEvent | None):
        if self.filled_part == 0:
            super().paintEvent(a0)
            return

        painter = QPainter(self)
        button_area = self.rect()

        xmiddle = int(button_area.width() // 2)
        ymiddle = int(button_area.height() // 2)
        width = button_area.width()
        height = button_area.height()

        draw_area = QRect(
            xmiddle - int((width / 100) * (self.filled_part // 2)),
            ymiddle - int((height / 100) * (self.filled_part // 2)),
            int(width // (100 / self.filled_part)), 
            int(height // (100 / self.filled_part))
        )

        #---Fill the widget with opaque light green color---#
        painter.setBrush(QBrush(QColor(35,220,61,100)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(draw_area, 15, 15)

        #---Redraw the button's text---#
        painter.setPen(QColor("black" if self.parentWidget().parentWidget().color_mode.value == "light" else "silver"))
        painter.setFont(self.font())
        painter.drawText(button_area, Alignments.Center, self.text())
