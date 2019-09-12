# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSharingConsole.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from after import Ui_after

class Ui_FileSharingConsole(object):
    def after_clicked(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_after()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, FileSharingConsole):
        FileSharingConsole.setObjectName("FileSharingConsole")
        FileSharingConsole.resize(640, 480)
        self.press = QtWidgets.QPushButton(FileSharingConsole)
        self.press.setGeometry(QtCore.QRect(190, 230, 93, 28))
        self.press.setObjectName("press")

        self.retranslateUi(FileSharingConsole)
        QtCore.QMetaObject.connectSlotsByName(FileSharingConsole)

        self.press.clicked.connect(self.after_clicked)

    def retranslateUi(self, FileSharingConsole):
        _translate = QtCore.QCoreApplication.translate
        FileSharingConsole.setWindowTitle(_translate("FileSharingConsole", "File Sharing"))
        self.press.setText(_translate("FileSharingConsole", "Press"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileSharingConsole = QtWidgets.QDialog()
    ui = Ui_FileSharingConsole()
    ui.setupUi(FileSharingConsole)
    FileSharingConsole.show()
    sys.exit(app.exec_())
