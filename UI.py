# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_C(object):
    def setupUi(self, C):
        C.setObjectName("C")
        C.resize(240, 72)
        self.horizontalLayoutWidget = QtWidgets.QWidget(C)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout.addWidget(self.lineEdit_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(C)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(11, 37, 221, 30))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_2.addWidget(self.pushButton_1)

        self.retranslateUi(C)
        QtCore.QMetaObject.connectSlotsByName(C)

    def retranslateUi(self, C):
        _translate = QtCore.QCoreApplication.translate
        C.setWindowTitle(_translate("C", "click"))
        self.pushButton_2.setText(_translate("C", "find coordinate"))
        self.pushButton_1.setText(_translate("C", "click"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    C = QtWidgets.QDialog()
    ui = Ui_C()
    ui.setupUi(C)
    C.show()
    sys.exit(app.exec_())
