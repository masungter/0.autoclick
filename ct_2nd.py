import sys, UI
import pyautogui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QTimer


class MainDialog(QDialog, UI.Ui_C):
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.click_1)
        self.pushButton_2.clicked.connect(self.click_2)


    def click_1(self):
        self.timer = QTimer()
        self.num_click = 0

        self.x = int(self.lineEdit_1.text())
        self.y = int(self.lineEdit_2.text())

        self.timer.start(2000)
        self.timer.timeout.connect(self.mouse_click2)

    def mouse_click(self):
        pyautogui.click(self.x, self.y)
        self.num_click += 1

        if self.num_click == 1810:
            self.timer.stop()

    def mouse_click2(self):
        pyautogui.click(self.x, self.y, clicks=2, interval=0.5)
        pyautogui.moveRel(0, 10)
        pyautogui.doubleClick()
        self.num_click += 1

        if self.num_click == 361:
            self.timer.stop()


    def click_2(self):
        position = pyautogui.position()
        self.lineEdit_1.setText(str(position[0]))
        self.lineEdit_2.setText(str(position[1]))

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()


