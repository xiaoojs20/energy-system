import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPalette,QIcon, QFont, QDesktopServices
from PyQt5.QtCore import Qt, pyqtSlot, QUrl
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

import numpy as np
import subprocess
from streamlit.web import cli as stcli

from BatteryUI import Battery_Window, battery_state
from show_pred_UI import Pred_Window
from EMS_UI import EMS_Window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.prediction_label = QLabel(f"SHOW PREDICTION",self)
        # font = QtGui.QFont("consolas", 20)
        # self.prediction_label.setFont(font)
        # # self.power_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;")
        # self.prediction_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        # self.prediction_label.setGeometry(780, 250, 600, 200)
        # self.prediction_label.setWordWrap(True)
        # self.prediction_label.setAlignment(Qt.AlignCenter)


        # exitAct = QAction(QIcon('heart256.ico'), 'Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Press and quit')
        # exitAct.triggered.connect(qApp.quit)

        self.action_init()
        self.menu_init()

        # open_action = QAction("打开图片", self)
        # open_action.triggered.connect(self.openImage)
        # file_menu.addAction(open_action)

        # self.image_label = QLabel(self)
        # self.image_label.setScaledContents(True)

        # 将标签添加到主窗口的布局中
        # layout = QVBoxLayout()
        # layout.addWidget(self.image_label)

        # fileMenu.addAction(exitAct)

        # # self.statusBar()

        # tbar.addAction(exitAct)
        # tbar = self.addToolBar('Exit')
        # tbar = self.addToolBar('Exit')

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        width = 1200
        height = 700
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.center()
        # self.background_init()
        self.setStyleSheet("background-color: white;")
        self.botton_init()
        self.pixmap_init()
        self.setWindowTitle("Distributed Energy Storage OS")
        self.setWindowIcon(QIcon('resource/太阳能_solar-energy.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def background_init(self):
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("resource/purple.jpg")))
        self.setPalette(window_pale)

    def botton_init(self):
        x_button, y_button = 500, 440
        y_delta = 60
        w_button, h_button= 200, 50

        button_refresh = QPushButton("Status Refresh", self)
        button_refresh.setGeometry(x_button, y_button, w_button, h_button)
        font = QtGui.QFont("consolas", 12)
        button_refresh.setFont(font)
        button_refresh.setIcon(QIcon("resource/刷新_refresh.png"))
        button_refresh.clicked.connect(self.refresh)
    
        button_showPrediction = QPushButton("Show PV Pred", self)
        button_showPrediction.setGeometry(x_button, y_button+1*y_delta, w_button, h_button)
        font = QtGui.QFont("consolas", 12)
        button_showPrediction.setFont(font)
        button_showPrediction.setIcon(QIcon("resource/太阳_sun.png"))
        button_showPrediction.clicked.connect(self.show_prediction)

        button_feedback = QPushButton("EMS", self)
        button_feedback.setGeometry(x_button, y_button+2*y_delta, w_button, h_button)
        font = QtGui.QFont("consolas", 12)
        button_feedback.setFont(font)
        button_feedback.setIcon(QIcon("resource/工作台_workbench.png"))
        button_feedback.clicked.connect(self.show_EMS)

    def action_init(self):
        self.topoAction = QAction("&topo...", self)
        self.reliabilityAction = QAction("&reliability...", self)
        
        self.helpContentAction = QAction("&Contact us...", self)
        self.helpContentAction.triggered.connect(self.openEmailClient)
        self.aboutAction = QAction("&About...", self)
        

    def menu_init(self):
        menuBar = self.menuBar()
        BESSMenu = menuBar.addMenu("&BESS")
        helpMenu = menuBar.addMenu("&Help")

        BESSMenu.addAction(self.topoAction)
        BESSMenu.addAction(self.reliabilityAction)
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def pixmap_init(self):
        pixmap_scale = 50
        x1,x2,x3= np.linspace(430, 830, 3, endpoint=False, dtype=int)
        y1,y2,y3= np.linspace(70, 470, 3, endpoint=False, dtype=int)
        # 9 batteries
        battery_1 = QLabel(self)
        battery_1.setPixmap(QPixmap(battery_state(1)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_1.move(x1, y1)
        battery_1.mousePressEvent = lambda event: self.open_Battery_Window(1)

        battery_2 = QLabel(self)
        battery_2.setPixmap(QPixmap(battery_state(2)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_2.move(x2, y1)
        battery_2.mousePressEvent = lambda event: self.open_Battery_Window(2)

        battery_3 = QLabel(self)
        battery_3.setPixmap(QPixmap(battery_state(3)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_3.move(x3, y1)
        battery_3.mousePressEvent = lambda event: self.open_Battery_Window(3)

        battery_4 = QLabel(self)
        battery_4.setPixmap(QPixmap(battery_state(4)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_4.move(x1, y2)
        battery_4.mousePressEvent = lambda event: self.open_Battery_Window(4)

        battery_5 = QLabel(self)
        battery_5.setPixmap(QPixmap(battery_state(5)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_5.move(x2, y2)
        battery_5.mousePressEvent = lambda event: self.open_Battery_Window(5)

        battery_6 = QLabel(self)
        battery_6.setPixmap(QPixmap(battery_state(6)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_6.move(x3, y2)
        battery_6.mousePressEvent = lambda event: self.open_Battery_Window(6)

        battery_7 = QLabel(self)
        battery_7.setPixmap(QPixmap(battery_state(7)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_7.move(x1, y3)
        battery_7.mousePressEvent = lambda event: self.open_Battery_Window(7)

        battery_8 = QLabel(self)
        battery_8.setPixmap(QPixmap(battery_state(8)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_8.move(x2, y3)
        battery_8.mousePressEvent = lambda event: self.open_Battery_Window(8)

        battery_9 = QLabel(self)
        battery_9.setPixmap(QPixmap(battery_state(9)).scaled(50, 50, Qt.KeepAspectRatio))
        battery_9.move(x3, y3)
        battery_9.mousePressEvent = lambda event: self.open_Battery_Window(9)

    def refresh(self):
        return

    def open_Battery_Window(self, battery_id):
        self.w = Battery_Window(battery_id)
        self.w.show()

    def show_prediction(self):
        self.w = Pred_Window()
        self.w.show()

    def show_EMS(self):
        self.w = EMS_Window()
        self.w.show()

    def openEmailClient(self):
        email_url = "mailto:xiaojs20@mails.tsinghua.edu.cn"
        QDesktopServices.openUrl(QUrl(email_url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())