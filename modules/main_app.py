from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHeaderView

import modules


class MainAppUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainAppUi, self).__init__()
        uic.loadUi("./ui/main.ui", self)

        modules.Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "COMPLEXE BEAU RIVAGE Zelfana"
        description = "COMPLEXE BEAU RIVAGE Application"
        # APPLY TEXTS
        self.setWindowTitle(title)

        self.appMargins = self.findChild(QtWidgets.QVBoxLayout, "appMargins")

        self.bgApp = self.findChild(QtWidgets.QFrame, "bgApp")

        self.appLayout = self.findChild(QtWidgets.QHBoxLayout, "appLayout")

        self.leftMenuBg = self.findChild(QtWidgets.QFrame, "leftMenuBg")

        self.verticalLayout_3 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_3")

        self.topLogoInfo = self.findChild(QtWidgets.QFrame, "topLogoInfo")

        self.topLogo = self.findChild(QtWidgets.QFrame, "topLogo")

        self.titleLeftApp = self.findChild(QtWidgets.QLabel, "titleLeftApp")

        self.titleLeftDescription = self.findChild(QtWidgets.QLabel, "titleLeftDescription")

        self.leftMenuFrame = self.findChild(QtWidgets.QFrame, "leftMenuFrame")

        self.verticalMenuLayout = self.findChild(QtWidgets.QVBoxLayout, "verticalMenuLayout")

        self.toggleBox = self.findChild(QtWidgets.QFrame, "toggleBox")

        self.verticalLayout_4 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_4")

        self.toggleButton = self.findChild(QtWidgets.QPushButton, "toggleButton")

        self.verticalLayout_8 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_8")

        self.btn_home = self.findChild(QtWidgets.QPushButton, "btn_home")

        self.btn_widgets = self.findChild(QtWidgets.QPushButton, "btn_widgets")

        self.btn_new = self.findChild(QtWidgets.QPushButton, "btn_new")

        self.btn_save = self.findChild(QtWidgets.QPushButton, "btn_save")

        self.btn_exit = self.findChild(QtWidgets.QPushButton, "btn_exit")

        self.bottomMenu = self.findChild(QtWidgets.QFrame, "bottomMenu")

        self.verticalLayout_9 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_9")

        self.toggleLeftBox = self.findChild(QtWidgets.QPushButton, "toggleLeftBox")

        self.extraLeftBox = self.findChild(QtWidgets.QFrame, "extraLeftBox")

        self.extraColumLayout = self.findChild(QtWidgets.QVBoxLayout, "extraColumLayout")

        self.extraTopBg = self.findChild(QtWidgets.QFrame, "extraTopBg")

        self.verticalLayout_5 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_5")

        self.extraTopLayout = self.findChild(QtWidgets.QGridLayout, "extraTopLayout")

        self.extraIcon = self.findChild(QtWidgets.QFrame, "extraIcon")

        self.extraLabel = self.findChild(QtWidgets.QLabel, "extraLabel")

        self.extraCloseColumnBtn = self.findChild(QtWidgets.QPushButton, "extraCloseColumnBtn")

        self.extraContent = self.findChild(QtWidgets.QFrame, "extraContent")

        self.verticalLayout_12 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_12")

        self.extraTopMenu = self.findChild(QtWidgets.QFrame, "extraTopMenu")

        self.verticalLayout_11 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_11")


        self.btn_share = self.findChild(QtWidgets.QPushButton, "btn_share")


        self.btn_adjustments = self.findChild(QtWidgets.QPushButton, "btn_adjustments")


        self.btn_more = self.findChild(QtWidgets.QPushButton, "btn_more")


        self.extraCenter = self.findChild(QtWidgets.QFrame, "extraCenter")


        self.verticalLayout_10 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_10")


        self.textEdit = self.findChild(QtWidgets.QTextEdit, "textEdit")


        self.extraBottom = self.findChild(QtWidgets.QFrame, "extraBottom")


        self.contentBox = self.findChild(QtWidgets.QFrame, "contentBox")


        self.verticalLayout_2 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_2")


        self.contentTopBg = self.findChild(QtWidgets.QFrame, "contentTopBg")


        self.horizontalLayout = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout")


        self.leftBox = self.findChild(QtWidgets.QFrame, "leftBox")


        self.horizontalLayout_3 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_3")


        self.titleRightInfo = self.findChild(QtWidgets.QLabel, "titleRightInfo")


        self.rightButtons = self.findChild(QtWidgets.QFrame, "rightButtons")


        self.horizontalLayout_2 = self.findChild(QtWidgets.QFrame, "horizontalLayout_2")


        self.settingsTopBtn = self.findChild(QtWidgets.QPushButton, "settingsTopBtn")


        self.minimizeAppBtn = self.findChild(QtWidgets.QPushButton, "minimizeAppBtn")


        self.maximizeRestoreAppBtn = self.findChild(QtWidgets.QPushButton, "maximizeRestoreAppBtn")


        self.closeAppBtn = self.findChild(QtWidgets.QPushButton, "closeAppBtn")


        self.contentBottom = self.findChild(QtWidgets.QFrame, "contentBottom")


        self.verticalLayout_6 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_6")


        self.content = self.findChild(QtWidgets.QFrame, "content")


        self.horizontalLayout_4 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_4")


        self.pagesContainer = self.findChild(QtWidgets.QFrame, "pagesContainer")


        self.verticalLayout_15 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_15")


        self.stackedWidget = self.findChild(QtWidgets.QStackedWidget, "stackedWidget")

        self.home = self.findChild(QtWidgets.QWidget, "home")


        self.widgets = self.findChild(QtWidgets.QWidget, "widgets")


        self.verticalLayout = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout")


        self.row_1 = self.findChild(QtWidgets.QFrame, "row_1")


        self.verticalLayout_16 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_16")


        self.frame_div_content_1 = self.findChild(QtWidgets.QFrame, "frame_div_content_1")


        self.verticalLayout_17 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_17")


        self.frame_title_wid_1 = self.findChild(QtWidgets.QFrame, "frame_title_wid_1")


        self.verticalLayout_18 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_18")


        self.labelBoxBlenderInstalation = self.findChild(QtWidgets.QFrame, "labelBoxBlenderInstalation")


        self.frame_content_wid_1 = self.findChild(QtWidgets.QFrame, "frame_content_wid_1")


        self.horizontalLayout_9 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_9")


        self.gridLayout = self.findChild(QtWidgets.QGridLayout, "gridLayout")


        self.lineEdit = self.findChild(QtWidgets.QLineEdit, "lineEdit")


        self.pushButton = self.findChild(QtWidgets.QPushButton, "pushButton")


        self.labelVersion_3 = self.findChild(QtWidgets.QLabel, "labelVersion_3")


        self.row_2 = self.findChild(QtWidgets.QFrame, "row_2")


        self.verticalLayout_19 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_19")


        self.gridLayout_2 = self.findChild(QtWidgets.QGridLayout, "gridLayout_2")


        self.checkBox = self.findChild(QtWidgets.QCheckBox, "checkBox")


        self.radioButton = self.findChild(QtWidgets.QRadioButton, "radioButton")


        self.verticalSlider = self.findChild(QtWidgets.QSlider, "verticalSlider")


        self.verticalScrollBar = self.findChild(QtWidgets.QScrollBar, "verticalScrollBar")


        self.scrollArea = self.findChild(QtWidgets.QScrollArea, "scrollArea")


        self.scrollAreaWidgetContents = self.findChild(QtWidgets.QWidget, "scrollAreaWidgetContents")


        self.horizontalLayout_11 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_11")


        self.plainTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "plainTextEdit")


        self.comboBox = self.findChild(QtWidgets.QComboBox, "comboBox")


        self.horizontalScrollBar = self.findChild(QtWidgets.QScrollBar, "horizontalScrollBar")



        self.commandLinkButton = self.findChild(QtWidgets.QCommandLinkButton, "commandLinkButton")


        self.horizontalSlider = self.findChild(QtWidgets.QSlider, "horizontalSlider")


        self.row_3 = self.findChild(QtWidgets.QFrame, "row_3")


        self.horizontalLayout_12 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_12")


        self.tableWidget = self.findChild(QtWidgets.QTableWidget, "tableWidget")


        self.new_page = self.findChild(QtWidgets.QWidget, "new_page")


        self.verticalLayout_20 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_20")


        self.label = self.findChild(QtWidgets.QLabel, "label")



        self.extraRightBox = self.findChild(QtWidgets.QFrame, "extraRightBox")


        self.verticalLayout_7 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_7")


        self.themeSettingsTopDetail = self.findChild(QtWidgets.QFrame, "themeSettingsTopDetail")


        self.contentSettings = self.findChild(QtWidgets.QFrame, "contentSettings")

        self.verticalLayout_13 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_13")


        self.topMenus = self.findChild(QtWidgets.QFrame, "topMenus")

        self.verticalLayout_14 = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout_14")

        self.btn_message = self.findChild(QtWidgets.QPushButton, "btn_message")


        self.btn_print = self.findChild(QtWidgets.QPushButton, "btn_print")


        self.btn_logout = self.findChild(QtWidgets.QPushButton, "btn_logout")


        self.bottomBar = self.findChild(QtWidgets.QPushButton, "bottomBar")


        self.horizontalLayout_5 = self.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_5")


        self.creditsLabel = self.findChild(QtWidgets.QLabel, "creditsLabel")


        self.version = self.findChild(QtWidgets.QLabel, "version")


        self.frame_size_grip = self.findChild(QtWidgets.QFrame, "frame_size_grip")



        self.titleRightInfo.setText(description)


        self.toggleButton.clicked.connect(lambda: modules.UIFunctions.toggleMenu(self, True))

        modules.UIFunctions.uiDefinitions(self)
        self.maximizeRestoreAppBtn.clicked.connect(lambda: modules.UIFunctions.maximize_restore(self))


        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        self.btn_home.clicked.connect(self.buttonClick)
        self.btn_widgets.clicked.connect(self.buttonClick)
        self.btn_new.clicked.connect(self.buttonClick)
        self.btn_save.clicked.connect(self.buttonClick)



        def openCloseLeftBox():
            modules.UIFunctions.toggleLeftBox(self, True)
        self.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            modules.UIFunctions.toggleRightBox(self, True)
        self.settingsTopBtn.clicked.connect(openCloseRightBox)



        useCustomTheme = True


        if useCustomTheme:
            modules.UIFunctions.theme(self, "themes/py_dracula_light.qss", True)
            modules.AppFunctions.setThemeHack(self)


        self.stackedWidget.setCurrentWidget(self.home)
        self.btn_home.setStyleSheet(modules.UIFunctions.selectMenu(self.btn_home.styleSheet()))


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.stackedWidget.setCurrentWidget(self.home)
            modules.UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(modules.UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.stackedWidget.setCurrentWidget(self.widgets)
            modules.UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(modules.UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            self.stackedWidget.setCurrentWidget(self.new_page) # SET PAGE
            modules.UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(modules.UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU


        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        modules.UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')






