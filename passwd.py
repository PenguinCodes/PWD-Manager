from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys




#GUI
class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PassWord Manager")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("")
        self.label.setGeometry(50, 50, 50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText("You Pressed Button")
        self.label.adjustSize()
    #


def cik():
    print("Clicked")

def window():
    app = QApplication(sys.argv)
    wind = mywindow()
    wind.show()
    sys.exit(app.exec_())

window()