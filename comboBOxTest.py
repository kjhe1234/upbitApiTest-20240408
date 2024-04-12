import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/comboTest.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_setting()
        self.comboBox.currentIndexChanged.connect(self.menu_select)

    def comboBox_setting(self):  # 콤보박스 셋팅
        menulist = ['월요일', '화요일', '수요일', '목요일', '금요일']

        menulist = sorted(menulist)

        self.comboBox.addItems(menulist)

    def menu_select(self):  # 콤보박스 메뉴가 변경되었을때 호출되는 함수
        comboText = self.comboBox.currentText()

        self.output_label.setText(comboText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

