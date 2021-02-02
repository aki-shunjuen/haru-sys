from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Japanese, QtCore.QLocale.Japan))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Input1_btn.setGeometry(QtCore.QRect(440, 140, 112, 34))
        self.Input1_btn.setObjectName("Input1_btn")
        self.Input2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Input2_btn.setGeometry(QtCore.QRect(440, 200, 112, 34))
        self.Input2_btn.setObjectName("Input2_btn")
        self.Clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_btn.setGeometry(QtCore.QRect(440, 320, 112, 34))
        self.Clear_btn.setObjectName("Clear_btn")
        self.InputTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.InputTextBox.setGeometry(QtCore.QRect(70, 90, 291, 101))
        self.InputTextBox.setObjectName("InputTextBox")
        self.InputLabel = QtWidgets.QLabel(self.centralwidget)
        self.InputLabel.setGeometry(QtCore.QRect(30, 60, 75, 18))
        self.InputLabel.setObjectName("InputLabel")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(516, 40, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 0);\n"
"    background-color: rgb(128, 128, 128);\n"
"    font: 20pt \"MS UI Gothic\";\n"
"}")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.OutputTextBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutputTextBox.setGeometry(QtCore.QRect(70, 240, 291, 101))
        self.OutputTextBox.setObjectName("OutputTextBox")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(30, 210, 75, 18))
        self.OutputLabel.setObjectName("OutputLabel")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(430, 40, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.Clear_btn.clicked.connect(self.Clear_btn.click)
        #self.Input1_btn.clicked.connect(self.Input1_btn.click)
        #self.Input2_btn.clicked.connect(self.Input2_btn.click)
        #self.spinBox.valueChanged['int'].connect(self.spinBox.setValue)
        self.Input1_btn.clicked.connect(self.func1)
        self.Input2_btn.clicked.connect(self.func2)
        self.Clear_btn.clicked.connect(self.clear)
        self.spinBox.valueChanged['int'].connect(self.lcdout)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Input1_btn.setText(_translate("MainWindow", "Input 1"))
        self.Input2_btn.setText(_translate("MainWindow", "Input 2"))
        self.Clear_btn.setText(_translate("MainWindow", "Clear"))
        self.InputLabel.setText(_translate("MainWindow", "Input"))
        self.OutputLabel.setText(_translate("MainWindow", "Output"))

    def lcdout(self):
        self.lcdNumber.display(self.spinBox.text())

    def func1(self):
        self.OutputTextBox.setText("Input 1 Button has clicked!")
        self.lcdNumber.display(1)

    def func2(self):
        self.OutputTextBox.setText(self.InputTextBox.toPlainText())
        self.lcdNumber.display(2)

    def clear(self):
        self.InputTextBox.clear()
        self.OutputTextBox.clear()
        self.spinBox.setValue(0)
        self.lcdNumber.display(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())