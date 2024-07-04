import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedLayout, QPushButton, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.plot_initial_graph()

    def plot_initial_graph(self):
        self.ax.clear()
        self.ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Multiple Matplotlib Graphs in QStackedLayout')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.stacked_layout = QStackedLayout()
        
        # Create multiple Matplotlib widgets
        self.graph1 = MatplotlibWidget(self)
        self.graph2 = MatplotlibWidget(self)
        self.graph3 = MatplotlibWidget(self)

        self.stacked_layout.addWidget(self.graph1)
        self.stacked_layout.addWidget(self.graph2)
        self.stacked_layout.addWidget(self.graph3)

        # Add buttons to switch between graphs
        button_layout = QHBoxLayout()
        button1 = QPushButton("Graph 1")
        button2 = QPushButton("Graph 2")
        button3 = QPushButton("Graph 3")

        button1.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        button2.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(1))
        button3.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(2))

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addLayout(self.stacked_layout)
        main_layout.addLayout(button_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
