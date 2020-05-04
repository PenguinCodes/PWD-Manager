# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 240, 151, 41))
        self.label.setObjectName("label")

        self.pwfield = QtWidgets.QTextEdit(self.centralwidget)
        self.pwfield.setGeometry(QtCore.QRect(230, 220, 431, 70))
        self.pwfield.setPlaceholderText("")
        self.pwfield.setObjectName("pwfield")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(250, 330, 121, 61))
        self.confirm.setObjectName("confirm")

        self.forgot = QtWidgets.QPushButton(self.centralwidget)
        self.forgot.setGeometry(QtCore.QRect(500, 330, 121, 61))
        self.forgot.setObjectName("forgot")
        self.disp = QtWidgets.QLabel(self.centralwidget)
        self.disp.setGeometry(QtCore.QRect(250, 440, 331, 51))
        self.disp.setObjectName("disp")

        MainWindow.setCentralWidget(self.centralwidget)
        self.confirm.clicked.connect(self.click("Confirm"))
        self.forgot.clicked.connect(self.click("Forgot"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def click(self,t):
        self.disp.setText("t")







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Master Password"))
        self.confirm.setText(_translate("MainWindow", "PushButton"))
        self.forgot.setText(_translate("MainWindow", "PushButton"))
        self.disp.setText(_translate("MainWindow", "TextLabel"))
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())