from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import uic

class MyWidget(QWidget):
    def __init__(self,parent=None):
        super(MyWidget, self).__init__(parent)
        uic.loadUi('my_widget.ui',self)

        self.setNumber(0)

    @pyqtSlot(int)
    def setNumber(self, val):
        self.spinBox.setValue(val)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())