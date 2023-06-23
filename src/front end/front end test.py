# import sys
# import matplotlib
# matplotlib.use('Qt5Agg')

# from PyQt5 import QtCore, QtGui, QtWidgets

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure


# class MplCanvas(FigureCanvasQTAgg):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)


# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         sc = MplCanvas(self, width=5, height=4, dpi=100)
#         sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

#         # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
#         toolbar = NavigationToolbar(sc, self)

#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(toolbar)
#         layout.addWidget(sc)

#         # Create a placeholder widget to hold our toolbar and canvas.
#         widget = QtWidgets.QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#         self.show()


# app = QtWidgets.QApplication(sys.argv)
# w = MainWindow()
# app.exec_()


# import sys
# import random
# import matplotlib
# matplotlib.use('Qt5Agg')

# from PyQt5 import QtCore, QtWidgets

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure


# class MplCanvas(FigureCanvas):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)


# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
#         self.setCentralWidget(self.canvas)

#         n_data = 50
#         self.xdata = list(range(n_data))
#         self.ydata = [random.randint(0, 10) for i in range(n_data)]
#         self.update_plot()

#         self.show()

#         # Setup a timer to trigger the redraw by calling update_plot.
#         self.timer = QtCore.QTimer()
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.update_plot)
#         self.timer.start()

#     def update_plot(self):
#         # Drop off the first y element, append a new one.
#         self.ydata = self.ydata[1:] + [random.randint(0, 10)]
#         self.canvas.axes.cla()  # Clear the canvas.
#         self.canvas.axes.plot(self.xdata, self.ydata, 'r')
#         # Trigger the canvas to update and redraw.
#         self.canvas.draw()


# app = QtWidgets.QApplication(sys.argv)
# w = MainWindow()
# app.exec_()

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, qApp, QAction
from PyQt5.QtGui import QIcon


class exp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        text = QTextEdit()
        self.setCentralWidget(text)

        exitAct = QAction(QIcon('heart256.ico'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Press and quit')
        exitAct.triggered.connect(qApp.quit)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.statusBar()

        tbar = self.addToolBar('Exit')
        tbar.addAction(exitAct)

        self.setGeometry(400, 200, 600, 400)
        self.setWindowTitle('all together')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = exp()
    sys.exit(app.exec_())
    