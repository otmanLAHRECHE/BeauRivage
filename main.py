# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from PyQt5 import Qt, uic, QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QApplication

import modules
from modules import *
from modules import main_app
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'EPSP_Djanet.EPSP_Guard.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./ui/splash_screen.ui", self)

        self.counter = 0
        self.jumper = 0




        self.centralwidget = self.findChild(QtWidgets.QWidget, "centralwidget")


        self.circularProgressBarBase = self.findChild(QtWidgets.QFrame, "circularProgressBarBase")


        self.circularProgress = self.findChild(QtWidgets.QFrame, "circularProgress")


        self.circularBg = self.findChild(QtWidgets.QFrame, "circularBg")


        self.container = self.findChild(QtWidgets.QFrame, "container")


        self.widget = self.findChild(QtWidgets.QWidget, "widget")


        self.gridLayout = self.findChild(QtWidgets.QGridLayout, "gridLayout")


        self.labelTitle = self.findChild(QtWidgets.QLabel, "labelTitle")



        self.labelPercentage = self.findChild(QtWidgets.QLabel, "labelPercentage")


        self.labelLoadingInfo = self.findChild(QtWidgets.QLabel, "labelLoadingInfo")



        self.labelCredits = self.findChild(QtWidgets.QLabel, "labelCredits")

        self.progressBarValue(0)


        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.circularBg.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)


    def progress(self):

        value = self.counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(self.jumper))

        if (value > self.jumper):

            self.labelPercentage.setText(newHtml)
            self.jumper += 1


        if value >= 100: value = 1.000
        self.progressBarValue(value)




        self.counter += 0.5


    def progressBarValue(self, value):


        styleSheet = """
                QFrame{
                	border-radius: 150px;
                	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
                }
                """


        progress = (100 - value) / 100.0


        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)


        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)


        self.circularProgress.setStyleSheet(newStylesheet)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/icons/app_icon.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
