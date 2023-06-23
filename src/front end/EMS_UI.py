import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pandas as pd


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.suptitle("EMS")
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class EMS_Window(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(EMS_Window, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40],label='66')

        # Create our pandas DataFrame with some simple
        # data and headers.
        df = pd.DataFrame([
           [0, 10], [5, 15], [2, 20], [15, 25], [4, 10],
        ], columns=['A', 'B'])


        # Create toolbar, passing canvas as first parament, parent (self, the Pred_Window) as second.
        toolbar = NavigationToolbar(sc, self)
    
        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.initUI()
        self.show()

    def initUI(self):
        width = 1200
        height = 700
        self.resize(width, height)
        # self.setMinimumSize(width, height)
        # self.setMaximumSize(width, height)
        self.center()
        # self.background_init()
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("EMS")
        self.setWindowIcon(QIcon('resource/工作台_workbench.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = EMS_Window()
    app.exec_()