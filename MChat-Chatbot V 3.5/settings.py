from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(442, 317)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphics\\Icons window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        Settings.setLayoutDirection(QtCore.Qt.LeftToRight)
        Settings.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.line1_2 = QtWidgets.QLabel(self.centralwidget)
        self.line1_2.setGeometry(QtCore.QRect(-360, -10, 954, 23))
        self.line1_2.setText("")
        self.line1_2.setPixmap(QtGui.QPixmap("Graphics\\line.png"))
        self.line1_2.setObjectName("line1_2")
        self.line1_3 = QtWidgets.QLabel(self.centralwidget)
        self.line1_3.setGeometry(QtCore.QRect(-120, 300, 954, 23))
        self.line1_3.setText("")
        self.line1_3.setPixmap(QtGui.QPixmap("Graphics\\line.png"))
        self.line1_3.setObjectName("line1_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(220, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.radioButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Graphics\\mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton.setIcon(icon1)
        self.radioButton.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 170, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.settings_save = QtWidgets.QPushButton(self.centralwidget)
        self.settings_save.setGeometry(QtCore.QRect(310, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settings_save.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Graphics\\settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_save.setIcon(icon2)
        self.settings_save.setIconSize(QtCore.QSize(25, 25))
        self.settings_save.setAutoDefault(False)
        self.settings_save.setDefault(False)
        self.settings_save.setFlat(True)
        self.settings_save.setObjectName("settings_save")
        self.settings_save.clicked.connect(lambda: self.checkradio())

       
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 26))
        self.menubar.setObjectName("menubar")
        Settings.setMenuBar(self.menubar)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def checkradio(self):
        if self.radioButton.isChecked() == True:
                tts_toggle_var = True
        else:
            tts_toggle_var = False
        return tts_toggle_var
    
    
    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        Settings.setStatusTip(_translate("Settings", "Click SAVE before closing"))
        self.label.setText(_translate("Settings", "Text to speech "))
        self.label_2.setText(_translate("Settings", "MChat | Settings "))
        self.radioButton.setText(_translate("Settings", "Enable"))
        self.label_3.setText(_translate("Settings", "More personalization options coming soon.."))
        self.settings_save.setText(_translate("Settings", "Save "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QMainWindow()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

