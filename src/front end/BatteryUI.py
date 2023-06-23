import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPalette,QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

import numpy as np
import pandas as pd

percentage = [0.8,0.6,0.5,0.4,0.9,0.5,0.7,0,1]
charging_power = [100,200,100,50,100,50,100,100,200]
connection = ["connnected","connnected","connnected","disconnnected","connnected","connnected","connnected","connnected","connnected"]

# read data
df_test = pd.read_csv('data/test.csv', header=0, infer_datetime_format=True, parse_dates=['index_test'], index_col=['index_test'])
df_test.info()

df_BESS1 = pd.DataFrame({'SoC': [0.8],'power': [-10],'connection': ['1']})
df_BESS2 = pd.DataFrame({'SoC': [0.6],'power': [-10],'connection': ['1']})
df_BESS3 = pd.DataFrame({'SoC': [0.5],'power': [-16],'connection': ['0']})
df_BESS4 = pd.DataFrame({'SoC': [0.4],'power': [-4],'connection': ['1']})
df_BESS5 = pd.DataFrame({'SoC': [0.9],'power': [5],'connection': ['1']})
df_BESS6 = pd.DataFrame({'SoC': [0.5],'power': [6],'connection': ['0']})
df_BESS7 = pd.DataFrame({'SoC': [0.7],'power': [-10],'connection': ['1']})
df_BESS8 = pd.DataFrame({'SoC': [0.1],'power': [-1],'connection': ['1']})
df_BESS9 = pd.DataFrame({'SoC': [0.8],'power': [-12],'connection': ['1']})

df_BESS1.to_csv('data/BESS_data/BESS1.csv', index=False)
df_BESS2.to_csv('data/BESS_data/BESS2.csv', index=False)
df_BESS3.to_csv('data/BESS_data/BESS3.csv', index=False)
df_BESS4.to_csv('data/BESS_data/BESS4.csv', index=False)
df_BESS5.to_csv('data/BESS_data/BESS5.csv', index=False)
df_BESS6.to_csv('data/BESS_data/BESS6.csv', index=False)
df_BESS7.to_csv('data/BESS_data/BESS7.csv', index=False)
df_BESS8.to_csv('data/BESS_data/BESS8.csv', index=False)
df_BESS9.to_csv('data/BESS_data/BESS9.csv', index=False)

df_BESS = [df_BESS1, df_BESS2, df_BESS3, df_BESS4, df_BESS5, df_BESS6, df_BESS7, df_BESS8, df_BESS9]

charge = "resource/电池充电_battery-charge.png"
full = "resource/电池满电_battery-full.png"
empty = "resource/电池没电_battery-empty.png"
working = "resource/电池运行_battery-working.png"
charge_disconnected = "resource/电池充电_battery-charge_disconnected.png"
full_disconnected = "resource/电池满电_battery-full_disconnected.png"
empty_disconnected = "resource/电池没电_battery-empty_disconnected.png"
working_disconnected = "resource/电池运行_battery-working_disconnected.png"

def battery_state(id):
    if df_BESS[id-1].loc[0,'power'] > 0:
        if df_BESS[id-1].loc[0,'connection'] == '1':
            return charge
        else:
            return charge_disconnected
        
    if df_BESS[id-1].loc[0,'SoC'] <= 0.2:
        if df_BESS[id-1].loc[0,'connection'] == '1':
            return empty
        else:
            return empty_disconnected
    if df_BESS[id-1].loc[0,'SoC'] > 0.2 and df_BESS[id-1].loc[0,'SoC'] <= 0.8:
        if df_BESS[id-1].loc[0,'connection'] == '1':
            return working
        else:
            return working_disconnected
    if df_BESS[id-1].loc[0,'SoC'] > 0.8:
        if df_BESS[id-1].loc[0,'connection'] == '1':
            return full
        else:
            return full_disconnected


class Battery_Window(QMainWindow):
    def __init__(self, id):
        super().__init__()
        
        self.initUI(id)

    def initUI(self,id):
        width = 350
        height = 200
        connection_dict = {'0':'disconnected', '1':'connected'}
        # 创建显示储能功率和连接关系的 Label
        # 储能电量比例80%、充放电功率100kW、连接信息connected

        self.power_label = QLabel(f"SoC: {100*df_BESS[id-1].loc[0,'SoC']}% \
                                  Power: {df_BESS[id-1].loc[0,'power']} KW\
                                  Connection: {connection_dict[df_BESS[id-1].loc[0,'connection']]}",self)
        font = QtGui.QFont("consolas", 12)
        self.power_label.setFont(font)
        # self.power_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;")
        self.power_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self.power_label.setGeometry(50, 0, width, height//2)
        self.power_label.setWordWrap(True)
        # self.power_label.setAlignment(Qt.AlignCenter)
    
        self.resize(width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.center()
        self.botton_init()
        # self.background_init()
        self.setWindowTitle(f"BESS {id} Info")
        self.setWindowIcon(QIcon('resource/battery.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def botton_init(self):
        button_refresh = QPushButton("Connect", self)
        button_refresh.setGeometry(40, 140, 120, 40)
        font = QtGui.QFont("consolas", 12)
        button_refresh.setFont(font)

        button_refresh = QPushButton("Disonnect", self)
        button_refresh.setGeometry(180, 140, 120, 40)
        font = QtGui.QFont("consolas", 12)
        button_refresh.setFont(font)

    def background_init(self):
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("pics/purple.jpg")))
        self.setPalette(window_pale)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Battery_Window(1)
    sys.exit(app.exec_())